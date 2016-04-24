"""
===============================================================
Trial Program for PE 18

Goal: Find the greatest path-sum. 
        https://projecteuler.net/problem=18

Note: The program uses FILE IO
===============================================================
"""
_FILE_NAME = "data.pe"

def extract(fileName):
    f = open(fileName, "r")
    data = f.readlines()
    number = []
    for line in data:
        row = line.split()
        number.append(row)
    count = 0
    while (count < len(number)):
        number[count] = [int(i) for i in number[count]]
        count += 1
    return number
    
def maxPathSum(number):
    count = 1
    curIndex = 0
    maxSum = number[0][0]
    while (count < len(number)):
        if ( number[count][curIndex] >= number[count][curIndex + 1] ):
            maxSum += number[count][curIndex]
        else:
            maxSum += number[count][curIndex + 1]
            curIndex += 1
        count += 1
    return maxSum
                
def main():
    number = extract(_FILE_NAME) 
    answer = maxPathSum(number)
    print(answer)
           
main()
