#!/bin/bash
if [[ $# -ne 1 ]]
then
echo "Usage: ./brostart.sh <MACHINE>"
echo "Starts Bro on the given machine (specified by IP address or hostname)"
exit
fi

MACHINE=$1

# Change the network interface here if necessary:
# e.g. in my setting it is enp0s8 when using Vagrant VMs and enp0s25 without Vagrant
INTERFACE="enp0s8"

# Note: To enable automatic SSH login execute on the source machine:
# ssh-keygen -t rsa -b 4096 (Enter, Enter, Enter)
# ssh-copy-id $MACHINE

# Note: To enable sudo w/o password execute on the target machine:
# sudo visudo
# And add the following line at the end (without #):
# %sudo ALL=(ALL:ALL) NOPASSWD:   /usr/local/bro/bin/bro * 

ssh ubuntu@$MACHINE "mkdir -p ~/brolog; cd ~/brolog; nohup sudo /usr/local/bro/bin/bro -i $INTERFACE > /dev/null 2> /dev/null < /dev/null &"

echo "WARNING:"
echo "Enabled Bro on $MACHINE at the network interface $INTERFACE."
echo "Please ensure this is the right interface, e.g. by running ifconfig"
echo "and change the file 'helpers/brostart.sh' accordingly."
sleep 5

