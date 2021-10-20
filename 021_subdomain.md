# Subdomain


## OSINT - SSL/TLS Certificates 
[crt](https://crt.sh)

[Google Certificates](https://transparencyreport.google.com/https/certificates)


## OSINT - Search Engines 
Google : -site:www.tryhackme.com  site:*.tryhackme.com

## DNS BruteForce

### dnsrecon [link](https://www.kali.org/tools/dnsrecon/)
```
dnsrecon -t brt -d acmeitsupport.thm
```

### sublist3r [link](https://www.kali.org/tools/sublist3r/)
```
./sublist3r.py -d acmeitsupport.thm
```

### fuff
```
ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://MACHINE_IP
```

```
ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://MACHINE_IP -fs {size}
```
the -fs switch, which tells ffuf to ignore any results that are of the specified size
