#!/bin/bash
if [[ $# -ne 1 ]]
then
echo "Usage: ./brokill.sh <MACHINE>"
echo "Kills Bro on the given machine (specified by IP address or hostname)"
exit
fi

MACHINE=$1

# Note: To enable automatic SSH login execute on the source machine:
# ssh-keygen -t rsa -b 4096 (Enter, Enter, Enter)
# ssh-copy-id $MACHINE

# Note: To enable sudo w/o password execute on the target machine:
# sudo visudo
# And add the following line at the end (without #):
# %sudo ALL=(ALL:ALL) NOPASSWD:   /usr/bin/killall /usr/local/bro/bin/bro

ssh ubuntu@$MACHINE 'sudo /usr/bin/killall /usr/local/bro/bin/bro'

