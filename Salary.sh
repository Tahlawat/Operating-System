#!/bin/bash
echo "Enter basic salary:"
read bsal

if [ $bsal -lt 1500 ]
then
  gsal=$((bsal + (bsal / 100) * 10 + (bsal / 100) * 90))
  echo "The gross salary: $gsal"
else
  gsal=$((bsal + 500 + (bsal / 100) * 98))
  echo "The gross salary: $gsal"
fi

