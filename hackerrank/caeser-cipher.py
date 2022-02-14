#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def reduceIndex(index, lengthOfAlpha):
    newIndex = index
    while newIndex >= lengthOfAlpha:
        newIndex = newIndex - lengthOfAlpha
        if newIndex == lengthOfAlpha:
            return 0
    return newIndex
    

def caesarCipher(s, k):
    # Write your code here
    word = s
    wordLen = len(word)
    alphabetsLow = "abcdefghijklmnopqrstuvwxyz"
    alphabetsUpp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = ""
    for i in range(wordLen):
        index = 0
        if word[i].isupper() and alphabetsUpp.find(word[i]) != -1:
            index = alphabetsUpp.find(word[i]) + k
            if index >= len(alphabetsUpp):
                index = reduceIndex(index, len(alphabetsUpp))
        
            newLetter = alphabetsUpp[index]
            result = result + newLetter
        elif word[i].islower() and alphabetsLow.find(word[i]) != -1:
            index = alphabetsLow.find(word[i]) + k
            if index >= len(alphabetsLow):
                index = reduceIndex(index, len(alphabetsLow))
                
            newLetter = alphabetsLow[index]
            result = result + newLetter
        elif True:
            result = result + word[i]
    return result

print(caesarCipher("Hello_World!", 4))
