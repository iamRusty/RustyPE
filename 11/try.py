"""
===============================================================
Trial Program for PE 11

Goal: Find the greatest product of 4 adjacent numbers in the
      array given. https://projecteuler.net/problem=11

Note: The program uses FILE IO
===============================================================
"""
_FILE_NAME = "data.pe"
_NUMBERS_TO_MULTIPLY = 4
_ARRAY_SIZE = 20

def extract(fileName):
    f = open(fileName, "r")
    data = f.readlines()
    number = []
    for line in data:
        row = line.split()
        number.append(row)
    count = 0
    while (count < _ARRAY_SIZE):
        number[count] = [int(i) for i in number[count]]
        count += 1
    return number

def product(count1, count2, number):
    product1 = 0
    product2 = 0
    product3 = 0
    product4 = 0 
    
    if (count1 < _ARRAY_SIZE - (_NUMBERS_TO_MULTIPLY - 1)):
        product1 = number[count1][count2] * number[count1 + 1][count2] * number[count1 + 2][count2] * number[count1 + 3][count2]
    if (count2 < _ARRAY_SIZE - (_NUMBERS_TO_MULTIPLY - 1)):
        product2 = number[count1][count2] * number[count1][count2 + 1] * number[count1][count2 + 2] * number[count1][count2 + 3]
    if ((count1 < _ARRAY_SIZE - (_NUMBERS_TO_MULTIPLY - 1)) and (count2 < _ARRAY_SIZE - (_NUMBERS_TO_MULTIPLY - 1))):
        product3 = number[count1][count2] * number[count1 + 1][count2 + 1] * number[count1 + 2][count2 + 2] * number[count1 + 3][count2 + 3]
    if ((count1 >= _NUMBERS_TO_MULTIPLY - 1) and (count2 < _ARRAY_SIZE - (_NUMBERS_TO_MULTIPLY - 1))):
        product4 = number[count1][count2] * number[count1 - 1][count2 + 1] * number[count1 - 2][count2 + 2] * number[count1 - 3][count2 + 3]
    
    li = [product1, product2, product3, product4]
    #print(li, " - ", count1, count2)
    return max(li)
        
def main():
    number = extract(_FILE_NAME)
    largestProduct = 1
    
    count1 = 0
    while (count1 < _ARRAY_SIZE):
        count2 = 0
        while (count2 < _ARRAY_SIZE):
            challenger = int(product(count1, count2, number))
            if (challenger > largestProduct):
                largestProduct = challenger
                largeCount1 = count1
                largeCount2 = count2
            count2 += 1
        count1 += 1    
            
    print(largestProduct, largeCount1, largeCount2)
           
main()
