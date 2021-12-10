# Scan

- [Scan](#scan)
  - [Network Scanning / Host Discovery](#network-scanning--host-discovery)
    - [Port and Service Scanning](#port-and-service-scanning)
      - [Common Ports](#common-ports)
      - [Nmap: Helpers](#nmap-helpers)
      - [Nmap: TCP Connect Scan (3-way handshake)](#nmap-tcp-connect-scan-3-way-handshake)
      - [Nmap: TCP Stealth Scan (TCP SYN Scan or Half-Open Scan)](#nmap-tcp-stealth-scan-tcp-syn-scan-or-half-open-scan)
      - [Nmap: Inverse TCP](#nmap-inverse-tcp)
      - [Nmap: XMAS](#nmap-xmas)
      - [Nmap: Maimon Scans](#nmap-maimon-scans)
      - [Nmap: ACK Scan - attempt to map firewall/filtering rules for target](#nmap-ack-scan---attempt-to-map-firewallfiltering-rules-for-target)
      - [Nmap: IDLE/IPID Scan Zombie](#nmap-idleipid-scan-zombie)
      - [Nmap: UDP Scan](#nmap-udp-scan)
      - [Nmap: SCTP INIT](#nmap-sctp-init)
      - [Nmap: COOKIE ECHO Scans](#nmap-cookie-echo-scans)
      - [Nmap: IPv6 Scan](#nmap-ipv6-scan)
      - [Nmap: Version Scan](#nmap-version-scan)
      - [Nmap: Scan Optimizations](#nmap-scan-optimizations)
    - [Nmap: Target OS Identification Techniques](#nmap-target-os-identification-techniques)
      - [Nmap: IDS and Firewall Evasion](#nmap-ids-and-firewall-evasion)
      - [Hping3](#hping3)
      - [Metasploit](#metasploit)
      - [Other Port and Service Scanning Tools](#other-port-and-service-scanning-tools)

---

## Network Scanning / Host Discovery

- sweeper.sh

``` bash
#!/bin/bash

read -p "Enter IP subnet --> " IP
for i in {1..254}
do
  ping -c 1 $IP.$i | grep ^64 | awk '{print $4}' | cut -d ":" -f 1 &
done

```

---

- Nmap - <https://nmap.org/>
  - `nmap -sn targetIP` -sn: disables port scan / ping scan
  - `nmap -sn 10.10.10.0/24` ping sweep on subnet 10.10.10
  - `nmap -sn -PR targetIP`
    - **-PR**: performs ARP ping scan
    - -PU: performs the UDP ping scan
    - -PE: performs the ICMP ECHO ping scan
    - -PP: performs ICMP timestamp ping scan
    - -PM: performs ICMP address mask ping scan
    - -PS: performs TCP SYN Ping Scan
    - -PA: performs TCP ACK Ping Scan
    - **-PO**: performs IP Protocol Ping Scan

---

- Netdiscover
  - `sudo netdiscover -i eth0 -r 10.10.10.0/24` - whole subnet
- **nmapAutomator**  - <https://github.com/21y4d/nmapAutomator>
  - `nmapAutomator localIP -t Network`  - whole subnet
  - `nmapAutomator -H $target -t Port`
  - `nmapAutomator -H $target -t Full`
- Unicornscan - <http://unicornscan.org/>
  - `unicornscan -msf -v 192.168.1.1/24` - whole subnet
  - `sudo unicornscan -r30 -mT $target`
- Masscan - <https://github.com/robertdavidgraham/masscan>
  - `masscan -p22,80,445 192.168.1.0/24` - whole network ports 22 and 80
- Metasploit - <https://www.metasploit.com/>
- hping3 - <http://www.hping.org/>
  - `hping3 -A target_IP -p 80 -c 5`
- SolarWinds Engineer's Toolset - <https://www.solarwinds.com/engineers-toolset>
- PRTG Network Monitor - <https://www.paessler.com/prtg>
- Fing - <https://www.fing.io>

---

### Port and Service Scanning

#### Common Ports

- 21:FTP
- 22:SSH
- 23:Telnet
- 25:SMTP
- 53:DNS
- 80:HTTP
- 110:POP3
- 111:RPC
- 137-139:NETBios
- 143:IMAP
- 161:SNMP (TCP/UDP)
- 443:HTTPS
- 445:SMB/CIFS (Server Message Block / Common Internet File System)
- 3306:mysql
- 8080:proxy
- 6667:irc

---

#### Nmap: Helpers

- **`-v`** verbose
- `-vv` very verbose
- `-oN/-oX` Output scan in normal/xms
- `--reason` Display the reason a port is in a particular state
- `find / -name *.nse 2>/dev/null`
- `--script=script.nse`

#### Nmap: TCP Connect Scan (3-way handshake)

- `nmap -sT $target`
  - slow
  - noisy / prone to detection
  - may crash services

#### Nmap: TCP Stealth Scan (TCP SYN Scan or Half-Open Scan)

- `nmap -sS $target`
  - Much quieter than TCP Connect scans
  - Faster
  - Now detectable by IDS/IPS

#### Nmap: Inverse TCP

- `nmap -sF $target --reason` (FIN)
- `nmap -sF $target --reason` (NULL)
- `--scanflags URGACKPSHRSTSYNFIN`

#### Nmap: XMAS

- `nmap -sX $target  --reason`

#### Nmap: Maimon Scans

- `nmap -sM $target  --reason`

#### Nmap: ACK Scan - attempt to map firewall/filtering rules for target

- `nmap -sA <targetIP>`

#### Nmap: IDLE/IPID Scan Zombie

- `nmap -Pn -sI 10.0.10.50 <targetIP>`
  - *10.0.10.50 is the IP of a Printer/Zombie*

IDLE Scan - <https://nmap.org/book/idlescan.html>

#### Nmap: UDP Scan

- `sudo nmap -sU -p 22,69 <targetIP> --packet-trace`
  - very slow
  - maybe overlooked

#### Nmap: SCTP INIT

- `nmap -sY <targetIP>`

#### Nmap: COOKIE ECHO Scans

- `nmap -sZ <targetIP>`

#### Nmap: IPv6 Scan

- `nmap -6 <targetIP>`

#### Nmap: Version Scan

- `nmap -sV <targetIP>`

#### Nmap: Scan Optimizations

- `-n`
- `-Pn`
- `-p` ports
- `-T1-T5` Speed

### Nmap: Target OS Identification Techniques

- `nmap -O <targetIP>` - performs the OS discovery
- `nmap -A <targetIP>` - perform an aggressive scan
- `nmap --script smb-os-discovery.nse target_IP`
- unicornscan
  - `unicornscan <targetIP> -iV`

#### Nmap: IDS and Firewall Evasion

- Packet Fragmentation
  - `nmap -f`
- IP Address Decoy
  - `nmap -D <decoy1>,<decoy2> targetIP`
- Source IP Address Spoofing
  - `nmap -S <SPOOF_IP>`
- Source Port Modification
- Use a port that's not being filtered by the target
- i.e. 80,53,443,3389,etc
  - `nmap -g <PORT>`
- Randomizing Hosts
  - `nmap --randomize-hosts`
- Proxy Servers
  - `nmap --proxies`

---

#### Hping3

- Hping3 - <http://www.hping.org/>
  - `hping3 -A target_IP -p 80 -c 5`

#### Metasploit

- Metasploit - <https://www.metasploit.com/>

```bash
msfdb init
service postgresql start
msfconsole
msf > db_status
nmap -Pn -sS -A -oX Test 10.10.10.0/24
db_import Test
hosts -> To show all available hosts in the subnet
db_nmap -sS -A 10.10.10.16 -> To extract services of particular machine
services -> to get all available services in a subnet
```

- <https://www.offensive-security.com/metasploit-unleashed/port-scanning/>

---

#### Other Port and Service Scanning Tools

- Angry IP Scanner - <https://angryip.org/> - (win/lin/mac)
- MegaPing - <http://magnetosoft.com/products-downloads/>
- NetScanTools Pro - <https://www.netscantools.com/nstpromain.html>

---
