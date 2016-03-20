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
    f.close()
    return number

#Credits to Uziel Agub for introducing this method. I'm amazed
def maxPathSum(number):
    numOfRows = len(number) - 1
    count = numOfRows - 1
    while (count > -1):
        curCol = 0
        while (curCol < len(number[count])):
            if (number[count + 1][curCol] > number[count + 1][curCol + 1]):
                number[count][curCol] += number[count + 1][curCol]
            else:
                number[count][curCol] += number[count + 1][curCol + 1]
            curCol += 1      
        count -= 1       
    return number[0][0]
                    
def main():
    number = extract(_FILE_NAME) 
    answer = maxPathSum(number)
    print(answer)
           
main()
