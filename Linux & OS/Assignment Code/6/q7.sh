#!/bin/bash

i=1

until [ $i -gt 15 ]
do
    echo "$i -> $((i*i))"
    i=$((i+1))
done
