#!/bin/sh

data=$(date +'%Y_%m_%d')

cp /etc/hosts /etc/hosts_${data}

echo $1'\t'$2 >> /etc/hosts

