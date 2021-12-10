# SAMBA

nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse $target

smbclient //<ip>/anonymous

smbget -R smb://<ip>/anonymous

  
enum4linux -a $target

  
smbmount //server/share /mnt/win -o user=username,password=password1

smbclient -U user \\\\server\\share

mount -t cifs -o username=user,password=password //x.x.x.x/share /mnt/share
