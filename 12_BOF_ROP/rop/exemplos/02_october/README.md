# October Buffer Overflow Script

## Countermeasures

- NX Enabled
- ASLR Enabled

## Additional Info

- [libc version](https://libc.blukat.me/?q=__libc_system%3A0003ada0%2Csvcerr_systemerr%3A00112f20%2Cexit%3A0002e9d0)
- Linux frolic 4.4.0-116-generic #140-Ubuntu SMP Mon Feb 12 21:22:43 UTC 2018 i686 athlon i686 GNU/Linux


## Example

`while true; do ./ovrflw $(./exploit); done`



