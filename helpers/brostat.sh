#!/bin/bash
if [[ $# -ne 1 ]]
then
echo "Usage: ./brostat.sh <MACHINE>"
echo "Collects statistics on Bro on the given machine (specified by IP address or hostname)"
exit
fi

MACHINE=$1

# Note: To enable automatic SSH login execute on the source machine:
# ssh-keygen -t rsa -b 4096 (Enter, Enter, Enter)
# ssh-copy-id $MACHINE

# Note: To enable sudo w/o password execute on the target machine:
# sudo visudo
# And add the following line at the end (without #):
# %sudo ALL=(ALL:ALL) NOPASSWD:   /usr/local/bro/bin/bro * 

while :
do
ssh ubuntu@$MACHINE 'pidstat -ruh -C "^bro$" 1 1 | tail -n 1 | tr -s " " | cut -d " " -f 8,13'
done

