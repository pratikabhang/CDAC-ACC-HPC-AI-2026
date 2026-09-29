#!/bin/bash

read -p "Enter Filename: " file

wc -l < "$file"
