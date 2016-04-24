"""
=============================================================
Trial Program for PE 20

Goal: Find the sum of the digits of number 100!

=============================================================
"""
_BASE = 100


def factorial(base):
    curNum = 1
    while (base):
        curNum *= base
        base -= 1
    return curNum

def sumOfDigits(curNum):
    sum = 0
    while curNum:
        sum += curNum % 10
        curNum //= 10
    return sum
    
def main():
    print("Trial Program PE 20")
    num = factorial(_BASE)
    sumDig = sumOfDigits(num)
    
    print(sumDig)    
            
main()