//Credits to xingliang of Project Euler. This is beauty

#include <stdio.h>
#include <math.h>

int main()
{
    int p, f1, f2;
    int n1, n2, n3;

    for (n1 = 9; n1 > 0; n1--)
        for (n2 = 9; n2 >= 0; n2--)
            for (n3 = 9; n3 >= 0; n3--) {
                p = n1 * 100001 + n2 * 10010 + n3 * 1100;
                for (f1 = sqrt(p); f1 >= 100; f1--) {
                    if (p % f1 == 0) {
                        f2 = p / f1;
                        if (f2 < 999) {
                            printf("%d = %d x %d\n", p, f1, f2);
                            return 0;
                        }
                    }
                }
            }

    return 0;
}