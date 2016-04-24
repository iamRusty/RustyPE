/*
    10001st Prime
    
    By listing the first six currentNumber numbers: 
    2, 3, 5, 7, 11, and 13, 
    we can see that the 6th currentNumber is 13.
    What is the 10 001st currentNumber number?
    
    https://projecteuler.net/problem=7
*/
#include <stdio.h>

int main(void)
{
    long count, currentNumber, primeCount;
    
    primeCount = 1;
    
    for (currentNumber = 3; primeCount != 10001; currentNumber = currentNumber + 2) //currentNumber = currentNumber + 2 to skip out even numbers
    {
        for (count = 3; count < currentNumber; count = count + 2) //For Optimal performace, use "count < sqrt(currentNumber)"
        {
            if (currentNumber % count == 0)
                break;
        }
        
        if (count == currentNumber)
            primeCount++;
    }
    
    printf("10001st Prime number: %li", count);
    return 0;
}

