#!/bin/bash

echo "Enter the value of n"
read n

a=0
b=1
count=2

echo "Fibonacci series:"
echo $a
echo $b

while [ $count -lt $n ]  # Fix: Using -lt instead of -le to print exactly 'n' terms
do
    fib=$((a + b))  # Fix: Using $((...)) instead of expr
    a=$b
    b=$fib
    echo $fib
    ((count++))  # Fix: Simplified increment
done

