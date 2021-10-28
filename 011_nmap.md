# NMAP

## ARP Scan 
```
sudo nmap -PR -sn MACHINE_IP/24
```

## ICMP Echo Scan
```
sudo nmap -PE -sn MACHINE_IP/24
```

## ICMP Timestamp Scan
```
sudo nmap -PP -sn MACHINE_IP/24
```

## ICMP Address Mask Scan
```
sudo nmap -PM -sn MACHINE_IP/24
```

## TCP SYN Ping Scan
```
sudo nmap -PS22,80,443 -sn MACHINE_IP/30
```

## TCP ACK Ping Scan
```
sudo nmap -PA22,80,443 -sn MACHINE_IP/30
```

## UDP Ping Scan
```
sudo nmap -PU53,161,162 -sn MACHINE_IP/30
```

## TCP Connect Scan
```
nmap -sT 10.10.154.20
```

## TCP SYN Scan
```
sudo nmap -sS 10.10.154.20
```

## UDP Scan
```
sudo nmap -sU 10.10.154.20
```

## TCP Null Scan
```
sudo nmap -sN 10.10.1.234
```

## TCP FIN Scan
```
sudo nmap -sF 10.10.1.234
```

## TCP Xmas Scan
```
sudo nmap -sX 10.10.1.234
```

## TCP Maimon Scan
```
sudo nmap -sM 10.10.1.234
```

## TCP ACK Scan
```
sudo nmap -sA 10.10.1.234
```

## TCP Window Scan
```
sudo nmap -sW 10.10.1.234
```

## Custom TCP Scan
```
sudo nmap --scanflags URGACKPSHRSTSYNFIN 10.10.1.234
```

## Spoofed Source IP
```
sudo nmap -S SPOOFED_IP 10.10.1.234
```

## Spoofed MAC Address
```
--spoof-mac SPOOFED_MAC
```

## Decoy Scan
```
nmap -D DECOY_IP,ME 10.10.1.234
```

## Idle (Zombie) Scan
```
sudo nmap -sI ZOMBIE_IP 10.10.1.234
```

## Fragment IP data into 8 bytes
```
-f
```

## Fragment IP data into 16 bytes
```
-ff
```

## --reason
```
explains how Nmap made its conclusion
```

## -v
```
verbose
```

## -vv
```
very verbose
```

## -d
```
debugging
```

## -dd
```
more details for debugging
```
