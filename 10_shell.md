## Spawning a Shell


## Spawning a TTY Shell
```
python -c 'import pty; pty.spawn("/bin/sh")'
python3 -c 'import pty;pty.spawn("/bin/bash")'

export TERM=xterm

CTRL+Z; stty raw -echo; fg
```

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
https://github.com/pentestmonkey/php-reverse-shell


## Web Shell
https://github.com/Arrexel/phpbash



