"""
================================================================
Trial Program for PE 21

Goal: Find the sum of all Amicable Numbers under 10000

Note: Amicable numbers are pairs that have equal sum of factors
      e.g. 220 (1, 2, 4, 5, 10, 11, 20, 22, 44, 55) 
      and 284 (1, 2, 4, 71, 142)
================================================================
"""
import math
_UPPER_LIMIT = 10000

def factorSum(num):
    count = 2
    sum = 1
    while (count < math.sqrt(num) + 1):
        if (count > num // count):
            count += 1
        elif ((num % count == 0) and (num // count == count)):
            sum += count
            #print(count)
        elif (num % count == 0):
            sum = sum + count + (num // count)
            #print (count, num // count)            
        count += 1    
        
    return sum
        
def main():
    li = [220, 284]
    count = 2
    while (count < _UPPER_LIMIT):
        #print(count)
        new_num = factorSum(count)
        if new_num in li:
            count += 1
        elif (new_num == count):
            count += 1
        elif (count == factorSum(new_num)):
            li.append(new_num)
            li.append(count)
        count += 1
    sum = 0
    for i in li:
        print(i)
        sum += i
    print("Sum: ", sum)
                
main()
