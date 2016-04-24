/* Special Pythagorean Triplet
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
*/

#include <stdio.h>

int main(void) {
    long c, sum;
    long count1, count2;
    
    for (count1 = 1; count1 <= 1000; count1++) {
        for (count2 = 1; count2 <= count1; count2++) {
            c = 1000 - (count1 + count2);
            sum = count1 * count1 + count2 * count2;
            
            //printf("%li %li = %li\n", count1 * count1, count2 * count2, c * c);
            if ((c * c ) == sum)
                break;
        }
    }
    
    printf("%li %li %li\n", count1, count2, c);
}