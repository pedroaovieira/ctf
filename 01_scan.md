# Perform Host Discovery

## Hosts on network
```
netdiscover
```

## Local IP (eth0)
```
export local=$(ifconfig eth0 | grep 'inet ' | awk -F'[: ]+' '{ print $3 }')
```

## Local IP (tun0)
```
export vpn=$(ifconfig tun0 | grep 'inet ' | awk -F'[: ]+' '{ print $3 }')
```









The following are examples of host discovery techniques:\
• ARP ping scan\
• UDP ping scan\
• ICMP ping scan (ICMP ECHO ping, ICMP timestamp, ping ICMP, and address mask ping)\
• TCP ping scan (TCP SYN ping and TCP ACK ping)\
• IP protocol scan

• Perform host discovery using Nmap\
• Perform host discovery using Angry IP Scanner

{% hint style="info" %}
Lab Duration Time: **10 Minutes**
{% endhint %}

### 1.1 Perform Host Discovery using Nmap

```
nmap -sn 10.10.10.16
```

















VPN IP
```
remote_ip() { ifconfig tun0 | grep 'inet ' | awk -F'[: ]+' '{ print $3 }'; }

export target=10.10.211.96

echo $target



nmap -sC -sV -T4 -p1-65535 $target
