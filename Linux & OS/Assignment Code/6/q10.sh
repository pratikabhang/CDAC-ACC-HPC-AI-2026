#!/bin/bash

while true
do
    echo "Enter Directory Name:"
    read dir

    if [ -d "$dir" ]
    then
        echo "Directory Already Exists"
    else
        mkdir "$dir"
        echo "Directory Created Successfully"
        break
    fi
done
