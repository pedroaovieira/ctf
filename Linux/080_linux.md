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


## Linux Decompression Commands

- **unzip archive.zip - Extracts zip file on Linux.

- **zipgrep *.txt archive.zip** - Search inside a .zip archive.

- **tar xf archive.tar** - Extract tar file Linux.

- **tar xvzf archive.tar.gz** - Extract a tar.gz file Linux.

- **tar xjf archive.tar.bz2** - Extract a tar.bz2 file Linux.

- **tar ztvf file.tar.gz | grep blah** - Search inside a tar.gz file.

- **gzip -d archive.gz** - Extract a gzip file Linux.

- **zcat archive.gz** - Read a gz file Linux without decompressing.

- **zless archive.gz** - Same function as the less command for .gz archives.

- **zgrep 'blah' /var/log/maillog*.gz** - Search inside .gz archives on Linux, search inside of compressed log files.

- **vim file.txt.gz** - Use vim to read .txt.gz files (my personal favorite).

- **upx -9 -o output.exe input.exe** - UPX compress .exe file Linux. 


## Linux Compression Commands

- **zip -r file.zip /dir/*** - Creates a .zip file on Linux.

- **tar cf archive.tar files** - Creates a tar file on Linux.

- **tar czf archive.tar.gz files** - Creates a tar.gz file on Linux.

- **tar cjf archive.tar.bz2 files** - Creates a tar.bz2 file on Linux.

- **gzip file** - Creates a file.gz file on Linux. 

## Linux File Commands

- **df -h blah
	

Display size of file / dir Linux.

- **diff file1 file2** - Compare / Show differences between two files on Linux.

- **md5sum file** - Generate MD5SUM Linux.

- **md5sum -c blah.iso.md5** - Check file against MD5SUM on Linux, assuming both file and .md5 are in the same dir.

- **file blah** - Find out the type of file on Linux, also displays if file is 32 or 64 bit.

- **dos2unix** - Convert Windows line endings to Unix / Linux.

- **base64 < input-file > output-file** - Base64 encodes input file and outputs a Base64 encoded file called output-file.

- **base64 -d < input-file > output-file** - Base64 decodes input file and outputs a Base64 decoded file called output-file.

- **touch -r ref-file new-file** - Creates a new file using the timestamp data from the reference file, drop the -r to simply create a file.

- **rm -rf** - Remove files and directories without prompting for confirmation. 



