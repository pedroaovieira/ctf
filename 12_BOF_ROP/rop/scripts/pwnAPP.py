#!/usr/bin/python

###########################################################################
# Title: ROP exploit
# Date: 12/10/2019
# Exploit Author: shell5
###########################################################################

import sys
from pwn import *

app = sys.argv[1]
context.binary = app

print (context)
