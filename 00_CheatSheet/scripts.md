# Scripts

## IP

{% code title="ip.sh" %}
```bash
###########################################################################
# Title: Script to set ip (tun0)
# Date: 12/10/2019
# Exploit Author: shell5
###########################################################################

export xip2=$(ifconfig eth0 | grep 'inet ' | awk -F'[: ]+' '{ print $3 }')

```
{% endcode %}

## Local IP

{% code title="local.sh" %}
```
#!/bin/bash

###########################################################################
# Title: 
# Date: 12/10/2019
# Exploit Author: shell5
###########################################################################

remote_ip() { ifconfig tun0 | grep 'inet ' | awk -F'[: ]+' '{ print $3 }'; }
export -f remote_ip
remote_ip

```
{% endcode %}

## Find File

```
find / -iname 40716.py 2>/dev/null
find / -type f -name teste.txt -print 2>/dev/null
```

## Spawn a TTY Shell

```
python -c 'import pty; pty.spawn("/bin/sh")'
python3 -c 'import pty;pty.spawn("/bin/bash")'

export TERM=xterm

CTRL+Z; stty raw -echo; fg
```





```
gobuster dir -u http://10.10.211.96 -x php,txt,tar,zip,old,bak -w /usr/share/wordlists/dirb/common.txt 


```

```
List all SUID files
find / -perm -4000 2>/dev/null
```
