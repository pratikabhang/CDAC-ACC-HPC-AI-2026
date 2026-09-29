#!/bin/bash

read -p "Enter Filename: " file
read -p "Enter Search Word: " word

grep "$word" "$file"
