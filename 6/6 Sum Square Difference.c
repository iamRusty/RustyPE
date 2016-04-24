/*
    Sum Square Difference
    
    The sum of the squares of the first ten natural numbers is,
        12 + 22 + ... + 102 = 385    
    The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)2 = 552 = 3025
        
    Hence the difference between the sum of the squares of the first 
    ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum.
    
    https://projecteuler.net/problem=6
*/

#include <stdio.h>

int main(void)
{
    long sumOfSquare, squareOfSum;
    long count1, count2, count3;
    
    sumOfSquare = 0;
    squareOfSum = 0;
    
    //Computes for the sum of squares
    for (count1 = 1; count1 <=100; count1++)
        sumOfSquare = sumOfSquare + count1 * count1;
        
    //Computes for the square of sum
    for (count2 = 1; count2 <= 100; count2++)
        for (count3 = 1; count3 <= 100; count3++)
            squareOfSum = squareOfSum + count2 * count3;
    
    printf("Answer: %li - %li = %li\n", squareOfSum, sumOfSquare, squareOfSum - sumOfSquare);
    return 0;
}
/* Interesting Notes
    If counting numbers are treated as variables
    then the answer equals twice the triangle of monomials.
    
    There are other mathematical beauties behind this problem...
    
    hmm answer = n*(n+1)*(3*n*n-n-2)/12 where n = number of digits
*/