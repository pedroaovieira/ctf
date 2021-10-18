# Perform Host Discovery

## Hosts on network

```
gobuster dir -u $target -w /usr/share/dirb/wordlists/common.txt

```



dirb $target

  
  dirsearch
```
  git clone https://github.com/maurosoria/dirsearch.git
  cd dirsearch
  pip3 install -r requirements.txt
  python3 dirsearch.py -u <URL> -e <EXTENSIONS>
```


enum4linux <machien_ip>


hydra -l <username> -P /usr/share/wordlists

hydra -t 4 -l jan -P <rockyou.txt directory> ssh://<MACHINE IP>

  
  
  
  sudo -l


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
  
  
  
