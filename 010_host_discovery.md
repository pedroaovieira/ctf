# Host Discovery

## Hosts on network
```
netdiscover
```
```
nmap -sn 192.168.0.1/24
```

## Local IP (eth0)
```
export ip=$(ifconfig eth0 | grep 'inet ' | awk -F'[: ]+' '{ print $3 }')
echo $ip
```

## VPN IP (tun0)
```
export vpn=$(ifconfig tun0 | grep 'inet ' | awk -F'[: ]+' '{ print $3 }')
echo $vpn
```

## Target
```
export target=192.168.17.60
echo $target

echo $target "team.thm" | sudo tee -a /etc/hosts

export folder='target'
echo $folder

mkdir $folder
cd $folder
``` 

## NMAP
```
mkdir nmap
ports=$(nmap -p- --min-rate=1000 -T4 $target | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
nmap -p$ports -sC -sV -Pn $target -oA nmap/$folder

nmap -sC -sV -T4 -p1-65535 $target

nmap -A -sC -sV -O -vvv <ip>
```

## rustscan
```
rustscan -a $target --ulimit 5000 -- -sV -sC -A -oN nmap_output.txt
```


## nmapAutomator
```
git clone https://github.com/21y4d/nmapAutomator
./nmapAutomator.sh $target Basic
```

## whois 
to query WHOIS servers
```
whois DOMAIN_NAME

whois tryhackme.com
```

## nslookup
to query DNS servers

### Query type
**A** 	IPv4 Addresses

**AAAA** 	IPv6 Addresses

**CNAME** 	Canonical Name

**MX** 	Mail Servers

**SOA** 	Start of Authority

**TXT** 	TXT Records

[dnsdumpster](https://dnsdumpster.com/)


```
nslookup OPTIONS DOMAIN_NAME SERVER

nslookup -type=A tryhackme.com 1.1.1.1
```

## dig
to query DNS servers

```
dig tryhackme.com A
```


## ping
```
ping -c 10 10.10.160.200 on Linux or macOS
ping 	ping -n 10 10.10.160.200 on MS Windows
```

## traceroute
```
traceroute 10.10.160.200 on Linux or macOS
```

## tracert
```
tracert 10.10.160.200 on MS Windows
```

## telnet
```
telnet 10.10.160.200 PORT_NUMBER
```

## netcat
### netcat as client
```
nc 10.10.160.200 PORT_NUMBER
```

### netcat as server
```
nc -lvnp PORT_NUMBER
```

## NMAP

### ARP Scan 
```
sudo nmap -PR -sn MACHINE_IP/24
```

### ICMP Echo Scan
```
sudo nmap -PE -sn MACHINE_IP/24
```

### ICMP Timestamp Scan
```
sudo nmap -PP -sn MACHINE_IP/24
```

### ICMP Address Mask Scan
```
sudo nmap -PM -sn MACHINE_IP/24
```

### TCP SYN Ping Scan
```
sudo nmap -PS22,80,443 -sn MACHINE_IP/30
```

### TCP ACK Ping Scan
```
sudo nmap -PA22,80,443 -sn MACHINE_IP/30
```

### UDP Ping Scan
```
sudo nmap -PU53,161,162 -sn MACHINE_IP/30
```

### TCP Connect Scan
```
nmap -sT 10.10.154.20
```

### TCP SYN Scan
```
sudo nmap -sS 10.10.154.20
```

### UDP Scan
```
sudo nmap -sU 10.10.154.20
```


TCP Null Scan 	sudo nmap -sN 10.10.1.234
TCP FIN Scan 	sudo nmap -sF 10.10.1.234
TCP Xmas Scan 	sudo nmap -sX 10.10.1.234
TCP Maimon Scan 	sudo nmap -sM 10.10.1.234
TCP ACK Scan 	sudo nmap -sA 10.10.1.234
TCP Window Scan 	sudo nmap -sW 10.10.1.234
Custom TCP Scan 	sudo nmap --scanflags URGACKPSHRSTSYNFIN 10.10.1.234
Spoofed Source IP 	sudo nmap -S SPOOFED_IP 10.10.1.234
Spoofed MAC Address 	--spoof-mac SPOOFED_MAC
Decoy Scan 	nmap -D DECOY_IP,ME 10.10.1.234
Idle (Zombie) Scan 	sudo nmap -sI ZOMBIE_IP 10.10.1.234
Fragment IP data into 8 bytes 	-f
Fragment IP data into 16 bytes 	-ff
