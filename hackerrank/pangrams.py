import string
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    allAlphs = string.ascii_lowercase
    new_s = s.replace(" ", "").lower()
    lenOfString = len(new_s)
    
    if lenOfString == 0:
        return "not pangram"    
    allLettersInString = list(new_s)
    allLettersInString.sort()
    newAllLettersInString = list(dict.fromkeys(allLettersInString))
    if len(newAllLettersInString) != len(allAlphs):
        return "not pangram"
    else: 
        return "pangram"

print(pangrams("We promptly judged antique ivory buckles for the next prize"))