/*
    Largest Prime Factor
    
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    https://projecteuler.net/problem=3
*/

/* Technique
    The usual approach of attacking the problem is to find a prime number
    and test if it's a factor of the number. This is inefficient.
    Instead, look for the factors of the number and test if it's prime.
    Again, although that is more efficient, it is still inefficient.
     
    The MOST EFFICIENT way of attacking this problem is to find small prime numbers
    which are factors of the number and perform divition between them. 

    Use of "continue" and "break" is highly-encouraged.
*/
#include <stdio.h>

int main(void)
{
    long number, count, prime;
    number = 600851475143;
    
    for (prime = 3; prime < number; prime = prime + 2) //prime = prime + 2 to skip out even numbers
    {
        for (count = 2; count < prime; count++)
        {
            if (prime % count == 0)
                break;
        }
        
        if (count == prime)
        {
            if (number % prime == 0)
                number = number / prime;
        }
        
    }
    
    printf("%li", number);
    return 0;
}