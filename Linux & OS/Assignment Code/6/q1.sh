#!/bin/bash

echo "Enter First Name:"
read fname

echo "Enter Last Name:"
read lname

fullname="$fname $lname"

echo "Full Name: $fullname"
echo "Length of Full Name: ${#fullname}"
echo "First Character: ${fname:0:1}"
echo "Last Character: ${lname: -1}"
