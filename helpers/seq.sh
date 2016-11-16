#!/bin/bash
if [[ $# -ne 4 ]]
then
echo "Usage: ./seq.sh <SOURCE> <TARGET> <ITER> <SIZE>"
echo "Times a sequential transfer of data."
exit
fi

SOURCE=$1
TARGET=$2
ITER=$3
SIZE=$4 

ssh ubuntu@$SOURCE "/usr/bin/time -f \"%e\" bash -c \"for i in {1..$ITER}; do curl -s http://$TARGET/$SIZE.txt > /dev/null; done\""

