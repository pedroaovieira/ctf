# Reverse Engineering

- [Reverse Engineering](#reverse-engineering)
  - [External Resource](#external-resource)
  - [Book](#book)
  - [VMs](#vms)
  - [x86](#x86)
    - [Registers (32 bits)](#registers-32-bits)
    - [Pointers (32 bits)](#pointers-32-bits)
  - [64 bits](#64-bits)
    - [Registers (64 bits)](#registers-64-bits)
    - [Pointers (64 bits)](#pointers-64-bits)
  - [Assembly](#assembly)
  - [Reversing Tools](#reversing-tools)
    - [Tools](#tools)
      - [file type/extension](#file-typeextension)
      - [strings](#strings)
      - [binwalk](#binwalk)
    - [Debugers](#debugers)
      - [OllyDBG](#ollydbg)
      - [ImmunityDebugger](#immunitydebugger)
      - [Mona](#mona)
      - [WinnDbg](#winndbg)
      - [GDB](#gdb)
    - [Disassemblers](#disassemblers)
      - [IDA](#ida)
      - [GHIDRA](#ghidra)
    - [Decompilers](#decompilers)
      - [Hex-Rays](#hex-rays)
      - [.Net Reflector](#net-reflector)
      - [VB Decompiler](#vb-decompiler)
    - [Hex Editors](#hex-editors)
      - [Hex Workshop](#hex-workshop)
      - [WinHex](#winhex)
    - [Memory Dumpers / PE Editors](#memory-dumpers--pe-editors)
      - [Explorer Suite](#explorer-suite)
    - [Monitoring Tools](#monitoring-tools)
      - [Process Heap Viewer](#process-heap-viewer)
      - [Process Explorer](#process-explorer)
    - [dnSpy](#dnspy)
  - [Online Disassembler](#online-disassembler)
  - [PEiD](#peid)
  - [UPX](#upx)
  - [SNDBOX](#sndbox)
- [Chapter 8 - Reverse Engineering](#chapter-8---reverse-engineering)

---

## External Resource

<https://forum.tuts4you.com/files/categories/>

---

## Book

- [Practical Malware Analysis] - <https://www.amazon.com/Practical-Malware-Analysis-Hands-Dissecting/dp/1593272901>
- [0xOPOSEC-CrackMe-Up] - [link](0xOPOSEC-CrackMe-Up-0xACB.pdf)

---

## VMs

- [flare-vm] - <https://www.mandiant.com/resources/flare-vm-update> - <https://github.com/mandiant/flare-vm>
- [commando vm] - <https://github.com/mandiant/commando-vm>

---

## x86

### Registers (32 bits)

- EAX - Accumulator Register
- EBX - Base Register
- ECX - Counter Register
- EDX - Data Register
- ESI - Source Index
- EDI - Destination Index

### Pointers (32 bits)

- ESP - Stack Pointer
- EBP - Base Pointer
- **EIP** - Index Pointer

---

## 64 bits

### Registers (64 bits)

- RAX - Accumulator Register
- RBX - Base Register
- RCX - Counter Register
- RDX - Data Register
- RSI - Source Index
- RDI - Destination Index

### Pointers (64 bits)

- RSP - Stack Pointer
- RBP - Base Pointer

---

## Assembly

- Memory address - e.g. [exa], [00487054]
- Constant - e.g. 0x123456789
- Move - `mov \<source>,\<dest>`  - copies data
- Repeat - `rep/repe/repne/repz/repnz` - relies on ECX Register
- Push Stack - `push \<val>`
- Pop Stack - `pop \<val>`
- Load Effective Address - `lea \<reg32>,\<mem>`
- Integer Addition - `add \<val1>,\<val2>`
- Increment/Decrement - `inc \<val>` or `dec \<val>`
- Integer Multiplication - `imul \<val1>,\<val2>`
- Integer Division - `idix \<val>`
- Bitwise Logical And, Or Exclusve Or - `and \<val1>,\<val2>` or `or \<val1>,\<val2>` or `xor \<val1>,\<val2>`
- Bitwise Logical Not - `not \<val>`
- Negate - `neg \<val>`
- Shift Left, Sift Right - `shl \<val>,\<shift>` or `shr \<val>,\<shift>`
- Compare - `cmp \<val1>,\<val2>`
- Test - `test \<val1>,\<val2>`
- Jump - `jmp \<label>`
- Conditional Jump - `j condition \<label>`
- Call - `call \<label>`
- Return - `ret`

---

## Reversing Tools

### Tools

#### file type/extension

- Identify File Type
  - `file file`
- can also check the magic bytes
  - <https://en.wikipedia.org/wiki/List_of_file_signatures>

#### strings

- `strings -n 15 file`

#### binwalk

- Show
  - `binwalk file`
- Extract
  - `binwalk -e file`

---

### Debugers

#### OllyDBG

#### ImmunityDebugger

> ##### Shortcuts

```
Breakpoint: F2
Step: F7
Exec till Return: Ctrl+F9
Run: F9
Pause: F12
```

#### Mona

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

---

#### WinnDbg

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

---

#### GDB

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

---

### Disassemblers

#### IDA

#### GHIDRA


---

### Decompilers

#### Hex-Rays

#### .Net Reflector

#### VB Decompiler


---

### Hex Editors

#### Hex Workshop

http://www.hexworkshop.com/

#### WinHex

http://www.winhex.com/winhex/hex-editor.html

---

### Memory Dumpers / PE Editors

#### Explorer Suite

- <https://ntcore.com/?page_id=388>

---

### Monitoring Tools

#### Process Heap Viewer

- [Process Heap Viewer] - <https://securityxploded.com/ProcHeapViewer.php>
- [HeapMemView] - <https://www.nirsoft.net/utils/heap_memory_view.html>

#### Process Explorer

- [Process Hacker]  <https://processhacker.sourceforge.io/>
- [Process Explorer] - <https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer>
- [Process Monitor] - <https://docs.microsoft.com/en-us/sysinternals/downloads/procmon>

---









---

### dnSpy

https://github.com/0xd4d/dnSpy


## Online Disassembler
https://onlinedisassembler.com/odaweb/



## PEiD


## UPX
The Ultimate Packer for eXecutables
https://github.com/upx/upx








## SNDBOX





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

