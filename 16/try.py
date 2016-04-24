"""
=============================================================
Trial Program for PE 16

Goal: Find the sequence required to answer the program

=============================================================
"""
_BASE = 2


def power(exp):
    return _BASE ** exp

def sumOfDigits(curNum):
    sum = 0
    while curNum:
        sum += curNum % 10
        curNum //= 10
    return sum
    
def main():
    print("Trial Program PE 16")
    exp = 0
    while (exp <= 1000):
        curNum = power(exp)
        sum = sumOfDigits(curNum)
        exp = exp + 1
        print(sum)
        
            
main()