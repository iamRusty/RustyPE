/* Summation of Primes
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
*/

#include <iostream>
#include <math.h>

using namespace std;

int main(void){
   long count, count2;
   long sum = 2;
   
   for (count = 3; count < 2000000; count+=2) {
       for (count2 = 2; count2 < sqrt(count) + 1; count2++) {
           if (count % count2 == 0)
               break;
       }
       
       if (count2 > sqrt(count)) 
            sum+= count;       
            
   }
   cout << sum << endl;
   return 0;
}

/* Programmer's Note
    sqrt() function is necessary to GREATLY lessen the time
    of determining if a number is prime.
    
    Review Sieve algorithm
*/