# John

## Shadow file

- `sudo /usr/sbin/unshadow /etc/passwd /etc/shadow > passwords.txt`
- `/usr/sbin/john --wordlist=/usr/share/wordlists/rockyou.txt passwords.txt`

- `/etc/shadow`
- `john --wordlist=/usr/share/wordlists/rockyou.txt shadow`

## ZIP

- `zip2john encrypted.zip > encrypted.hash`
- `john --wordlist=/usr/share/wordlists/rockyou.txt encrypted.hash`

### Fcrackzip

- <https://github.com/hyc/fcrackzip>
- `fcrackzip -u -D -p wordlist.txt file.zip` : bruteforces the given zip file with passwords from the given wordlist
- `fcrackzip -D -u -p /usr/share/wordlists/rockyou.txt fsociety.zip`
- `fcrackzip -v -l 4-4 -u BAND.zip`

## MsOffice

- `python office2john.py dummy.docx > hash.txt`
- `john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`

## GPG

- `gpg2john file.asc > hash`
- `john hash`

## Cracking everything with John the Ripper

- [Cracking with John the Ripper](https://bytesoverbombs.io/cracking-everything-with-john-the-ripper-d434f0f6dc1c)

## Other john tools

- dmg2john
- gpg2john
- hccap2john
- keepass2john
- keychain2john
- keyring2john
- keystore2john
- kwallet2john
- luks2john
- pfx2john
- putty2john
- pwsafe2john
- racf2john
- rar2john
- ssh2john
- truecrypt_volume2john
- uaf2john
- wpapcap2john
- zip2john
