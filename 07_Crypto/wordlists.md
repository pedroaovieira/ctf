# Wordlists

- Daniel Miessler SecLists [link](https://github.com/danielmiessler/SecLists)

- Web-Content [link](https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content)

- Sec-IT [link](https://blog.sec-it.fr/en/2021/03/02/web-wordlists/)

## Directories

- /usr/share/seclists
- /usr/share/wordlists
- /usr/share/dirb/wordlists/common.txt
- /usr/share/dirb/wordlists/big.txt
- /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
- /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
- /usr/share/wordlists/wfuzz/general/megabeast.txt

## Indexes

- /usr/share/dirb/wordlists/indexes.txt

## Extensions

- /usr/share/dirb/wordlists/extensions_common.txt
- /usr/share/wordlists/wfuzz/general/mutations_common.txt

## Custom Worldlist

### CEWL

- Create a worldlist from a webpage: 
  - `cewl -w wordlist.txt -d 2 -m 5 $target`
    - \-d represents the depth to spider the website
    - \-m represents minimum word length

### CUPP - Common User Passwords Profiler

- <https://github.com/Mebus/cupp>

### CRUNCH

- <https://sourceforge.net/projects/crunch-wordlist/>

## Passwords

- /usr/share/seclists
- /usr/share/wordlists
- /usr/share/wordlists/dirb/others/best110.txt
- /usr/share/wordlists/dirb/others/best1050.txt
- /usr/share/wordlists/rockyou.txt

## FastTrack

/usr/share/wordlists/fasttrack.txt

## ROCKYOU

- /usr/share/wordlists/rockyou.txt - `sudo gunzip /usr/share/wordlists/rockyou.txt.gzwc -l /usr/share/wordlists/rockyou.txt`
- <https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt>

## Many Passwords

- <https://many-passwords.github.io/>
