# Crypto

- [Crypto](#crypto)
  - [External Resource](#external-resource)
  - [Book](#book)
  - [Chalenges](#chalenges)
  - [Cryptogram solver](#cryptogram-solver)
  - [Cryptanalysis](#cryptanalysis)
  - [Transform](#transform)
    - [Text to Binary](#text-to-binary)
    - [Hexadecimal to Text](#hexadecimal-to-text)
    - [Replace](#replace)
    - [Reverse](#reverse)
    - [Case transform](#case-transform)
    - [Numeral system](#numeral-system)
    - [Bitwise operation](#bitwise-operation)
  - [Alphabets](#alphabets)
    - [Morse Code](#morse-code)
    - [Spelling alphabet](#spelling-alphabet)
  - [Ciphers](#ciphers)
    - [Enigma machine](#enigma-machine)
    - [Caesar cipher](#caesar-cipher)
    - [ROT13](#rot13)
    - [Affine cipher](#affine-cipher)
    - [A1Z26](#a1z26)
    - [Viginère cipher](#viginère-cipher)
    - [Bacon cipher](#bacon-cipher)
    - [Alphabetical substitution](#alphabetical-substitution)
    - [Rail fence cipher](#rail-fence-cipher)
  - [Polybius square ciphers](#polybius-square-ciphers)
    - [Polybius square](#polybius-square)
    - [ADFGX cipher](#adfgx-cipher)
    - [Bifid cipher](#bifid-cipher)
    - [Nihilist cipher](#nihilist-cipher)
    - [Tap code](#tap-code)
    - [Trifid cipher](#trifid-cipher)
  - [Encoding](#encoding)
    - [Base32](#base32)
    - [Base64](#base64)
    - [Ascii85](#ascii85)
    - [Baudot code](#baudot-code)
    - [Unicode code points](#unicode-code-points)
    - [URL encoding](#url-encoding)
    - [Punycode](#punycode)
    - [Bootstring](#bootstring)
    - [Integer](#integer)
  - [Modern cryptography](#modern-cryptography)
    - [Block Cipher](#block-cipher)
    - [RC4](#rc4)
    - [Hash function](#hash-function)
    - [HMAC](#hmac)
  - [Others](#others)
    - [Brainfuck](#brainfuck)
    - [RSA](#rsa)
      - [RsaCtfTool](#rsactftool)
      - [RSA Calculator](#rsa-calculator)
      - [rsa-encryption-decryption](#rsa-encryption-decryption)
      - [rsatool](#rsatool)
    - [Substitution](#substitution)
    - [Snow](#snow)
    - [QR Code](#qr-code)
    - [Barcode Reader](#barcode-reader)
    - [Fernet](#fernet)
    - [SMS](#sms)
    - [Atbash](#atbash)
    - [Tone Detect](#tone-detect)
    - [Prime Number](#prime-number)
    - [Malbolge](#malbolge)
    - [XOR](#xor)
  - [Tools](#tools)
    - [Wordlists](#wordlists)
    - [John](#john)
    - [Hashcat](#hashcat)
    - [Hashes](#hashes)
    - [GPG](#gpg)

---

## External Resource

- <https://cryptii.com/>
- <https://www.dcode.fr/>
- <https://www.guballa.de/>
- <https://asecuritysite.com/>
- <https://gchq.github.io/CyberChef/>
- <https://www.cryptool.org/en/>
- <http://rumkin.com/tools/cipher/>
- <https://project-awesome.org/apsdehal/awesome-ctf>

---

## Book

---

## Chalenges

- <https://cryptohack.org/>

---

## Cryptogram solver

- <https://quipqiup.com/>

## Cryptanalysis

- <https://github.com/nccgroup/featherduster>

---

## Transform

### Text to Binary

- [cryptii - Text to Bytes](https://cryptii.com/pipes/text-to-binary)

### Hexadecimal to Text

- [cryptii - Hexadecimal to Text](https://cryptii.com/pipes/hex-to-text)

### Replace

- [cryptii - Replace](https://cryptii.com/)

### Reverse

- [cryptii - Reverse](https://cryptii.com/)

### Case transform

- [cryptii - Case transform](https://cryptii.com/)

### Numeral system

- [cryptii - Numeral system](https://cryptii.com/)

### Bitwise operation

- [cryptii - Bitwise operation](https://cryptii.com/)

---

## Alphabets

### Morse Code

- [cryptii - Morse Code](https://cryptii.com/)
- [Text tools - morse code](http://www.unit-conversion.info/texttools/morse-code/)

### Spelling alphabet

- [cryptii - Spelling alphabet](https://cryptii.com/)

---

## Ciphers

### Enigma machine

- [cryptii - Enigma machine](https://cryptii.com/)

### Caesar cipher

- [cryptii - Caesar cipher](https://cryptii.com/)
- `cat file.txt | tr '[a-z]' '[n-za-m]' | tr '[A-Z]' '[N-ZA-M]'`
- `echo 'hello world' | tr '[a-z]' '[n-za-m]' | tr '[A-Z]' '[N-ZA-M]'`

### ROT13

- [cryptii - ROT13](https://cryptii.com/)

- `alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"`

- `echo 'hello world' | rot13`

### Affine cipher

- [cryptii - Affine cipher](https://cryptii.com/)

### A1Z26

- [cryptii - A1Z26](https://cryptii.com/)

### Viginère cipher

- [cryptii - Viginère cipher](https://cryptii.com/)
- [dcode - Viginère cipher](https://www.dcode.fr/vigenere-cipher)
- [guballa - Viginère cipher](https://www.guballa.de/vigenere-solver)

### Bacon cipher

- [cryptii - Bacon cipher](https://cryptii.com/)
- [dcode - Bacon cipher](https://www.dcode.fr/bacon-cipher)

### Alphabetical substitution

- [cryptii - Alphabetical substitution](https://cryptii.com/)

### Rail fence cipher

- [cryptii - Rail fence cipher](https://cryptii.com/)

---

## Polybius square ciphers

### Polybius square

- [cryptii - Polybius square](https://cryptii.com/)

### ADFGX cipher

- [cryptii - ADFGX cipher](https://cryptii.com/)

### Bifid cipher

- [cryptii - Bifid cipher](https://cryptii.com/)

### Nihilist cipher

- [cryptii - Nihilist cipher](https://cryptii.com/)

### Tap code

- [cryptii - Tap code](https://cryptii.com/)

### Trifid cipher

- [cryptii - Trifid cipher](https://cryptii.com/)

---

## Encoding

### Base32

- [cryptii - Base32](https://cryptii.com/)

### Base64

- `echo text | base64 -d`
- [base64decode](https://www.base64decode.org/)
- [cryptii - Base64](https://cryptii.com/)

### Ascii85

- [cryptii - Ascii85](https://cryptii.com/)

### Baudot code

- [cryptii - Baudot code](https://cryptii.com/)

### Unicode code points

- [cryptii - Unicode code points](https://cryptii.com/)

### URL encoding

- [cryptii - URL encoding](https://cryptii.com/)
- [URL decoder](https://www.urldecoder.org/)

### Punycode

- [cryptii - Punycode](https://cryptii.com/)

### Bootstring

- [cryptii - Bootstring](https://cryptii.com/)

### Integer

- [cryptii - Integer](https://cryptii.com/)

---

## Modern cryptography

### Block Cipher

- [cryptii - Block Cipher](https://cryptii.com/)

### RC4

- [cryptii - RC4](https://cryptii.com/)

### Hash function

- [cryptii - Hash function](https://cryptii.com/)

### HMAC

- [cryptii - HMAC](https://cryptii.com/)

---

## Others

### Brainfuck

- [Brainfuck](https://sange.fi/esoteric/brainfuck/impl/interp/i.html)

### RSA

- [RSA post](https://muirlandoracle.co.uk/2020/01/29/rsa-encryption/)
- [Decode](https://crypto.stackexchange.com/questions/19444/rsa-given-q-p-and-e/19530#19530)

#### RsaCtfTool

- [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

#### RSA Calculator

- [RSA Calculator](https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html)

#### rsa-encryption-decryption

- [rsa-encryption-decryption](https://www.devglan.com/online-tools/rsa-encryption-decryption)

#### rsatool

- [rsatool](https://github.com/ius/rsatool)

### Substitution

- [guballa- Substitution](https://www.guballa.de/substitution-solver)

- [guballa git - Substitution](https://gitlab.com/guballa/SubstitutionBreaker)

### Snow

- stegsnow - <http://www.darkside.com.au/snow/>
  - `stegsnow -C -p "password" -m "secret message" infile.txt outfile.txt`
  - `snow -C -p "magic" readme2.txt`

### QR Code

- [4qrcode - QR code](https://4qrcode.com/scan-qr-code.php)

### Barcode Reader

- [Barcode Reader] - https://online-barcode-reader.inliteresearch.com/

### Fernet

- [Fernet](https://asecuritysite.com/encryption/ferdecode)

### SMS

- [dcode - SMS](https://www.dcode.fr/code-multitap-abc)

### Atbash

- [dcode - Atbash](https://www.dcode.fr/atbash-cipher)

### Tone Detect

- [Tone Detect](http://dialabc.com/sound/detect/)

### Prime Number

- [dcode- Prime Number](https://www.dcode.fr/prime-numbers-cipher)

### Malbolge

- [Malbolge](https://www.tutorialspoint.com/execute_malbolge_online.php)

### XOR

- [Solve Crypto Force](https://scwf.dima.ninja/)

```python
>>> data = 'CAPTURETHEFLAG'
>>> key = 'A'
>>> encrypted = ''.join([chr(ord(x) ^ ord(key)) for x in data])
>>> encrypted
'\x02\x00\x11\x15\x14\x13\x04\x15\t\x04\x07\r\x00\x06'
>>> decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])
>>> decrypted
'CAPTURETHEFLAG'
```

---

## Tools

---

### Wordlists

[Wordlists](wordlists.md)

---

### John

[John The Ripper](john.md)

---

### Hashcat

[Hashcat](hashcat.md)

---

### Hashes

[Hashes](hashes.md)

---

### GPG

[GnuPGP](gpg.md)

---
