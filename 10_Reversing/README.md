# Reversing




## file

## binwalk

## strings


## dnSpy

https://github.com/0xd4d/dnSpy


## Online Disassembler
https://onlinedisassembler.com/odaweb/

## OllyDBG

## Ghidra

## IDA


## PEiD


## UPX
The Ultimate Packer for eXecutables
https://github.com/upx/upx


## GDB

> ##### Commands

```
disas - disassemble
b - breakpoint
c - continue
r - run
p - TODO
st - step
x - examine
```

> ##### Examples

```
gdb> disas main
gdb> b 0xd34dc0d3
gdb> x/200x $esp
```

## WinDBG

> ##### Commands

```
g - pass exception
gN - step
bp [address] - breakpoint
bl - list breakpoints
!exchain - view exception chain
.load pykd.pyd - load python
!py mona [command] [args] - exceute mona stuff
a -> [jmp address]
u [address] - inspect
u - view stack
t - step
```

> ##### Examples

```
!py mona findmsp
!py mona seh
```

> ##### Shortcuts

```
Open Executable: CTRL+E
Attach to process: F6
Memory: Alt+5
Close Window: Ctrl+F4
Restart: Ctrl+Shift+F5
Break: Ctrl+Break
```

## ImmunityDebugger

> ##### Shortcuts

```
Breakpoint: F2
Step: F7
Exec till Return: Ctrl+F9
Run: F9
Pause: F12
```

## Mona

> ##### Arguments

```
pc [size] - generate cyclic pattern
po [address] - find offset
findmsp - find register overwritten with pattern
bytearray -b [badchars] - generate bytes from 0x00 to 0xff excluding badchars
jmp -r [register] - find a jump point
-n - skip modules that start with 0x00
-o - skip os modules
-m - module
-cm - module property
-cpd - filter bad chars
```

> ##### Examples

```
!mona config -set workingfolder path
!mona pc 2400
!mona po d34db33f
!mona findmsp
!mona find -s "\xff\xe4" -m comctl32.dll
!mona jmp -r esp
!mona seh -cm aslr=false
!mona seh -cpb "\x00\x0a\x0d"
```



# Chapter 8 - Reverse Engineering

> Reverse engineering is taking apart an object to see how it works in order to duplicate or enhance the object. The practice, taken from older industries, is now frequently used on computer hardware and software. Software reverse engineering involves reversing a program's machine code back into the source code that it was written in, using program language statements.
>
> _**— Anonymous**_

Reverse Engineering is hard and I'm bad at it, looking for contributions to this section. Please DM me on [Twitter](https://twitter.com/dostoevskylabs)

[Reverse Engineering - WikiPedia](https://en.wikipedia.org/wiki/Reverse_engineering#Reverse_engineering_of_software)

[Intro to Reverse Engineering - YouTube](https://www.youtube.com/playlist?list=PLUFkSN0XLZ-nXcDG89jS9iqKBnNHmz7Qw)

[Intro to Reverse Engineering - Course Files](http://opensecuritytraining.info/IntroductionToReverseEngineering.html)

[Intro to x86 Assembly - YouTube](https://www.youtube.com/playlist?list=PL038BE01D3BAEFDB0)

[Intro to x86 Assembly - Course Files](http://opensecuritytraining.info/IntroX86.html)

[Awesome Reversing](https://github.com/fdivrp/awesome-reversing)

[Reverse Engineering 101 - Malware Unicorn](https://securedorg.github.io/RE101/)

[What Can Reverse Engineering Do For You? - Malware Unicorn](https://www.slideshare.net/AmandaRousseau1/what-can-reverse-engineering-do-for-you)

[Lenas Reversing for Newbies](https://tuts4you.com/download.php?list.17)

[PoC\|\|GTFO 0x16](https://archive.org/stream/pocorgtfo16)

