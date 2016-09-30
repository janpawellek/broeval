#!/bin/bash
if [[ $# -ne 1 ]]
then
echo "Usage: ./brostart.sh <MACHINE>"
echo "Starts Bro on the given machine (specified by IP address or hostname)"
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

ssh ubuntu@$MACHINE 'cd ~/brolog; nohup sudo /usr/local/bro/bin/bro -i enp0s25 > /dev/null 2> /dev/null < /dev/null &'
sleep 5

