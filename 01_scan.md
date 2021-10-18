# Perform Host Discovery

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
```

## nmapAutomator
```
git clone https://github.com/21y4d/nmapAutomator
./nmapAutomator.sh $target Basic
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
