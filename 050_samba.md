# SAMBA

nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse $target

smbclient //<ip>/anonymous

smbget -R smb://<ip>/anonymous
