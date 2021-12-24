# Stego

- [Stego](#stego)
  - [External Resource](#external-resource)
  - [Book](#book)
  - [Chalenges](#chalenges)
  - [Google: “filetype ctf tools”s](#google-filetype-ctf-toolss)
  - [Magic Bytes - Filetype signatures](#magic-bytes---filetype-signatures)
  - [Tools](#tools)
    - [Online](#online)
    - [File type/extension](#file-typeextension)
    - [Hexeditor](#hexeditor)
    - [Strings](#strings)
    - [Binwalk](#binwalk)
    - [xxd](#xxd)
    - [Foremost](#foremost)
    - [Exiftool](#exiftool)
    - [Exiv2](#exiv2)
    - [Steghide](#steghide)
    - [Steghide with dictionary](#steghide-with-dictionary)
    - [Steghide Brute Force Tool](#steghide-brute-force-tool)
    - [Stegsolve](#stegsolve)
    - [Zsteg](#zsteg)
    - [StegCracker](#stegcracker)
    - [Stegseek](#stegseek)
    - [Wavsteg](#wavsteg)
    - [Sonic visualizer](#sonic-visualizer)
  - [Snow](#snow)
    - [QR Code](#qr-code)
    - [Barcode Reader](#barcode-reader)
    - [SMS](#sms)
    - [Tone Detect](#tone-detect)
    - [Cyrilic](#cyrilic)
    - [Broken Unicode](#broken-unicode)
    - [Braille](#braille)
    - [Piet](#piet)
    - [unicode](#unicode)
    - [Fcrackzip](#fcrackzip)

---

## External Resource

- <https://0xrick.github.io/lists/stego/>
- <https://github.com/DominicBreuker/stego-toolkit>
- <https://project-awesome.org/apsdehal/awesome-ctf>
- <https://pequalsnp-team.github.io/cheatsheet/steganography-101>

---

## Book

---

## Chalenges

- <https://www.hackthebox.eu/>
- <https://www.root-me.org/>
- <https://ringzer0ctf.com/challenges>

---

## Google: “filetype ctf tools”s

---

## Magic Bytes - Filetype signatures

- <https://en.wikipedia.org/wiki/List_of_file_signatures>

---

## Tools

### Online

- https://www.dcode.fr/>
- <https://gchq.github.io/CyberChef/>

---

### File type/extension

- `file file` : identifies the filetype

---

### Hexeditor

- A hex editor is a type of program that allows a user to view and edit the raw and exact contents of files.
- Bless

---

### Strings

- `strings file` : displays printable strings in the given file.
- `strings -n 15 file` : Display strings with minimum lenght of 15 chars

---

### Binwalk

- <https://github.com/ReFirmLabs/binwalk>
- `binwalk file` : Displays the embedded data in the given file  
- `binwalk -e file` : Displays and extracts the data from the given file

---

### xxd

- is a Linux command that creates a hex dump of a given file or standard input. It can also convert a hex dump back to its original binary form.

---

### Foremost

Foremost is a program that recovers files based on their headers.

- <https://github.com/korczis/foremost>
- `foremost -i file` : extracts data from the given file.

---

### Exiftool

- <https://www.sno.phy.queensu.ca/~phil/exiftool/>
- `exiftool file` : shows the metadata of the given file

---

### Exiv2

- <https://github.com/Exiv2/exiv2>
- `exiv2 file` : shows the metadata of the given file

---

### Steghide

- <https://github.com/StefanoDeVuono/steghide>
- `steghide info file` : displays info about a file whether it has embedded data or not.  
- `steghide extract -sf file` : extracts embedded data from a file
- `steghide extract -sf file -p password`

### Steghide with dictionary

- <https://raw.githubusercontent.com/felipesi/steghide-crack/master/steghide-crack.sh>

---

### Steghide Brute Force Tool

- <https://github.com/Va5c0/Steghide-Brute-Force-Tool.git>

---

### Stegsolve

- <https://github.com/eugenekolo/sec-tools/tree/master/stego/stegsolve/stegsolve>
- <https://github.com/zardus/ctf-tools/tree/master/stegsolve>

---

### Zsteg

- <https://github.com/zed-0xff/zsteg>
- `zsteg -a file` : Runs all the methods on the given file  
- `zsteg -E file` : Extracts data from the given payload \(example : zsteg -E b4,bgr,msb,xy name.png\)

---

### StegCracker

- <https://github.com/Paradoxis/StegCracker>

---

### Stegseek

- <https://github.com/RickdeJager/stegseek>
- `stegseek cute-alien.jpg /usr/share/wordlists/rockyou.txt`

---

### Wavsteg

- <https://github.com/ragibson/Steganography#WavSteg>
- `python3 WavSteg.py -r -s soundfile -o outputfile` : extracts data from a wav sound file and outputs the data into a new file

---

### Sonic visualizer

- <https://www.sonicvisualiser.org/>

---

## Snow

- stegsnow - <http://www.darkside.com.au/snow/>
  - `stegsnow -C -p "password" -m "secret message" infile.txt outfile.txt`
  - `snow -C -p "magic" readme2.txt`

---

### QR Code

- [4qrcode - QR code](https://4qrcode.com/scan-qr-code.php)
- [webqr] - <https://webqr.com/>

---

### Barcode Reader

- [Barcode Reader] - https://online-barcode-reader.inliteresearch.com/

---

### SMS

- [dcode - SMS](https://www.dcode.fr/code-multitap-abc)

---

### Tone Detect

- [Tone Detect](http://dialabc.com/sound/detect/)

---

### Cyrilic

- <https://2cyr.com/decode/>

---

### Broken Unicode

- <https://ftfy.now.sh/>

---

### Braille

- <https://www.branah.com/braille-translator>

---

### Piet

- <https://www.bertnase.de/npiet/npiet-execute.php>
- <http://www.dangermouse.net/esoteric/piet.html>

---

### unicode

- <https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder>

---

### Fcrackzip

- <https://github.com/hyc/fcrackzip>
- `fcrackzip -u -D -p wordlist.txt file.zip` : bruteforces the given zip file with passwords from the given wordlist
- `fcrackzip -D -u -p /usr/share/wordlists/rockyou.txt fsociety.zip`
- `fcrackzip -v -l 4-4 -u BAND.zip`
