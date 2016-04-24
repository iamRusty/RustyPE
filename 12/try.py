"""
=============================================================
Trial Program for PE 12

Goal: Find the first triangle number to have over 
      five hundred factors

=============================================================
"""
import math

_FACTORS = 500

def numOfFactors(curNum):
    count = 1
    sqrt_curNum = int(math.sqrt(curNum)) + 1
    factors = 0
    while (count < sqrt_curNum):
        if (curNum % count == 0):
            factors += 2
        count += 1
    return factors
    
def main():
    print("Program for PE 12")
    curNum = 1
    count = 2
    while ( numOfFactors(curNum) <= _FACTORS ):
        #print(curNum, numOfFactors(curNum), int(math.sqrt(curNum))) 
        curNum += count
        count += 1   
    print(curNum)
            
main()