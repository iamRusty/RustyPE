/* 10 Summation of Primes
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
*/

#include <stdio.h>
#include <math.h>

int main(void) {
    long count, currentNumber, sum;
    sum = 2;
    
    //currentNumber = currentNumber + 2 to skip out even numbers    
    for (currentNumber = 3; currentNumber < 2000000000; currentNumber += 2) {
        printf("current number: %li", currentNumber);
        
        long sqrtNum = sqrt(currentNumber);
        //For Optimal performace, use "count < sqrt(currentNumber)"
        for (count = 3; count < sqrtNum; count = count + 2) {
            if (currentNumber % count == 0)
                break;
        }
        
        if (count >= sqrtNum) {
            sum += currentNumber;
            printf("yes");
        }
        printf("\n");
    }
    
    printf("Sum: %li", count);
    return 0;
}