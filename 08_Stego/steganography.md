# Resources

{% embed url="https://0xrick.github.io/lists/stego/" %}

### Steghide <a id="Steghide"></a>

Steghide is a steganography program that hides data in various kinds of image and audio files , only supports these file formats : `JPEG, BMP, WAV and AU`. but it’s also useful for extracting embedded and encrypted data from other files.  
It can be installed with `apt` however the [source](https://github.com/StefanoDeVuono/steghide) can be found on github.

Useful commands:  
`steghide info file` : displays info about a file whether it has embedded data or not.  
`steghide extract -sf file` : extracts embedded data from a file

### Foremost <a id="Foremost"></a>

Foremost is a program that recovers files based on their headers , footers and internal data structures , I find it useful when dealing with png images.  
It can be installed with `apt` however the [source](https://github.com/korczis/foremost) can be found on github.

Useful commands:  
`foremost -i file` : extracts data from the given file.

### Stegsolve <a id="Stegsolve"></a>

Sometimes there is a message or a text hidden in the image itself and in order to view it you need to apply some color filters or play with the color levels. You can do it with GIMP or Photoshop or any other image editing software but stegsolve made it easier. it’s a small java tool that applies many color filters on images. Personally i find it very useful  
You can get it from [github](https://github.com/eugenekolo/sec-tools/tree/master/stego/stegsolve/stegsolve)

### Strings <a id="Strings"></a>

Strings is a linux tool that displays printable strings in a file. That simple tool can be very helpful when solving stego challenges. Usually the embedded data is password protected or encrypted and sometimes the password is actaully in the file itself and can be easily viewed by using strings  
It’s a default linux tool so you don’t need to install anything.

Useful commands:  
`strings file` : displays printable strings in the given file.

### Exiftool <a id="Exiftool"></a>

Sometimes important stuff is hidden in the metadata of the image or the file , exiftool can be very helpful to view the metadata of the files.  
You can get it from [here](https://www.sno.phy.queensu.ca/~phil/exiftool/)

Useful commands:  
`exiftool file` : shows the metadata of the given file

### Exiv2 <a id="Exiv2"></a>

A tool similar to exiftool.  
It can be installed with `apt` however the [source](https://github.com/Exiv2/exiv2) can be found on github.  
[Official website](http://www.exiv2.org/)

Useful commands:  
`exiv2 file` : shows the metadata of the given file

### Binwalk <a id="Binwalk"></a>

Binwalk is a tool for searching binary files like images and audio files for embedded files and data.  
It can be installed with `apt` however the [source](https://github.com/ReFirmLabs/binwalk) can be found on github.

Useful commands:  
`binwalk file` : Displays the embedded data in the given file  
`binwalk -e file` : Displays and extracts the data from the given file

### Zsteg <a id="Zsteg"></a>

zsteg is a tool that can detect hidden data in png and bmp files.  
to install it : `gem install zsteg` , The source can be found on [github](https://github.com/zed-0xff/zsteg)

Useful commands:  
`zsteg -a file` : Runs all the methods on the given file  
`zsteg -E file` : Extracts data from the given payload \(example : zsteg -E b4,bgr,msb,xy name.png\)

### Wavsteg <a id="Wavsteg"></a>

WavSteg is a python3 tool that can hide data and files in wav files and can also extract data from wav files.  
You can get it from [github](https://github.com/ragibson/Steganography#WavSteg)

Useful commands:  
`python3 WavSteg.py -r -s soundfile -o outputfile` : extracts data from a wav sound file and outputs the data into a new file

### Sonic visualizer <a id="Sonic-visualizer"></a>

Sonic visualizer is a tool for viewing and analyzing the contents of audio files, however it can be helpful when dealing with audio steganography. You can reveal hidden shapes in audio files.  
[Offical Website](https://www.sonicvisualiser.org/)

### File

The file command determines the file type of a file. It reports the file type in human readable format \(e.g. ‘ASCII text’\) or MIME type \(e.g. ‘text/plain; charset=us-ascii’\). As filenames in UNIX can be entirely independent of file type file can be a useful command to determine how to view or work with a file.

### xxd

is a Linux command that creates a hex dump of a given file or standard input. It can also convert a hex dump back to its original binary form. Like uuencode\(1\) and uudecode\(1\) it allows the transmission of binary data in a “mail-safe” ASCII representation, but has the advantage of decoding to standard output.

### Hexeditor

A hex editor, also called a binary file editor or byteeditor, is a type of program that allows a user to view and edit the raw and exact contents of files, that is, at the byte level

### Web Tools <a id="Web-Tools"></a>

### [Unicode Text Steganography](https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder) <a id="Unicode-Text-Steganography"></a>

A web tool for unicode steganography , it can encode and decode text.

### [npiet online](https://www.bertnase.de/npiet/npiet-execute.php) <a id="npiet-online"></a>

an online interpreter for piet. piet is an esoteric language , programs in piet are images. read more about piet [here](http://www.dangermouse.net/esoteric/piet.html)

### [dcode.fr](https://www.dcode.fr/) <a id="dcode-fr"></a>

Sometimes when solving steganography challenges you will need to decode some text. dcode.fr has many decoders for a lot of ciphers and can be really helpful.

### Bruteforcers <a id="Bruteforcers"></a>

### [StegCracker](https://github.com/Paradoxis/StegCracker) <a id="StegCracker"></a>

A tool that bruteforces passwords using steghide

### Fcrackzip <a id="Fcrackzip"></a>

Sometimes the extracted data is a password protected zip , this tool bruteforces zip archives.  
It can be installed with `apt` however the [source](https://github.com/hyc/fcrackzip) can be found on github.

Useful commands:  
`fcrackzip -u -D -p wordlist.txt file.zip` : bruteforces the given zip file with passwords from the given wordlist

{% embed url="https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder" %}






## file type/extension

- `file`

## strings

- `strings -n 15 file`

## binwalk

- `binwalk file`
- `binwalk -e file`

## exiftool

## pngcheck

## hex editor

## magic bytes

## Google: “filetype ctf tools”s

## steghide
```
steghide extract -sf file
steghide extract -sf file -p password
```

## steghide with dictionary
{% embed url="https://raw.githubusercontent.com/felipesi/steghide-crack/master/steghide-crack.sh" %}

## stegseek
stegseek cute-alien.jpg /usr/share/wordlists/rockyou.txt

## stegsolve
{% embed url="https://github.com/zardus/ctf-tools/tree/master/stegsolve" %}

## QR Code
{% embed url="https://webqr.com/" %}

## Fcrack
```
fcrackzip -v -l 4-4 -u BAND.zip

fcrackzip -D -u -p /usr/share/wordlists/rockyou.txt fsociety.zip

fcrackzip -u -v -D -p users.txt username.zip
```

## Cyrilic
{% embed url="https://2cyr.com/decode/" %}

## Broken Unicode
{% embed url="https://ftfy.now.sh/" %}


## Braille
{% embed url="https://www.branah.com/braille-translator" %}




# Steghide Brute Force Tool
https://github.com/Va5c0/Steghide-Brute-Force-Tool.git