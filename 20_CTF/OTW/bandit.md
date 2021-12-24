# Bandit

## Bandit0

```text
ssh bandit0@bandit.labs.overthewire.org -p 2220

bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

## Bandit1

ssh bandit1@bandit.labs.overthewire.org -p 2220  
  
bandit1@bandit:~$ cat ./-  
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

## Bandit2

ssh bandit2@bandit.labs.overthewire.org -p 2220  
  
bandit2@bandit:~$ cat "spaces in this filename"  
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit3 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit3@bandit.labs.overthewire.org -p 2220  
  
bandit3@bandit:~/inhere$ cat .hidden  
pIwrPrtPN36QITSp3EQaw936yaFoFgAB  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit4 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit4@bandit.labs.overthewire.org -p 2220  
  
bandit4@bandit:~/inhere$ file ./\*  
./-file00: data  
./-file01: data  
./-file02: data  
./-file03: data  
./-file04: data  
./-file05: data  
./-file06: data  
./-file07: ASCII text  
./-file08: data  
./-file09: data  
  
bandit4@bandit:~/inhere$ cat ./-file07  
koReBOKuIDDepwhWk7jZC0RTdopnAYKh  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit5 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit5@bandit.labs.overthewire.org -p 2220  
  
bandit5@bandit:~$ find inhere -size 1033c  
inhere/maybehere07/.file2  
bandit5@bandit:~$ cat inhere/maybehere07/.file2  
DXjZPULLxYr17uwoI01bNLQbtFemEgo7  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit6 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit6@bandit.labs.overthewire.org -p 2220  
  
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2&gt;/dev/null  
  
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password  
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit7 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit7@bandit.labs.overthewire.org -p 2220  
  
bandit7@bandit:~$ grep millionth data.txt  
millionth cvX2JJa4CFALtqS87jk27qwqGhBM9plV  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit8 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit8@bandit.labs.overthewire.org -p 2220  
  
bandit8@bandit:~$ sort data.txt \| uniq -c \|sort -r  
 1 UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit9 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit9@bandit.labs.overthewire.org -p 2220  
  
bandit9@bandit:~$ strings data.txt \|grep ==  
========== theP\`  
========== password  
L========== isA  
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit10 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit10@bandit.labs.overthewire.org -p 2220  
  
bandit10@bandit:~$ base64 -d data.txt  
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit11 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit11@bandit.labs.overthewire.org -p 2220  
  
alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"  
  
bandit11@bandit:~$ alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"  
  
bandit11@bandit:~$ cat data.txt \| rot13  
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit12 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit12@bandit.labs.overthewire.org -p 2220  
  
bandit12@bandit:/tmp/pvieira22$ file data.txt  
data.txt: ASCII text  
bandit12@bandit:/tmp/pvieira22$ xxd -r data.txt &gt; data2.bin  
bandit12@bandit:/tmp/pvieira22$ file data2.bin  
data2.bin: gzip compressed data, was "data2.bin", last modified: Thu Dec 28 13:34:36 2017, max compression, from Unix  
bandit12@bandit:/tmp/pvieira22$ mv data2.bin data2.gz  
bandit12@bandit:/tmp/pvieira22$ gunzip data2.gz  
bandit12@bandit:/tmp/pvieira22$ file data2  
data2: bzip2 compressed data, block size = 900k  
bandit12@bandit:/tmp/pvieira22$ mv data2 data2.bz2  
bandit12@bandit:/tmp/pvieira22$ bunzip2 data2.bz2  
bandit12@bandit:/tmp/pvieira22$ file data2  
data2: gzip compressed data, was "data4.bin", last modified: Thu Dec 28 13:34:36 2017, max compression, from Unix  
bandit12@bandit:/tmp/pvieira22$ mv data2 data2.gz  
bandit12@bandit:/tmp/pvieira22$ gunzip data2.gz  
bandit12@bandit:/tmp/pvieira22$ file data2  
data2: POSIX tar archive \(GNU\)  
bandit12@bandit:/tmp/pvieira22$ mv data2 data2.tar  
bandit12@bandit:/tmp/pvieira22$ tar -xvf data2.tar  
data5.bin  
bandit12@bandit:/tmp/pvieira22$ file data5.bin  
data5.bin: POSIX tar archive \(GNU\)  
bandit12@bandit:/tmp/pvieira22$ mv data5.bin data5.tar  
bandit12@bandit:/tmp/pvieira22$ tar -xvf data5.tar  
data6.bin  
bandit12@bandit:/tmp/pvieira22$ file data6.bin  
data6.bin: bzip2 compressed data, block size = 900k  
bandit12@bandit:/tmp/pvieira22$ mv data6.bin data6.bz2  
bandit12@bandit:/tmp/pvieira22$ bunzip2 data6.bz2  
bandit12@bandit:/tmp/pvieira22$ file data6  
data6: POSIX tar archive \(GNU\)  
bandit12@bandit:/tmp/pvieira22$ mv data6 data6.tar  
bandit12@bandit:/tmp/pvieira22$ tar -xvf data6.tar  
data8.bin  
bandit12@bandit:/tmp/pvieira22$ file data8.bin  
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Dec 28 13:34:36 2017, max compression, from Unix  
bandit12@bandit:/tmp/pvieira22$ mv data8.bin data8.gz  
bandit12@bandit:/tmp/pvieira22$ gunzip data8.gz  
bandit12@bandit:/tmp/pvieira22$ file data8  
data8: ASCII text  
bandit12@bandit:/tmp/pvieira22$ cat data8  
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit13 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit13@bandit.labs.overthewire.org -p 2220  
  
bandit13@bandit:~$ ls  
sshkey.private  
bandit13@bandit:~$ cat sshkey.private  
-----BEGIN RSA PRIVATE KEY-----  
MIIEpAIBAAKCAQEAxkkOE83W2cOT7IWhFc9aPaaQmQDdgzuXCv+ppZHa++buSkN+  
gg0tcr7Fw8NLGa5+Uzec2rEg0WmeevB13AIoYp0MZyETq46t+jk9puNwZwIt9XgB  
ZufGtZEwWbFWw/vVLNwOXBe4UWStGRWzgPpEeSv5Tb1VjLZIBdGphTIK22Amz6Zb  
ThMsiMnyJafEwJ/T8PQO3myS91vUHEuoOMAzoUID4kN0MEZ3+XahyK0HJVq68KsV  
ObefXG1vvA3GAJ29kxJaqvRfgYnqZryWN7w3CHjNU4c/2Jkp+n8L0SnxaNA+WYA7  
jiPyTF0is8uzMlYQ4l1Lzh/8/MpvhCQF8r22dwIDAQABAoIBAQC6dWBjhyEOzjeA  
J3j/RWmap9M5zfJ/wb2bfidNpwbB8rsJ4sZIDZQ7XuIh4LfygoAQSS+bBw3RXvzE  
pvJt3SmU8hIDuLsCjL1VnBY5pY7Bju8g8aR/3FyjyNAqx/TLfzlLYfOu7i9Jet67  
xAh0tONG/u8FB5I3LAI2Vp6OviwvdWeC4nOxCthldpuPKNLA8rmMMVRTKQ+7T2VS  
nXmwYckKUcUgzoVSpiNZaS0zUDypdpy2+tRH3MQa5kqN1YKjvF8RC47woOYCktsD  
o3FFpGNFec9Taa3Msy+DfQQhHKZFKIL3bJDONtmrVvtYK40/yeU4aZ/HA2DQzwhe  
ol1AfiEhAoGBAOnVjosBkm7sblK+n4IEwPxs8sOmhPnTDUy5WGrpSCrXOmsVIBUf  
laL3ZGLx3xCIwtCnEucB9DvN2HZkupc/h6hTKUYLqXuyLD8njTrbRhLgbC9QrKrS  
M1F2fSTxVqPtZDlDMwjNR04xHA/fKh8bXXyTMqOHNJTHHNhbh3McdURjAoGBANkU  
1hqfnw7+aXncJ9bjysr1ZWbqOE5Nd8AFgfwaKuGTTVX2NsUQnCMWdOp+wFak40JH  
PKWkJNdBG+ex0H9JNQsTK3X5PBMAS8AfX0GrKeuwKWA6erytVTqjOfLYcdp5+z9s  
8DtVCxDuVsM+i4X8UqIGOlvGbtKEVokHPFXP1q/dAoGAcHg5YX7WEehCgCYTzpO+  
xysX8ScM2qS6xuZ3MqUWAxUWkh7NGZvhe0sGy9iOdANzwKw7mUUFViaCMR/t54W1  
GC83sOs3D7n5Mj8x3NdO8xFit7dT9a245TvaoYQ7KgmqpSg/ScKCw4c3eiLava+J  
3btnJeSIU+8ZXq9XjPRpKwUCgYA7z6LiOQKxNeXH3qHXcnHok855maUj5fJNpPbY  
iDkyZ8ySF8GlcFsky8Yw6fWCqfG3zDrohJ5l9JmEsBh7SadkwsZhvecQcS9t4vby  
9/8X4jS0P8ibfcKS4nBP+dT81kkkg5Z5MohXBORA7VWx+ACohcDEkprsQ+w32xeD  
qT1EvQKBgQDKm8ws2ByvSUVs9GjTilCajFqLJ0eVYzRPaY6f++Gv/UVfAPV4c+S0  
kAWpXbv5tbkkzbS0eaLPTKgLzavXtQoTtKwrjpolHKIHUz6Wu+n4abfAIRFubOdN  
/+aLoRQ0yBDRbdXMsZN/jvY44eM+xRLdRVyMmdPtP8belRi2E2aEzA==  
-----END RSA PRIVATE KEY-----  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit14 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
$ chmod 600 bandit/sshkey.private  
  
$ ssh -i bandit/sshkey.private bandit14@bandit.labs.overthewire.org -p 2220  
This is a OverTheWire game server. More information on [http://www.overthewire.org/wargames](http://www.overthewire.org/wargames)  
  
bandit14@bandit:~$ cat /etc/bandit\_pass/bandit14  
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
bandit14@bandit:~$ nc localhost 30000  
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e  
Correct!  
BfMYroe26WYalil77FoDi9qh59eK5xNr  
  
\*\*\*\*  
  
echo 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e \| nc localhost 30000  
  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit15 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
bandit14@bandit:~$ openssl s\_client -ign\_eof -connect localhost:30001  
CONNECTED\(00000003\)  
depth=0 CN = bandit  
verify error:num=18:self signed certificate  
verify return:1  
depth=0 CN = bandit  
verify return:1  
---  
Certificate chain  
 0 s:/CN=bandit  
 i:/CN=bandit  
---  
Server certificate  
-----BEGIN CERTIFICATE-----  
MIICsjCCAZqgAwIBAgIJAKZI1xYeoXFuMA0GCSqGSIb3DQEBCwUAMBExDzANBgNV  
BAMMBmJhbmRpdDAeFw0xNzEyMjgxMzIzNDBaFw0yNzEyMjYxMzIzNDBaMBExDzAN  
BgNVBAMMBmJhbmRpdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOcX  
ruVcnQUBeHJeNpSYayQExCJmcHzSCktnOnF/H4efWzxvLRWt5z4gYaKvTC9ixLrb  
K7a255GEaUbP/NVFpB/sn56uJc1ijz8u0hWQ3DwVe5ZrHUkNzAuvC2OeQgh2HanV  
5LwB1nmRZn90PG1puKxktMjXsGY7f9Yvx1/yVnZqu2Ev2uDA0RXij/T+hEqgDMI7  
y4ZFmuYD8z4b2kAUwj7RHh9LUKXKQlO+Pn8hchdR/4IK+Xc4+GFOin0XdQdUJaBD  
8quOUma424ejF5aB6QCSE82MmHlLBO2tzC9yKv8L8w+fUeQFECH1WfPC56GcAq3U  
IvgdjGrU/7EKN5XkONcCAwEAAaMNMAswCQYDVR0TBAIwADANBgkqhkiG9w0BAQsF  
AAOCAQEAnrOty7WAOpDGhuu0V8FqPoKNwFrqGuQCTeqhQ9LP0bFNhuH34pZ0JFsH  
L+Y/q4Um7+66mNJUFpMDykm51xLY2Y4oDNCzugy+fm5Q0EWKRwrq+hIM+5hs0RdC  
nARP+719ddmUiXF7r7IVP2gK+xqpa8+YcYnLuoXEtpKkrrQCCUiqabltU5yRMR77  
3wqB54txrB4IhwnXqpO23kTuRNrkG+JqDUkaVpvct+FAdT3PODMONP/oHII3SH9i  
ar/rI9k+4hjlg4NqOoduxX9M+iLJ0Zgj6HAg3EQVn4NHsgmuTgmknbhqTU3o4IwB  
XFnxdxVy0ImGYtvmnZDQCGivDok6jA==  
-----END CERTIFICATE-----  
subject=/CN=bandit  
issuer=/CN=bandit  
---  
No client certificate CA names sent  
---  
SSL handshake has read 1015 bytes and written 631 bytes  
---  
New, TLSv1/SSLv3, Cipher is AES128-SHA  
Server public key is 2048 bit  
Secure Renegotiation IS supported  
Compression: NONE  
Expansion: NONE  
No ALPN negotiated  
SSL-Session:  
 Protocol : TLSv1  
 Cipher : AES128-SHA  
 Session-ID: E4F96CC51433587A5E355AD88A62FAA914544706FC4895E38AD58AB5AA7B875F  
 Session-ID-ctx:  
 Master-Key: 19EA7664EEB1CEB8A2E81983F94D9FBDF4214E37FC67E8D84BA1DE5E3484AF87CC257CCDEF1115D33A9330E3A0D0D314  
 Key-Arg : None  
 PSK identity: None  
 PSK identity hint: None  
 SRP username: None  
 TLS session ticket lifetime hint: 7200 \(seconds\)  
 TLS session ticket:  
 0000 - 08 f0 15 a5 d6 6f a0 e8-06 d6 bb a4 0c 33 eb 04 .....o.......3..  
 0010 - 7e 9b f1 e6 ab 1e 11 ea-bb 23 79 10 14 8e 9a 72 ~........\#y....r  
 0020 - f0 67 a7 6e 6e 5b 4a dd-2b c9 e9 ae c1 71 ea 88 .g.nn\[J.+....q..  
 0030 - ff eb 0b 7b ae c7 4b e5-be 88 97 b2 b5 98 91 1b ...{..K.........  
 0040 - c7 99 c9 82 bd 4a af dd-cb 3b 60 cb 0d 45 89 2a .....J...;\`..E.\*  
 0050 - 71 5c 7d f0 64 51 c1 6f-4e a6 53 66 3e 59 3a df q\}.dQ.oN.Sf&gt;Y:.  
 0060 - a7 e0 74 57 14 4f 96 54-31 73 ce 4a 88 f7 f2 55 ..tW.O.T1s.J...U  
 0070 - 1b 54 94 a9 16 14 a2 7d-de 52 57 af 04 7a e0 96 .T.....}.RW..z..  
 0080 - ff f8 58 3b 6b 00 60 71-dd 27 c8 a2 55 a9 40 0c ..X;k.\`q.'..U.@.  
 0090 - d2 e2 15 b5 1d 08 68 44-56 e1 84 0b 4c f2 5e 08 ......hDV...L.^.  
  
 Start Time: 1524331244  
 Timeout : 300 \(sec\)  
 Verify return code: 18 \(self signed certificate\)  
---  
BfMYroe26WYalil77FoDi9qh59eK5xNr  
Correct!  
cluFn7wTiGryunymYOu4RcffSxQluehd  
  
closed  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit16 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
bandit14@bandit:~$ openssl s\_client -ign\_eof -connect localhost:31790  
CONNECTED\(00000003\)  
depth=0 CN = bandit  
verify error:num=18:self signed certificate  
verify return:1  
depth=0 CN = bandit  
verify return:1  
---  
Certificate chain  
 0 s:/CN=bandit  
 i:/CN=bandit  
---  
Server certificate  
-----BEGIN CERTIFICATE-----  
MIICsjCCAZqgAwIBAgIJAKZI1xYeoXFuMA0GCSqGSIb3DQEBCwUAMBExDzANBgNV  
BAMMBmJhbmRpdDAeFw0xNzEyMjgxMzIzNDBaFw0yNzEyMjYxMzIzNDBaMBExDzAN  
BgNVBAMMBmJhbmRpdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOcX  
ruVcnQUBeHJeNpSYayQExCJmcHzSCktnOnF/H4efWzxvLRWt5z4gYaKvTC9ixLrb  
K7a255GEaUbP/NVFpB/sn56uJc1ijz8u0hWQ3DwVe5ZrHUkNzAuvC2OeQgh2HanV  
5LwB1nmRZn90PG1puKxktMjXsGY7f9Yvx1/yVnZqu2Ev2uDA0RXij/T+hEqgDMI7  
y4ZFmuYD8z4b2kAUwj7RHh9LUKXKQlO+Pn8hchdR/4IK+Xc4+GFOin0XdQdUJaBD  
8quOUma424ejF5aB6QCSE82MmHlLBO2tzC9yKv8L8w+fUeQFECH1WfPC56GcAq3U  
IvgdjGrU/7EKN5XkONcCAwEAAaMNMAswCQYDVR0TBAIwADANBgkqhkiG9w0BAQsF  
AAOCAQEAnrOty7WAOpDGhuu0V8FqPoKNwFrqGuQCTeqhQ9LP0bFNhuH34pZ0JFsH  
L+Y/q4Um7+66mNJUFpMDykm51xLY2Y4oDNCzugy+fm5Q0EWKRwrq+hIM+5hs0RdC  
nARP+719ddmUiXF7r7IVP2gK+xqpa8+YcYnLuoXEtpKkrrQCCUiqabltU5yRMR77  
3wqB54txrB4IhwnXqpO23kTuRNrkG+JqDUkaVpvct+FAdT3PODMONP/oHII3SH9i  
ar/rI9k+4hjlg4NqOoduxX9M+iLJ0Zgj6HAg3EQVn4NHsgmuTgmknbhqTU3o4IwB  
XFnxdxVy0ImGYtvmnZDQCGivDok6jA==  
-----END CERTIFICATE-----  
subject=/CN=bandit  
issuer=/CN=bandit  
---  
No client certificate CA names sent  
---  
SSL handshake has read 1015 bytes and written 631 bytes  
---  
New, TLSv1/SSLv3, Cipher is AES128-SHA  
Server public key is 2048 bit  
Secure Renegotiation IS supported  
Compression: NONE  
Expansion: NONE  
No ALPN negotiated  
SSL-Session:  
 Protocol : TLSv1  
 Cipher : AES128-SHA  
 Session-ID: 44EBAAAAC9FBBB404BDAC1745A9478F4C8E4BDDC9DF35B943342590AB74D0AD6  
 Session-ID-ctx:  
 Master-Key: 948ACD02929150BF9C938B9D7432A69AABBBBD7F7F0527D08AD3F182177FEBB762EAA6B04291FD56710085000DB68DE9  
 Key-Arg : None  
 PSK identity: None  
 PSK identity hint: None  
 SRP username: None  
 TLS session ticket lifetime hint: 7200 \(seconds\)  
 TLS session ticket:  
 0000 - 9a b6 c1 e5 3e 9c 51 03-45 ba c9 c1 cc d7 23 80 ....&gt;.Q.E.....\#.  
 0010 - e3 e6 11 38 b9 9b e7 8d-db 4e 2a 1f 65 72 ab d7 ...8.....N\*.er..  
 0020 - 17 c3 a3 3b da e0 5d 9b-d7 a7 20 4f bb e6 19 e5 ...;..\]... O....  
 0030 - cf 16 4b 59 6f 3e dc ee-b6 07 26 09 2b d4 81 46 ..KYo&gt;....&.+..F  
 0040 - 65 17 a2 f1 32 dd ef 84-65 58 17 69 7e ce a1 a6 e...2...eX.i~...  
 0050 - 75 63 f2 14 5f 4d d4 6e-ba a2 6d 54 84 56 65 0a uc..\_M.n..mT.Ve.  
 0060 - a0 84 6d a6 62 29 f3 0e-42 91 07 e7 cc 44 14 90 ..m.b\)..B....D..  
 0070 - 01 b5 ea 3f cd b1 92 99-be 99 2e 0c e1 88 54 8a ...?..........T.  
 0080 - 43 4f 8c 5a c4 c7 52 a7-e3 5c ec 11 a5 eb 42 7e CO.Z..R..\....B~  
 0090 - a8 3f f1 ab 1b d6 13 77-f2 7e e6 31 cb b8 a3 81 .?.....w.~.1....  
  
 Start Time: 1524331439  
 Timeout : 300 \(sec\)  
 Verify return code: 18 \(self signed certificate\)  
---  
cluFn7wTiGryunymYOu4RcffSxQluehd  
Correct!  
-----BEGIN RSA PRIVATE KEY-----  
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ  
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ  
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu  
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW  
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX  
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD  
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl  
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd  
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC  
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A  
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama  
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT  
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx  
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd  
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt  
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A  
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi  
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg  
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu  
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni  
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU  
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM  
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b  
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3  
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=  
-----END RSA PRIVATE KEY-----  
  
closed  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit17 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
chmod 600 bandit/sshkey17.private  
  
ssh -i bandit/sshkey17.private bandit17@bandit.labs.overthewire.org -p 2220  
  
bandit17@bandit:~$ diff passwords.new passwords.old  
42c42  
&lt; kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd  
---  
&gt;  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit18 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/sh  
This is a OverTheWire game server. More information on [http://www.overthewire.org/wargames](http://www.overthewire.org/wargames)  
bandit18@bandit.labs.overthewire.org's password:  
ls  
readme  
cat readme  
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit19 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit19@bandit.labs.overthewire.org -p 2220  
  
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit\_pass/bandit20  
GbKksEFF4yrVs6il55v6gwY5aVje5f0j  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit20 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit20@bandit.labs.overthewire.org -p 2220  
  
Processo 1  
  
bandit20@bandit:~$ nc -l 16985 &lt; /etc/bandit\_pass/bandit20  
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr  
  
Processo 2  
  
bandit20@bandit:~$ ./suconnect 16985  
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j  
Password matches, sending next password  
  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit21 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit21@bandit.labs.overthewire.org -p 2220  
  
bandit21@bandit:/etc/cron.d$ cat cronjob\_bandit22  
@reboot bandit22 /usr/bin/cronjob\_bandit22.sh &&gt; /dev/null  
\* \* \* \* \* bandit22 /usr/bin/cronjob\_bandit22.sh &&gt; /dev/null  
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob\_bandit22.sh  
\#!/bin/bash  
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv  
cat /etc/bandit\_pass/bandit22 &gt; /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv  
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv  
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit22 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit22@bandit.labs.overthewire.org -p 2220  
  
bandit22@bandit:/usr/bin$ cat /usr/bin/cronjob\_bandit23.sh  
\#!/bin/bash  
  
myname=$\(whoami\)  
mytarget=$\(echo I am user $myname \| md5sum \| cut -d ' ' -f 1\)  
  
echo "Copying passwordfile /etc/bandit\_pass/$myname to /tmp/$mytarget"  
  
cat /etc/bandit\_pass/$myname &gt; /tmp/$mytarget  
bandit22@bandit:/usr/bin$ echo I am user bandit23 \| md5sum \| cut -d ' ' -f 1  
8ca319486bfbbc3663ea0fbe81326349  
bandit22@bandit:/usr/bin$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349  
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit23 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit23@bandit.labs.overthewire.org -p 2220  
  
criar script /tmp/pvieira24/pv.sh  
  
\*\*\*\*\*\*\*  
\#!/bin/bash  
  
cat /etc/bandit\_pass/bandit24 &gt; /tmp/pvieira24/bandit24.pass  
\*\*\*\*  
  
bandit23@bandit:/tmp/pvieira24$ chmod +x pv.sh  
  
bandit23@bandit:/tmp/pvieira24$ chmod 777 .  
  
bandit23@bandit:/tmp/pvieira24$ cp pv.sh /var/spool/bandit24  
  
bandit23@bandit:/tmp/pvieira24$ ls  
bandit24.pass pv.sh  
bandit23@bandit:/tmp/pvieira24$ cat bandit24.pass  
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit24 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit24@bandit.labs.overthewire.org -p 2220  
  
\#\#\#\#\#\#\#  
  
\#!/bin/bash  
  
pass24=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ  
  
  
for a in {0..9}{0..9}{0..9}{0..9}  
do  
 echo "Attempting PIN: $a"  
  
 attempt="$\(echo $pass24 $a \| nc localhost 30002\)"  
  
 if ! \[\[ $attempt == \*"Wrong!"\* \]\]; then  
  
 echo -ne "$attempt"  
  
 break  
  
 fi  
done  
  
\#\#\#\#\#\#  
  
echo "" &gt; pins && for i in {0000..9999}; do echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i &gt;&gt; pins; done && cat pins \| nc localhost 30002  
  
  
\#\#\#\#\#\#  
  
Exiting.bandit24@bandit:/tmp/pvieira24$ nc localhost 30002  
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.  
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 5440  
Correct!  
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG  
  
Exiting.  
  
  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\# Bandit25 \#\#\#\#\#\#\#\#\#\#\#\#\#\#  
\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
  
ssh bandit25@bandit.labs.overthewire.org -p 2220  
  
  
  
  
  
  
  


