#include <stdio.h>
#include "libcheckprime.h"

void main() 
{
    while(1){
        int x;
        printf("input integer (0:Exit): ");
        scanf("%d", &x);
        if (x == 0){
            printf("Program Exit\n");
            break;
            }
        if (prime(x) == 0){
            printf("%d is not prime number\n", x);}
        else{
            printf("%d is a prime number\n", x);}
    }

}
