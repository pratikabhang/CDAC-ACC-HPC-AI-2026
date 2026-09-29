#!/bin/bash

i=50

while [ $i -ge 1 ]
do
    echo $i

    if [ $i -eq 25 ]
    then
        break
    fi

    i=$((i-1))
done
