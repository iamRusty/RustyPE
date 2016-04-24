/*
    Largest Palindrome Product
    
    A palindromic number reads the same both ways. 
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    
    https://projecteuler.net/problem=4
*/

#include <stdio.h>

int main(void)
{
    int a, b, current_number, count, exponent, divider, placeholder_number, count2, count3, done, lower_limit;
    int printf_number, biggestNumber;
    int digits[6];
    
    biggestNumber = 1;
    done = 0;
    lower_limit = 99;
    for (a = 999; a > 99; a--)
    {
        for (b = 999; b > lower_limit; b--)
        {
            current_number = a * b;
            printf_number  = current_number;
            placeholder_number = current_number;
           
            //Counts the number of digits
            for (count = 0; placeholder_number != 0; count++)
                placeholder_number = placeholder_number/10;
            
            count--;
            count2 = count;
            
            //Extracts the digits
            for (; count>=0; count--)
            {
                divider = 1;
                for (exponent = count; exponent > 0; exponent--)
                    divider = divider * 10;
                
                digits[count] = current_number / divider; //digits[] array stores the digits
                current_number = current_number - divider * digits[count];
            }
            
            //Compares the digits if they satisfy palin behaviour
            for (count3 = 0; count3 <= count2 - count3; count3++)
            {
                if (digits[count3] != digits[count2-count3])
                    break;
            }
            
            //Which is the bigger palindrome?
            if (count3 > count2/2)
            {
                done++;
                lower_limit = b;
                if (biggestNumber < printf_number)
                    biggestNumber = printf_number;
                printf("%i = %i * %i\n", printf_number, a, b); //prints all the "big" palindromes
                break;
            }            
        }
    }    
    
    printf("Biggest Palindrome: %i\n", biggestNumber);
    return 0;
}