# John


## Shadow file
```
sudo /usr/sbin/unshadow /etc/passwd /etc/shadow > passwords.txt

/usr/sbin/john --wordlist=/usr/share/wordlists/rockyou.txt passwords.txt
```


```
/etc/shadow

john --wordlist=/usr/share/wordlists/rockyou.txt shadow
```

## ZIP


## GPG
```
gpg2john file.asc > hash

john hash


```

## Cracking everything with John the Ripper
[Cracking with John the Ripper](https://bytesoverbombs.io/cracking-everything-with-john-the-ripper-d434f0f6dc1c)


