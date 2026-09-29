#!/bin/bash

for file in *.txt
do
    if [ -f "$file" ]
    then
        echo "File Name: $file"
        wc -c < "$file"
    fi
done
