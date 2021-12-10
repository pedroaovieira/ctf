# Enumeration

[[CEH Labs]](../labs-v11/04-enumeration-1/README.md)

---

### NetBIOS : 137 (UDP)

- nbtstat (Windows)
  - `nbtstat -a target_IP` NetBIOS name table of a remote computer
  - `nbtstat -c` Cache
  - `nbtstat 1-n` Names
  - `net use`
- nbtscan (Linux)
  - `nbtscan -r target_IP`
  - `nbtscan -v` for more output
- Nmap - <https://nmap.org/>
  - `nmap -sV --script nbstat.nse target_IP`

---

### SMB : 137,138 (UDP)  137,139,445 (TCP)

- Nmap - <https://nmap.org/>
  - `nmap -A -T4 -n -Pn -p 445 target_IP`
- net view (Windows)
  - `net view \\target_IP /ALL`
  - `net view example.com`
- enum4linux
  - `enum4linux -u user -p password -a target_IP`
  - `enum4linux -u user -p password -U target_IP`

  -a Do all simple enumeration
  -U get userlist
  -M get machine list*
  -S get sharelist
  -P get password policy information
  -G get group and member list
  -d be detailed, applies to -U and -S
  -u user specify username to use (default "")
  -p pass specify password to use (default "")

---

### SNMP : 161 (UDP)

- Community String
  - Basically a password
  - Default of 'public'
    - Default of READ access
  - 'private' is another commonly used string
    - Typically set to READ/WRITE

- Nmap - <https://nmap.org/>
  - `nmap -sU -p 161 target_IP`
- snmp-check - <http://www.nothink.org/codes/snmpcheck/index.php>
  - `snmp-check target_IP`
- onesixtyone - <https://github.com/trailofbits/onesixtyone>
  - `onesixtyone 10.10.10.0/24 public`

---

### LDAP : 389 (TCP/UDP)

- AD Explorer (Sysinternals) - <https://docs.microsoft.com/en-us/sysinternals/downloads/adexplorer>
- ldapsearch
  - `ldapsearch -LLL -x -H ldap://192.168.241.200 -b '' -s base'(objectclass=*)'`

---

### NTP : 123 (UDP)

- Nmap - <https://nmap.org/>
  - `sudo nmap -sU -n -Pn -p 123 target_IP`
- ntpdate
  - `-d` (debug info)
- ntptrace
  - Trace NTP servers to source
  - Could help map out network resources
- ntpdq & ntpdc
  - `host target_IP`
  - `version`
  - `peers`

---

### NFS : 2049 (TCP)

- Nmap - <https://nmap.org/>
  - `nmap -p 2049 target_IP`

- How do we check for NFS?
  - `nmap -A -T5 -n -Pn -p 2049 target_IP`
  - `rpcinfo -p target_IP`
  - `showmount -e target_IP`

- How do we access the NFS share?
  1. `mkdir /tmp/NFS`
  2. `sudo mount -t nfs target_IP:/path/to/share /tmp/NFS`
  3. `ls /tmp/NFS`

- SuperEnum - <https://github.com/p4pentest/SuperEnum>
  - `echo target > Target.txt; ./superenum`
- RPCScan - <https://github.com/hegusung/RPCScan>
  - `rpc-scan.py target_IP --rpc`

---

### SMTP : 25 (TCP)

- SMTP server commands
  - EHLO
  - VRFY
  - EXPN
  - RCPT TO

- Login directly
  - netcat
  - Telnet
- `smtp-user-enum`
  - `-U/-u` User list / single user
  - `-t` Target mail server (IP)
  - `-M` Mode (VRFY,EXPN,RCPT TO)

---

### DNS : 53 (TCP/UDP)

- dig
  - `dig ns www.certifiedhacker.com`
  - `dig @ns1.bluehost.com www.certifiedhacker.com axfr`
  - `dig axfr @nsztm1.digi.ninja zonetransfer.me`
- nslookup

    ```bash
    nslookup
    set querytype=soa
    certifiedhacker.com
    ```

- dnsrecon - <https://github.com/darkoperator/dnsrecon>
  - `dnsrecon -d www.certifiedhacker.com -z`

---

### RPC

- nmap
  - `nmap -p 111,2049 -A -T4 target_IP`

---

### FTP : 21 (TCP)

- Anonymous login?
  - anonymous:anonymous
  - Can anonymous upload?
- nmap
  - `nmap -p 21 target_IP`
  - `nmap -T4 -A -p 21 target_IP`

---

[[CEH Labs]](../labs-v11/04-enumeration-1/README.md)

---
