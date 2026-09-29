#!/bin/bash

echo "Enter Directory Name:"
read dir

if [ -d "$dir" ]
then
    echo "Directory Exists"

    echo "Total Files:"
    find "$dir" -maxdepth 1 -type f | wc -l

    echo "Total Directories:"
    find "$dir" -maxdepth 1 -type d | wc -l

else
    echo "Directory Not Found"
fi
