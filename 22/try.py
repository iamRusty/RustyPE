"""
===============================================================
Trial Program for PE 22     

Goal: Find the total score of the list.
        Formula: Score = WORD Score * position

Note: Uses FILE IO
===============================================================
"""
import string
_FILE_NAME_ = "p022_names.txt"
    
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

def valueOfWord(x):
    value = 0
    for character in x:
        value += ord(character) - 64     
    return value

def main():
    words = extractWord(_FILE_NAME_)
    words.sort()
    count = 1
    score = 0
    
    for x in words:
        current_score = valueOfWord(x)
        score += current_score * count
        count +=  1
    print score
            
main()
