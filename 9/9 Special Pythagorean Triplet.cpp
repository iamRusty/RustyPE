/* Special Pythagorean Triplet
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
*/
#include <iostream>

using namespace std;

int main(void) {
    int a, b, c, sum;
    bool isDone = false;
    
    
    for (a = 1; a <= 1000; a++) {
        for (b = 1; b<= 1000; b++) {
            sum = a * a + b * b;
            c = 1000 - (a + b);
            
            if ((c * c) == sum) {
                isDone = true;
                break;
            }
        }
        if (isDone)
            break;
    }
    
    cout << a << " - " << b << " - " << c << endl;
    cout << "Product: " << a*b*c << endl;
    return 0;
}