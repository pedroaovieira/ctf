# Wireless

- [Wireless](#wireless)
  - [Wireless Lab Setup](#wireless-lab-setup)
    - [wireless adapter](#wireless-adapter)
    - [Access point](#access-point)
    - [Configuring your wireless card](#configuring-your-wireless-card)
    - [monitor mode interface](#monitor-mode-interface)
  - [Wireshark](#wireshark)
    - [Management frames](#management-frames)
    - [Control frames](#control-frames)
    - [Data frames](#data-frames)
  - [Sniffing data packets](#sniffing-data-packets)
  - [Packet injection](#packet-injection)
  - [Uncovering hidden SSIDs](#uncovering-hidden-ssids)
  - [Beating MAC filters](#beating-mac-filters)
  - [bypassing Shared Authentication](#bypassing-shared-authentication)

## Wireless Lab Setup

### wireless adapter

### Access point

> TP-LINK TL-WR841N Wireless router

- `route –n`

### Configuring your wireless card

- `iwconfig`

- `ifconfig wlan0`
  
- `iwlist wlan0 scanning` - scan available networks
- `iwconfig wlan0 essid "Wireless Lab"` - connect to "Wireless Lab network"

- `iwconfig wlan0` - to check the status.

- `ifconfig wlan0 192.168.0.2 netmask 255.255.255.0 up`
- `ifconfig wlan0`

- `arp –a`

- `iw reg set US` - set regulatory domain to US
- `iwconfig wlan1 txpower 27` - set transmitting power to 27 dBm

### monitor mode interface

- `dmesg` or `tail -f -n @ /var/log/messages` 

- `iwconfig`
- `ifconfig wlan1 up`

- `ifconfig wlan1`

- `airmon-ng` - show available wireles cards

- `airmon-ng start wlan1` - starts wlan1 in monitor mode

## Wireshark

### Management frames

- filter `wlan.fc.type == 0`

### Control frames

- filter `wlan.fc.type == 1`

### Data frames

- filter `wlan.fc.type == 2`

## Sniffing data packets

- find router channel 
  - `airodump-ng --bssid <mac> wlan1`

- lock card on same channel as router 
  - `iwconfig wlan1 channel <channel>`

- `iwconfig wlan1`

- wireshark filter `wlan.bssid == <mac>`

## Packet injection

- wireshark filter to monitor all non-Beacon packets
  - `(wlan.bssid == <mac>) && !(wlan.fc.type_subtype == 0x08)`

- `aireplay-ng -9 -e "Wireless Lab" -a <mac> wlan1`

- wireshark check packets

## Uncovering hidden SSIDs

- passive technique - waiting for a legitimate client to connect the access point

- send deauthentication packets
  - `aireplay-ng -0 5 -a <mac> --ignore-negative wlan1`

- wireshark filter to catch deauth packets
  - `wlan.fc.type_subtype == 0x0C`

- wireshark filter to monitor all non-Beacon packets
  - `(wlan.bssid == <mac>) && !(wlan.fc.type_subtype == 0x08)`

## Beating MAC filters

airodumpng -c 11 -a --bssid <mac> mon0

ifconfig wlan0 down
macchanger –m <mac> wlan0
ifconfig wlan0 up

## bypassing Shared Authentication

pagina 48

