#!/bin/bash

echo "Enter Size(N)"
read N

echo "Enter Numbers"
read -a numbers  # Read all numbers in an array

sum=0

# Loop through array elements
for num in "${numbers[@]}"; do
    sum=$((sum + num))
done

# Calculate average using awk instead of bc
avg=$(awk "BEGIN {print $sum / $N}")

echo "Average: $avg"

