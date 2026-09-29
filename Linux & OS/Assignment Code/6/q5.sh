#!/bin/bash

echo "Enter Sentence:"
read sentence

echo "Enter Word:"
read word

if echo "$sentence" | grep -q "$word"
then
    echo "Found"
else
    echo "Not Found"
fi
