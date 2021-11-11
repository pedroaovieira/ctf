# Bash

## Example

```
#!/bin/bash
echo "Hello World"
```

## Variables
```
name="Jammy"
echo $name
Jammy
```

## Parameters
```
#!/bin/bash
echo "Enter your name"
read name
echo "Your name is $name"
```

Number of arguments passed: $#
First argument $1

## Arrays

var[index_position]
```
transport=('car' 'train' 'bike' 'bus')
echo "${transport[1]}"
train
```

---------------------------

[devhints bash](https://devhints.io/bash)


[THM Bash](https://tryhackme.com/room/bashscripting)
