# Hashcat

## Hash Examples

- <https://hashcat.net/wiki/doku.php?id=example_hashes>

### WEB Hash type identifier

- [hash_type_checker](https://md5hashing.net/hash_type_checker)
- [hash_identifier](https://hashes.com/en/tools/hash_identifier)
- [hash-analyzer](https://www.tunnelsup.com/hash-analyzer/)

## bcrypt $2*$, Blowfish (Unix)

- `hashcat -m 3200 5_1.txt /opt/rockyou/rockyou.txt --force`

## SHA2-256

- `hashcat -m 1400 5_2.txt /opt/rockyou/rockyou.txt --force`
