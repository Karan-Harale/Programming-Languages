#include <stdio.h>
#include <stdlib.h>
#include <conio.h> 
#include <math.h> 
#include <string.h>
#include <time.h> 



void main() 
{ 


    int k = 0;

    int *p  = &k;

    int add = p + 2;


     printf("\n %d",p);  //returns address of p

     printf("\n %d",*p); //returns value of p


     printf("\n %d",add);  //returns next element addresee of p becouse min datatype character takes 2 bytes of input



     int i = 105;

int *p1;

p1 = &i;


printf("\n value of i = %d", *p1);
printf("\n value of i = %d", *&i);
printf("\n address of i = %d", &i);
printf("\n address of i = %d", p1);
printf("\n address of p = %d", &p1);


 }