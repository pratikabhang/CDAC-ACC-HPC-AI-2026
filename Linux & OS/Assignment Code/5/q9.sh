#!/bin/bash

echo "Current Date: $(date)" > systeminfo.txt
echo "Current Working Directory: $(pwd)" >> systeminfo.txt
echo "Logged-in Username: $USER" >> systeminfo.txt

echo "Contents of systeminfo.txt"

cat systeminfo.txt
