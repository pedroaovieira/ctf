#!/bin/sh

ip_address=$1
maquina=$2

mkdir nmap

ports=$(nmap -p- --min-rate=1000 -T4 $ip_address | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)

nmap -p$ports -sC -sV -Pn $ip_address -oA nmap/$maquina

