

  gobuster dir -u <MACHINE IP> -w /usr/share/dirb/wordlists/common.txt


  dirb

  
  dirsearch
```
  git clone https://github.com/maurosoria/dirsearch.git
  cd dirsearch
  pip3 install -r requirements.txt
  python3 dirsearch.py -u <URL> -e <EXTENSIONS>
```

hydra -t 4 -l jan -P <rockyou.txt directory> ssh://<MACHINE IP>
