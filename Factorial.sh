#!/bin/bash

echo "Enter any number:"
read num
fact=1
for (( i=1; num > 1; num-- ))
do
  fact=$((fact * num))
done
echo "Factorial is $fact"

