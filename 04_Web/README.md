# Web <https://tryhackme.com/module/intro-to-web-hacking>

## Walking An Application

## Content Discovery

- robots.txt
- favicon.ico - framework used
- sitemap.xml
- HTTP Headers
- Framework Stack
- Wappalyzer
- Wayback Machine
- GitHub
- S3 Buckets
- `ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://MACHINE_IP/FUZZ`
- `dirb http://MACHINE_IP/ /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt`
- `gobuster dir --url http://MACHINE_IP/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt`
- `feroxbuster`

## Subdomain Enumeration

## Authentication Bypass

## IDOR - Insecure Direct Object Reference

- Query Component
  - `http://site/profile?user_id=**1305**`
- Post Variables
- Cookies

## Cookie Manipulation

## Fuzzing

- Burp Suite Sniper
- Bur Suite Repeater

## File Inclusion

## SSRF

## Cross-site Scripting

## Command Injection

## SQL Injection

