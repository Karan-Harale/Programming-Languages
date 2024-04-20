#include <stdio.h>
#include <stdlib.h>
#include <conio.h> 
#include <math.h> 
#include <string.h>
#include <time.h> 



int main() 
{ 
     int a = 4;

     int b = 6;

     swapbyvalue(a,b);
      printf("values after swapping by value : a= %d and b = %d\n",  a,b);  //does not workbecause we are providing copied values to the function so it cannot modify original values

    swapbyreference(&a, &b);

     printf("values after swapping by reference : a= %d and b = %d\n",  a,b); 
     
     tentimes(&a);

    printf("Ten times = %d\n",  a); 
     return 0; 
}

void swapbyvalue(int a, int b)
{
    int temp = a;
    a=b;
    b=temp;
}

void swapbyreference(int *a, int *b)
{
    int temp = *a;
    *a=*b;
    *b=temp;
}

void tentimes(int *a)
{
    *a = *a * 10;
}