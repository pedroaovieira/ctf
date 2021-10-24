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
echo "10.10.246.106 team.thm" | sudo tee -a /etc/hosts

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
