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
  
