#include <stdio.h>
#include <stdlib.h>
#include <conio.h> 
#include <math.h> 
#include <string.h>
#include <time.h> 



int main() 
{ 
     int length, breadth;


     printf("enter length and breadth of rectangle: ");

     scanf("%d %d", &length, &breadth);

     int area = length * breadth;


     printf("The area of the rectangle is: %d\n", area);
     return 0; 
}