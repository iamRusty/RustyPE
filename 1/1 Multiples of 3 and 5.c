//Multiples of 3 and 5 https://projecteuler.net/problem=1
#include <stdio.h>

int main(void)
{
    int threes, fives, fifteens;
    int sum = 0;
    for (threes = 3; threes < 1000; threes = threes + 3)
    {
        sum = sum + threes;
    }
    for (fives = 5; fives < 1000; fives = fives + 5)
    {
        sum = sum + fives;
    }
    for (fifteens = 15; fifteens < 1000; fifteens = fifteens + 15)
    {
        sum = sum - fifteens;
    }
    printf("%i", sum);
}