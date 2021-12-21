# CheatSheet

## Tools

- <https://app.gitbook.com/s/-MO2nS1JusVF7PXAjY3d/cheatsheet/tools>

---

## Network discovery

- <https://app.gitbook.com/s/-MO2nS1JusVF7PXAjY3d/cheatsheet/chapter03>
- <https://github.com/pedroaovieira/ctf/blob/main/old/010_host_discovery.md>

&nbsp;

- wget https://raw.githubusercontent.com/21y4d/nmapAutomator/master/nmapAutomator.sh
- mkdir network
- ./nmapAutomator.sh -H 10.10.10.10 -t network -o network
- nmap -sn 192.168.0.1/24
- nmap -sn -PR 192.168.1.1/24 -oN ips.txt

---

## Host Ports

- <https://app.gitbook.com/s/-MO2nS1JusVF7PXAjY3d/cheatsheet/chapter04>


- export target=10.10.10.13

- ./nmapAutomator.sh -H 10.10.10.10 -t Full
- ./nmapAutomator.sh -H 10.10.10.10 -t UDP

- mkdir nmap
- ports=$(nmap -p- --min-rate=1000 -T4 $target | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
- nmap -p$ports -sC -sV -Pn $target -oA nmap/$folder

### NMAP

- <https://github.com/pedroaovieira/ctf/blob/main/old/011_nmap.md>

- nmap -A -T4 -vv -iL ips.txt -oN nmap.txt
- nmap -sU -sV -A -T4 -v -oN udp.txt

---

## - Responder LLMNR

- responder -I eth0
- usr\share\responder\logs

---

## Enumeration

- <https://app.gitbook.com/s/-MO2nS1JusVF7PXAjY3d/cheatsheet/chapter04>

---

## WEB

- View Source
- Blocked/Hidden content
- Network requests
- robots.txt
- sitemap.xml
- HTTP Headers - curl http://MACHINE_IP -v

---

### wordlists

- <https://github.com/pedroaovieira/ctf/blob/main/old/001_wordlists.md>

---

### Directory

- feroxbuster -u http://$target -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x html php
- gobuster -t 100 dir -e -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.13.49/island
- wfuzz -c -z file,/usr/share/wordlists/dirb/big.txt --hw 57 10.10.110.56:82/FUZZ.php

---

### Cewl

- cewl -w wordlist.txt -d 2 -m 5 www.certifiedhacker.com

---

### nmap

- nmap -T4 -A -v <Target Web Application> 
- telnet www.moviescope.com 80 
- GET / HTTP/1.0 

---

### whatweb

- whatweb -v <Target Web Application> 

---

### wpsan

- wpscan –-url http://10.10.10.10 -t 50 -U admin -P rockyou.txt

---

### Nikto

- nikto -h <Target Website> -Tuning x 

### sql

- <https://app.gitbook.com/s/-MO2nS1JusVF7PXAjY3d/cheatsheet/chapter15>

## Crack

- <https://app.gitbook.com/s/-MO2nS1JusVF7PXAjY3d/cheatsheet/tools>

## Stego

- <https://github.com/pedroaovieira/ctf/blob/main/old/110_steganography.md>

- Steghide
  - Hide
    - steghide embed -cf [img file] -ef [file to be hide]
    - steghide embed -cf 1.jpg -ef 1.txt
    - Enter password or skip
  - Extract
    - steghide info 1.jpg
    - steghide extract -sf 1.jpg
    - Enter password if it does exist
