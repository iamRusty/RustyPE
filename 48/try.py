"""
===============================================================
Trial Program for PE 48

Goal: Find the last ten digits of the series
        1^1 + 2^2 + 3^3 + ... + 1000^1000

Note: 
===============================================================
"""
import math
_CONSTANT_ = 1000
def main():
    count = 1
    sum = 0
    while (count <= _CONSTANT_):
        print(count)
        sum += count ** count
        count += 1
        
    print("Last 10 digits:" + str(sum%10000000000))
            
main()
