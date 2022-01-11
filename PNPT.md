KeepNote: http://keepnote.org/

CheryTree: https://www.giuspen.com/cherrytree/

GreenShot: https://getgreenshot.org/downloads/

FlameShot: https://github.com/lupoDharkael/flameshot

128 64 32 16 8 4 2 1 = 255
 1   1  1  1 1 1 1 1 = 255
 0   0  0  0 0 1 1 1 = 7



Please
Do
Not
Throw
Sausage
Pizza
Away

1 Physical - data cables
2 Data - switching, mac address
3 Network - routing, ip address
4 Transport - TPC / UDP
5 Session - session management
6 Presentation - WMV, HPEG, MOV
7 Application - HTTP, SMTP

Seven Second Subnetting: https://www.youtube.com/watch?v=ZxAwQB8TZsM

Subnet Guide: https://drive.google.com/file/d/1ETKH31-E7G-7ntEOlWGZcDZWuukmeHFe/view

https://ipaddressguide.com/cidr

ifconfig
iwconfig
arp -a
netstat -ano
route
ip a
ip n
ip r

github pimpmykali

############################

#!/bin/bash
if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.168.1"

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi

############################

for ip in $(cat ips.txt); do nmap $ip; done

for ip in $(cat ips.txt); do nmap $ip& done


- Reconnaissance
- Scanning & Enumeration
- Exploitation - Gaining Access
- Maintaining Access
- Covering Tracks


## Kioptrix

arp-scan -l

netdiscover -r 192.168.10.0/24

nmap -T4 -p- -A 192.168.10.22
nmap -T4 -p -A  -sU 192.168.10.22
nikto
dirbuster
dirb
gobuster



kioptrix
root:TwoCows2

blue
user:Password321!
administrator:Password456!

academy
root:tcm

butler
butler:JeNkIn5@44
administrator: A%rc!BcA!


systemctl list-timers

pspy

history

dnsrecon -r 127.0.0.0/24 -n 192.168.138.130 -d domain

