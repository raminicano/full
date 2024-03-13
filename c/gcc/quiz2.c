#include <stdio.h>
#include "libcheckeod.h"

void main() 
{
    while(1){
        int x;
        printf("Input Number : ");
        scanf("%d", &x);
        if (x == 0){
            printf("Program Exit\n");
            break;
            }
        eod(x);
    }

}
