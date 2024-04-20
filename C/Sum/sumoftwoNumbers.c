#include <stdio.h>
#include <stdlib.h>
#include <conio.h> 
#include <math.h> 
#include <string.h>
#include <time.h> 



int main() 
{ 
    int a, b;
    a = 5;
    b = 10;


    printf("Enter the value of a and b: ");

    scanf("%d%d", &a,&b);

    int c = a + b;

    printf("%d + %d = %d", a, b, c);
     
    return 0; 
}