#!/bin/bash
if [[ $# -ne 4 ]]
then
echo "Usage: ./par.sh <SOURCE> <TARGET> <ITER> <SIZE>"
echo "Times a parallel transfer of data."
exit
fi

SOURCE=$1
TARGET=$2
ITER=$3
SIZE=$4 

ssh ubuntu@$SOURCE "/usr/bin/time -f \"%e\" bash -c \"seq $ITER | parallel -j0 -N250 --pipe parallel -j0 curl -s http://$TARGET/$SIZE.txt > /dev/null\""

