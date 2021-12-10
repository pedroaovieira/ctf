
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