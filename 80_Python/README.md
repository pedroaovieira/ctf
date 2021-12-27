# Python

- [Python](#python)
  - [Shebang](#shebang)
  - [Lists []](#lists-)
  - [Tuples - Do not change ()](#tuples---do-not-change-)
  - [Functions](#functions)
  - [Loops](#loops)
  - [Modules](#modules)
  - [Strings](#strings)
  - [Dictionary - key/value {}](#dictionary---keyvalue-)
  - [Sockets](#sockets)

## Shebang

`#!/bin/python3`

## Lists []

```python
movies = ["filme 1","filme 2","filme 3"]
print(movies[0])
```

## Tuples - Do not change ()

```python
grades ("a","b","c","d","f")
print(grades[0])
```

## Functions

```python
def func():
    print("hello")
```

## Loops

```python
roman = ["I","II","III","IV","V"]
for n in roman:
    print(n)
```

## Modules

```python
#!/bin/python3

import sys
import os

print(sys.version)
```

## Strings

```python
#!/bin/python3

sentence = "This is a sentence."
print(senetence[0])
print(senetence[-1])
print(senetence[:4])

# split
# join
# strip
# lower

movie = "The Hangover"
print("My favorite movie is {}".format(movie))
```

## Dictionary - key/value {}

```python
romans = {"I": 1, "II": 2, "III": 3, "IV": 4, "V"; 5}
romans["VI"] = 6

print(romans.get("IV"))
```

## Sockets

```python
#!/bin/python3

import sys
import socket

Host = '127.0.0.1'

try:
    for port in range(20,81)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((Host,port))
        if result == 0:
            print("Port {} is open.".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()

```
