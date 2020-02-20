#!/bin/bash
import sys

alphabet = "ABCDEFGHIKLMNOPQRSTVXYZ"
output = ""

# temp
letter_amount = int(sys.argv[1])
word_amount = int(sys.argv[2])

for number in range(1, word_amount + 1, 1):
    output += letter_amount * alphabet[number - 1]
print(output)
