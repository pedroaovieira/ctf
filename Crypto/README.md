# Crypto

- [Transform](#Transform)
  - [Replace](#Replace)
  - [Reverse](#Reverse)
  - [Case transform](#Case-transform)
  - [Numeral system](#Numeral-system)
  - [Bitwise operation](#Bitwise-operation)
- [Alphabets](#Alphabets)
  - [Morse Code](#Morse-Code)
  - [Spelling alphabet]](#Spelling-alphabet)
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

---

## Transform

### Replace

### Reverse

### Case transform

### Numeral system

### Bitwise operation

## Alphabets

### Morse Code

### Spelling alphabet

## Ciphers

### Enigma machine

### Caesar cipher

### Affine cipher

### ROT13

### A1Z26

### Viginère cipher

### Bacon cipher

### Alphabetical substitution

### Rail fence cipher

## Polybius square ciphers

### Polybius square

### ADFGX cipher

### Bifid cipher

### Nihilist cipher

### Tap code

### Trifid cipher

## Encoding

### Base32

### Base64

### Ascii85

### Baudot code

### Unicode code points

### URL encoding

### Punycode

### Bootstring

### Integer

## Modern cryptography

### Block Cipher

### RC4

### Hash function

### HMAC

## Others

### Brainfuck

### RSA

### Substitution

### Snow

### QR Code



---

## Caesar - ROT13

`alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"`

`echo 'fooman@example.com' | rot13`


```
cat file.txt | tr '[a-z]' '[n-za-m]' | tr '[A-Z]' '[N-ZA-M]'
```

```
echo 'hello world' | tr '[a-z]' '[n-za-m]' | tr '[A-Z]' '[N-ZA-M]'
```

## Hex

[Hex Decoder](https://cryptii.com/pipes/hex-decoder)


## Base64

```
echo text | base64 -d
```

## Enigma

