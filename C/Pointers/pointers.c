#include <stdio.h>
#include <stdlib.h>
#include <conio.h> 
#include <math.h> 
#include <string.h>
#include <time.h> 



int main() 
{ 
    int i = 10;

    int *j= &i;

    printf("i=%d\n", i);
    printf("add i= %d\n", j);
    printf("value@ add i= %d\n", *j);

    printf("value@ add i= %u\n", *(&j));
     return 0; 
}