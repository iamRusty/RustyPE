"""
===============================================================
Trial Program for PE 14

Goal: Find the starting number, under one million, that
      produces the longest Collatz Sequence

Note: To optimize the script, make a list of the first computed 
      numbers. If a larger sequence falls on a number 
      in the list, then just add its number of terms.
===============================================================
"""

_CEILING = 1000000

def howManyTerms(curNum):
    count = 1
    while (curNum != 1):
        if (curNum % 2):
            curNum = int( 1.5 * curNum + 0.5 )
            count += 1
        else:
            curNum //= 2
        count += 1
    return count                   
    
def main():
    print("Trial Program for PE 14")
    count = 1
    mostTerms = 1
    contender = 1
    while (count < _CEILING):
        curTerms = howManyTerms(count)
        if (curTerms > mostTerms):
            mostTerms = curTerms
            contender = count
        count += 1
        
    print(contender, mostTerms)
            
main()
