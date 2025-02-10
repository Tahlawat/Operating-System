#!/bin/bash

echo "Enter three Integers:"
read a b c

if [ $a -gt $b ] && [ $a -gt $c ]; then
    echo "$a is Greatest"
elif [ $b -gt $a ] && [ $b -gt $c ]; then
    echo "$b is Greatest"
else
    echo "$c is Greatest"
fi

