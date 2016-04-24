"""
======================================================================================
Trial Program for PE 42

Goal: Find the number of triangle words in data.pe

Note: Uses FILE IO. Check PE 22
        From Project Euler's Solution Discussion Page 
            Knowing that the inverse function of n(n+1)/2 is (Sqrt(1+8n)-1)/2, 
            one has only to check if the word-number comes from an integer 
            index using the reverse triangle formula.
            For SKY (55) the index will be (Sqrt(1+8*55)-1)/2 = 10.0, 
            which is integer, so 55 must be a triangle number.
======================================================================================
"""

import string
_FILE_NAME_ = "data.pe"

def extractWord(filename):
    f = open(filename, "r")
    data_list = f.readlines()
    data_string = str(data_list)
    words = []
    for x in data_string.split('","'):
        words.append(x)
    words[0] = words[0].split("[\'\"")[1]
    words[len(words)-1] = words[len(words)-1].split("\"\']")[0]
    return words

def valueOfWord(words):
    value_words = []
    value = 0
    for x in words:
        for character in x:
            value += ord(character) - 64
        value_words.append(value)
        value = 0
    return value_words
    
def triangleNumberGenerator(max_value):
    triangleNumbers = []
    n = 1
    currentNumber = 1
    while (currentNumber < max_value):
        currentNumber = int(n*(n+1)/2)
        triangleNumbers.append(currentNumber)
        n += 1 
    return triangleNumbers    
    
def triangleWordCounter(value_words, triangleNumbers):
    count = 0
    for number in value_words:
        if number in triangleNumbers:
            count += 1
    return count
    
def main():
    words = extractWord(_FILE_NAME_)
    value_words = valueOfWord(words)
    triangleNumbers = triangleNumberGenerator(max(value_words))
    triangleCount = triangleWordCounter(value_words, triangleNumbers)
    print(triangleCount)       
     
main()