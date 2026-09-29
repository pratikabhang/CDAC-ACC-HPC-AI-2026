#!/bin/bash

echo "Enter Word:"
read word

len=${#word}

for ((i=0; i<len; i++))
do
    echo "${word:i:1}"
done

echo "Total Characters: $len"
