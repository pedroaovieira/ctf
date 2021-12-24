# NMAP

## ARP Scan

- `sudo nmap -PR -sn MACHINE_IP/24`

## ICMP Echo Scan

- `sudo nmap -PE -sn MACHINE_IP/24`

## ICMP Timestamp Scan

- `sudo nmap -PP -sn MACHINE_IP/24`

## ICMP Address Mask Scan

- `sudo nmap -PM -sn MACHINE_IP/24`

## TCP SYN Ping Scan

- `sudo nmap -PS22,80,443 -sn MACHINE_IP/30`

## TCP ACK Ping Scan

- `sudo nmap -PA22,80,443 -sn MACHINE_IP/30`

## UDP Ping Scan

- `sudo nmap -PU53,161,162 -sn MACHINE_IP/30`

## TCP Connect Scan

- `nmap -sT 10.10.154.20`

## TCP SYN Scan

- `sudo nmap -sS 10.10.154.20`

## UDP Scan

- `sudo nmap -sU 10.10.154.20`

## TCP Null Scan

- `sudo nmap -sN 10.10.1.234`

## TCP FIN Scan

- `sudo nmap -sF 10.10.1.234`

## TCP Xmas Scan

- `sudo nmap -sX 10.10.1.234`

## TCP Maimon Scan

- `sudo nmap -sM 10.10.1.234`

## TCP ACK Scan

- `sudo nmap -sA 10.10.1.234`

## TCP Window Scan

- `sudo nmap -sW 10.10.1.234`

## Custom TCP Scan

- `sudo nmap --scanflags URGACKPSHRSTSYNFIN 10.10.1.234`

## Spoofed Source IP

- `sudo nmap -S SPOOFED_IP 10.10.1.234`

## Spoofed MAC Address

- `spoof-mac SPOOFED_MAC`

## Decoy Scan

- `nmap -D DECOY_IP,ME 10.10.1.234`

## Idle (Zombie) Scan

- `sudo nmap -sI ZOMBIE_IP 10.10.1.234`

## Fragment IP data into 8 bytes

- `\-f`

## Fragment IP data into 16 bytes

- `\-ff`

## explains how Nmap made its conclusion

- `--reason`

## -v

- `verbose`

## -vv

- `very verbose`

## -d

debugging

## -dd

more details for debugging


## Nmap Scripting Engine (NSE)

- /usr/share/nmap/scripts

auth - Authentication related scripts
broadcast - Discover hosts by sending broadcast messages
brute - Performs brute-force password auditing against logins
default - Default scripts, same as -sC
discovery - Retrieve accessible information, such as database tables and DNS names
dos - Detects servers vulnerable to Denial of Service (DoS)
exploit - Attempts to exploit various vulnerable services
external - Checks using a third-party service, such as Geoplugin and Virustotal
fuzzer - Launch fuzzing attacks
intrusive - Intrusive scripts such as brute-force attacks and exploitation
malware - Scans for backdoors
safe - Safe scripts that won’t crash the target
version - Retrieve service versions
vuln - Checks for vulnerabilities or exploit vulnerable services

\-sV determine service/version info on open ports
\-sV --version-light try the most likely probes (2)
\-sV --version-all try all available probes (9)
\-O detect OS
\--traceroute run traceroute to target
\--script=SCRIPTS Nmap scripts to run
\-sC or --script=default run default scripts
\-A equivalent to -sV -O -sC --traceroute
\-oN save output in normal format
\-oG save output in grepable format
\-oX save output in XML format
\-oA save output in normal, XML and Grepable formats
