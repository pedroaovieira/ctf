# Crypto

- [Transform](#Transform)
    - [Replace](#Replace)
    - [Reverse](#Reverse)
    - [Case transform](#Case-transform)
    - [Numeral-System]
    * [Bitwise-Operation]

 * [Alphabets]


 * [Ciphers]


 * [Polybius square ciphers]

 * [Encoding]


 * [Modern cryptography]







 * [Caesar](#Caesar)
 * [Hex](#Hex)
 * [Base64](#Base64)
 Enigma
 Viginere
 Bacon
 Substitution
 Brainfuck
 RSA






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

