# Find

- type
    - **d** to find directories
    - **f** to find files


    - find / -type f -name "*.xml" 2> /dev/null
    - find /home -type f -iname user.txt 2> /dev/null
    - find / -type d -name "*exploits*" 2> /dev/null


- user
    - find / -type f -user kittycat 2> /dev/null
- size
    - find / -type f -size 150c 2> /dev/null
- perm



[THM Find](https://tryhackme.com/room/thefindcommand)


