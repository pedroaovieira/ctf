# Linux Fundamentals


## System Information Commands

- **whoami** - Shows currently logged in user on Linux.

- **id** - Shows currently logged in user and groups for the user.

- **last** - Shows last logged in users.

- **mount** - Show mounted drives.

- **df -h** - Shows disk usage in human readable output.

- **echo "user:passwd" | chpasswd** - Reset password in one line.

- **getent passwd** - List users on Linux.

- **strings /usr/local/bin/blah** - Shows contents of none text files, e.g. whats in a binary.

- **uname -ar** - Shows running kernel version.

- **PATH=$PATH:/my/new-path** - Add a new PATH, handy for local FS manipulation.

- **history** - Show bash history, commands the user has entered previously. 


## Redhat / CentOS / RPM Based Distros

- **cat /etc/redhat-release** - Shows Redhat / CentOS version number.

- **rpm -qa** - List all installed RPM's on an RPM based Linux distro.

- **rpm -q --changelog openvpn** - Check installed RPM is patched against CVE, grep the output for CVE. 


## Debian / Ubuntu / .deb Based Distros

- **cat /etc/debian_version** - Shows Debian version number.

- **cat /etc/*-release** - Shows Ubuntu version number.

- **dpkg -l** - List all installed packages on Debian / .deb based Linux distro. 


## Linux Network Commands

- **netstat -tulpn** - Show Linux network ports with process ID's (PIDs)

- **watch ss -stplu** - Watch TCP, UDP open ports in real time with socket summary.

- **lsof -i** - Show established connections.

- **macchanger -m MACADDR INTR** - Change MAC address on KALI Linux.

- **ifconfig eth0 192.168.2.1/24** - Set IP address in Linux.

- **ifconfig eth0:1 192.168.2.3/24** - Add IP address to existing network interface in Linux.

- **ifconfig eth0 hw ether MACADDR** - Change MAC address in Linux using ifconfig.

- **ifconfig eth0 mtu 1500** - Change MTU size Linux using ifconfig, change 1500 to your desired MTU.

- **dig -x 192.168.1.1** - Dig reverse lookup on an IP address.

- **host 192.168.1.1** - Reverse lookup on an IP address, in case dig is not installed.

- **dig @192.168.2.2 domain.com -t AXFR** - Perform a DNS zone transfer using dig.

- **host -l domain.com nameserver** - Perform a DNS zone transfer using host.

- **nbtstat -A x.x.x.x** - Get hostname for IP address.

- **ip addr add 192.168.2.22/24 dev eth0** - Adds a hidden IP address to Linux, does not show up when performing an ifconfig.

- **tcpkill -9 host google.com** - Blocks access to google.com from the host machine.

- **echo "1" > /proc/sys/net/ipv4/ip_forward** - Enables IP forwarding, turns Linux box into a router - handy for routing traffic through a box.

- **echo "8.8.8.8" > /etc/resolv.conf** - Use Google DNS. 
