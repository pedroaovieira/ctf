#!/usr/bin/env python

import requests
import re
import hashlib
from hashlib import md5


url = 'http://docker.hackthebox.eu:33485/'

sessao = requests.session()
out = sessao.get(url)
content = out.text

texto =  re.findall('h1 align=\'center\'>MD5 encrypt this string</h1><h3 align=\'center\'>(.*)</h3><center><form action="" method="post">',content)[0]


md5string = hashlib.md5(texto.encode('utf-8')).hexdigest()

data = {"hash": md5string}

out = sessao.post(url = url, data = data)

print(out.text)
