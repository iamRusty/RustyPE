/*
    Smallest Multiple
    
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/
#include <stdio.h>

int main(void)
{
    long count, product;
    
    product = 1;
    
    for (count = 2; count <= 20; count++)
    {
        printf("%li - ", count);
        if (product % count)
        {
            product = product * count;
            printf("ok - %li\n", product);
        }
        else 
            printf("fail\n");
    }
    
    printf("Smallest Multiple: %li\n", product/24); 
    
    return 0;
}


// Another Beautiful Algorithm
/* Credits to lassevk

Python:
i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print i

*/