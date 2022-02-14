#!/bin/python3

import string
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def check_palindrome_1(string):
    reversed_string = string[::-1]
    status=1
    if(string!=reversed_string):
        status=0
    return status

def getAllOccurrences(s: string, allAlphs: string):
    if len(s) == 1:
        return 0
    countOfLetters = [0] * 26
    for i in range(len(s)):
        indexOfAlpha = allAlphs.index(s[i])
        stringCount = s.count(s[i])
        countOfLetters[indexOfAlpha] = stringCount

    palindrome = check_palindrome_1(s)
    
    if palindrome:
        return 0
    
    return countOfLetters
        
def alternate(s):
    # Write your code here
    allLowerAlphs = string.ascii_lowercase
    allCharOccurrences = getAllOccurrences(s, allLowerAlphs)
    if allCharOccurrences == 0:
        return 0
    
    s = s.replace(allLowerAlphs[allCharOccurrences.index(max(allCharOccurrences))], "")
    if len(s) == 0:
        return 0
    
    s = s.replace(allLowerAlphs[allCharOccurrences.index(min(allCharOccurrences))], "")
    if len(s) == 0:
        return 0
    result = 0
    lenOfString = len(s)
    twoLetters = []
    j = 0
    for i in range(len(allLowerAlphs)):
        count = 0
        j = 0
        while j < lenOfString:
            if allCharOccurrences[i] == 0:
                break
            if s[j] == allLowerAlphs[i]:
                count = count + 1
                if count > 1 and s[j - 1] == s[j]:
                    twoLetters = list(filter((s[j]).__ne__, twoLetters))
                    s = s.replace(s[j], "")
                    lenOfString = len(s)
                    
                elif len(twoLetters) < 2 and s[j] not in twoLetters:
                    twoLetters.append(s[j])
                    
                if s[j] not in twoLetters:
                    s = s.replace(s[j], "")
                    lenOfString = len(s)
            j = j + 1

    result = len(s)

    return result           

print(alternate('ucwtvajqreigbqszaukfieswtlhdvwhvlzsxswzbfcropnxlektloohamginpsxeooqsnlbaglmhiyednqibglmodhylweshcquhvxtqclqbvmptqglungavqccwlmhhogdlrzufeccpdmwnnrmgcxqlwdvtqqbicqbfgldxgdkkyvpzvlsncotyhwqeilzmguhpyrazsbsfvkzjzabcvrqwqndoqgztxtlpbfjcvbsplvbwlmmuyyqhiknybizxjzmrjvrtrsshgbiidrrcbapdwsxzlzlmcwrtvngokdvywjglorficgxqvatsbnvplqinopcrttpseweeekbypkvdanbcofvziojhpzhzaltgqvpstrrxfrjhdsdhrtwqzcqneicivppiquubsrvvbrtmwyhhqailyaaypfeusuefgqmbxmfadxtznfxfdtqggxeorjpvtmixlykezahzhxjbovglxggwxfcyrfxpefzolryernhmebhvcidocnknucdldlqtfvcoecygvejdrjnfrfrbqagcbellxnodvlzieerarmzrzfrdgxuhcfuwxvjlqmlflciotcylyyeywgtqgmbwghxaqesjgisuarjhqldcvxgyqzkwpecbapxxhevazufbgkrrzgxcnuuqdzzizbethncfhuvfjgccikzkqnksexzdvbhabdbrdspuygmhvmlbsptzejjtqnbdjpnhzamqvwliukpxxvkspgqxkedqcaaqwhglfiteiqnweyyfwswrkitadrayaqpllnnfatktsdlwtggzvjpefjglqbvpkpgtwarolbmsfbqxjsznmlmdohxwuxlasppsmqfcmfggxvimymnyqqoxdljdcyqlleuhfbemkwyysykdnjcazwrjhqpsclzhezqzghsmuzrapkxccniagkzfkntzrufvgqhbkfgyajwczsihigazrwvkdzequtqabdqqixjqudvdkvydknuamcxr'))