#include <stdio.h>
#include <stdlib.h>
#include <conio.h> 
#include <math.h> 
#include <string.h>
#include <time.h> 



int main() 
{ 
    int i = 34;

    int *j = &i;

    printf("address of i: %d\n", j);

    int **k = &j;
    printf("address of j: %d\n", k);
    printf("address of j: %d\n", *(&k));
    printf("address of j: %d\n", **k);  //dereferencing the value of k points to j and j points to add of i which value is 34

     return 0; 
}