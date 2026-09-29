#!/bin/bash

echo "Enter File Name:"
read file

if [ -e "$file" ]
then
    echo "File Size:"
    wc -c < "$file"

    echo "Number of Lines:"
    wc -l < "$file"

    echo "Number of Words:"
    wc -w < "$file"

    if [ -r "$file" ]
    then
        echo "Readable"
    fi

    if [ -w "$file" ]
    then
        echo "Writable"
    fi
else
    echo "File Not Found"
fi
