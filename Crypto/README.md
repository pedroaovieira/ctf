# Crypto

- [Transform](#Transform)
  - [Text to Binary](Text-to-Binary)
  - [Hexadecimal to Text](Hexadecimal-to-Text)
  - [Replace](#Replace)
  - [Reverse](#Reverse)
  - [Case transform](#Case-transform)
  - [Numeral system](#Numeral-system)
  - [Bitwise operation](#Bitwise-operation)
- [Alphabets](#Alphabets)
  - [Morse Code](#Morse-Code)
  - [Spelling alphabet](#Spelling-alphabet)
- [Ciphers](#Ciphers)
  - [Enigma machine](#Enigma-machine)
  - [Caesar cipher](#Caesar-cipher)
  - [Affine cipher](#Affine-cipher)
  - [ROT13](#ROT13)
  - [A1Z26](#A1Z26)
  - [Viginère cipher](#Viginère-cipher)
  - [Bacon cipher](#Bacon-cipher)
  - [Alphabetical substitution](#Alphabetical-substitution)
  - [Rail fence cipher](#Rail-fence-cipher)
- [Polybius square ciphers](#Polybius-square-ciphers)
  - [Polybius square](#Polybius-square)
  - [ADFGX cipher](#ADFGX-cipher)
  - [Bifid cipher](#Bifid-cipher)
  - [Nihilist cipher](#Nihilist-cipher)
  - [Tap code](#Tap-code)
  - [Trifid cipher](#Trifid-cipher)
- [Encoding](#Encoding)
  - [Base32](#Base32)
  - [Base64](#Base64)
  - [Ascii85](#Ascii85)
  - [Baudot code](#Baudot-code)
  - [Unicode code points](#Unicode-code-points)
  - [URL encoding](#URL-encoding)
  - [Punycode](#Punycode)
  - [Bootstring](#Bootstring)
  - [Integer](#Integer)
- [Modern cryptography](#Modern-cryptography)
  - [Block Cipher](#Block-Cipher)
  - [RC4](#RC4)
  - [Hash function](#Hash-function)
  - [HMAC](#HMAC)
- [Others](#Others)
  - [Brainfuck](#Brainfuck)
  - [RSA](#RSA)
  - [Substitution](#Substitution)
  - [Snow](#Snow)
  - [QR Code](#QR-Code)
  - [Fernet](#Fernet)
  - [SMS](#SMS)
  - [Atbash](#Atbash)
  - [Tone Detect](#Tone-Detect)
- [Sites](#Sites)
  - [The CrypTool Portal](https://www.cryptool.org/en/cto/)
  - [cryptii](https://cryptii.com/)
  - [dcode](https://www.dcode.fr/tools-list)
  - [asecuritysite](https://asecuritysite.com/)
  - [CyberChef](https://gchq.github.io/CyberChef/)
  - [Find Cypher](https://medium.com/hacking-info-sec/como-descubrir-el-tipo-de-cifrado-de-un-texto-encriptado-78d3a6f0bc2f)
  - [crypto-101](https://pequalsnp-team.github.io/cheatsheet/crypto-101)

---

## Transform

### Text to Binary

[cryptii - Text to Bytes](https://cryptii.com/pipes/text-to-binary)

### Hexadecimal to Text

[cryptii - Hexadecimal to Text](https://cryptii.com/pipes/hex-to-text)

### Replace

[cryptii - Replace](https://cryptii.com/)

### Reverse

[cryptii - Reverse](https://cryptii.com/)

### Case transform

[cryptii - Case transform](https://cryptii.com/)

### Numeral system

[cryptii - Numeral system](https://cryptii.com/)

### Bitwise operation

[cryptii - Bitwise operation](https://cryptii.com/)

## Alphabets

### Morse Code

[cryptii - Morse Code](https://cryptii.com/)

### Spelling alphabet

[cryptii - Spelling alphabet](https://cryptii.com/)

## Ciphers

### Enigma machine

[cryptii - Enigma machine](https://cryptii.com/)

### Caesar cipher

[cryptii - Caesar cipher](https://cryptii.com/)

`cat file.txt | tr '[a-z]' '[n-za-m]' | tr '[A-Z]' '[N-ZA-M]'`

`echo 'hello world' | tr '[a-z]' '[n-za-m]' | tr '[A-Z]' '[N-ZA-M]'`

### Affine cipher

[cryptii - Affine cipher](https://cryptii.com/)

### ROT13

[cryptii - ROT13](https://cryptii.com/)

`alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"`

`echo 'hello world' | rot13`

### A1Z26

[cryptii - A1Z26](https://cryptii.com/)

### Viginère cipher

[cryptii - Viginère cipher](https://cryptii.com/)

[dcode - Viginère cipher](https://www.dcode.fr/vigenere-cipher)

[guballa - Viginère cipher](https://www.guballa.de/vigenere-solver)

### Bacon cipher

[cryptii - Bacon cipher](https://cryptii.com/)

[dcode - Bacon cipher](https://www.dcode.fr/bacon-cipher)

### Alphabetical substitution

[cryptii - Alphabetical substitution](https://cryptii.com/)

### Rail fence cipher

[cryptii - Rail fence cipher](https://cryptii.com/)

## Polybius square ciphers

### Polybius square

[cryptii - Polybius square](https://cryptii.com/)

### ADFGX cipher

[cryptii - ADFGX cipher](https://cryptii.com/)

### Bifid cipher

[cryptii - Bifid cipher](https://cryptii.com/)

### Nihilist cipher

[cryptii - Nihilist cipher](https://cryptii.com/)

### Tap code

[cryptii - Tap code](https://cryptii.com/)

### Trifid cipher

[cryptii - Trifid cipher](https://cryptii.com/)

## Encoding

### Base32

[cryptii - Base32](https://cryptii.com/)

### Base64

`echo text | base64 -d`

[cryptii - Base64](https://cryptii.com/)

### Ascii85

[cryptii - Ascii85](https://cryptii.com/)

### Baudot code

[cryptii - Baudot code](https://cryptii.com/)

### Unicode code points

[cryptii - Unicode code points](https://cryptii.com/)

### URL encoding

[cryptii - URL encoding](https://cryptii.com/)

### Punycode

[cryptii - Punycode](https://cryptii.com/)

### Bootstring

[cryptii - Bootstring](https://cryptii.com/)

### Integer

[cryptii - Integer](https://cryptii.com/)

## Modern cryptography

### Block Cipher

[cryptii - Block Cipher](https://cryptii.com/)

### RC4

[cryptii - RC4](https://cryptii.com/)

### Hash function

[cryptii - Hash function](https://cryptii.com/)

### HMAC

[cryptii - HMAC](https://cryptii.com/)

## Others

### Brainfuck

[Brainfuck](https://sange.fi/esoteric/brainfuck/impl/interp/i.html)

### RSA

[RSA](https://github.com/Ganapati/RsaCtfTool)

### Substitution

[guballa- Substitution](https://www.guballa.de/substitution-solver)

[guballa git - Substitution](https://gitlab.com/guballa/SubstitutionBreaker)

### Snow

### QR Code

[4qrcode - QR code](https://4qrcode.com/scan-qr-code.php)

### Fernet

[Fernet](https://asecuritysite.com/encryption/ferdecode)

### SMS

[dcode - SMS](https://www.dcode.fr/code-multitap-abc)

### Atbash

[dcode - Atbash](https://www.dcode.fr/atbash-cipher)

### Tone Detect

[Tone Detect](http://dialabc.com/sound/detect/)

### Prime Number

[dcode- Prime Number](https://www.dcode.fr/prime-numbers-cipher)

### Malbolge

[Malbolge](https://www.tutorialspoint.com/execute_malbolge_online.php)