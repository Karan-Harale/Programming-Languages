#include <stdio.h>
#include <stdlib.h>
#include <conio.h> 
#include <math.h> 
#include <string.h>
#include <time.h> 


// copy,length,  reverse, compare, palinderome, substring

void copy (char[10]);
void palindrome (char[10]);
int length (char[10]);
void reverse (char[10]);
void compare (char[10]);
void subString (char[10]);


int main() 
{ 
    int choice;

    char tempstr[10];

    printf("\nEnter String  : ");

    scanf("%s", &tempstr);

    printf("\nChoose which string operation you want to perform.\n");

    printf("\t\t1.Copy\n\t\t2.Length\n\t\t3.Compare\n\t\t4.Reverse\n\t\t5.Palindrome\n\t\t6.Substring\n\t\tQ.Quit\n\n\tChoice : ");

    scanf("%d", &choice);


    

    switch (choice)
    {

    case 1: copy(tempstr); break;

    case 2: length(tempstr); break;

    case 3: compare(tempstr); break;
    
    case 4: reverse(tempstr); break;

    case 5: palindrome(tempstr); break;

    case 6: subString(tempstr); break;

    case 0 : exit(0); break;


    default:printf("\t\tInvalid choice\n");
        break;
    }
     
    return 0; 
}



void copy(char str1[])
{

    char copystr[10];

    
    for (int i = 0; i <= strlen(str1); i++)
    {
        copystr[i] =  str1[i];

        // printf("%s",copystr[i]);

    }
    printf("\nCopied String: %s", copystr);

}

int length(char str1[])

{
    printf("Length = %d", strlen(str1));
}

void reverse(char str1[])
{
     printf(str1 );

    int k = strlen(str1);


    char str2 [10];

    int i=0;

   int result;
    
   result = 0;

  for ( i = 0; i < k; i++) 
  {
        str2[i] = str1[k - 1 - i];
    }
  

    printf("\n%s",str2); 

}


void palindrome(char str1[])
{
    printf(str1 );

    int k = strlen(str1);


    char str2 [10];

    int i=0;

   int result;
    
   result = 0;

  for ( i = 0; i < k; i++) 
  {
        str2[i] = str1[k - 1 - i];
    }
  

    printf("\n%s",str2); 

    

    for (i=0; i<k ; i++) 
    {
        if (str1[i] == str2[i])
        {
            printf("\n%c", str1[i]);
            result = 1;
            

        }
        else{
            result = 0;
            
        }
        
    }

    if (result == 1)
    {
printf("\npalindrome");
    }
    else{
printf("\nNon palindrome");
    }
}
 
 
void compare(char str1[])
{

    char str2[10];
    int count = 0;

    printf("Enter string for comparison : ");

    scanf("%s", &str2);

    for (int i = 0; i <strlen(str1); i++)
    {
        for (int j = 0; j <strlen(str2); j++)
      {  
        if (str2[i] == str1[i])
        {
            count += 1;
            break;
        }
        }
    }

    if(count == strlen(str1))
    {
        printf("\n Matched");
    }
    else{
        printf("\n Not Matched");
    }
     
}


void subString(char str1[])
{

    char str2[5];
    int count = 0;

    printf("Enter substring : ");

    scanf("%s", &str2);

    for (int i = 0; i <strlen(str2); i++)
    {
        for (int j = 0; j <strlen(str1); j++)
      {  
        if (str1[j] == str2[i])
        {

            // int result = count+1 

            printf("String Present at index : %d\n", count+1);           
            break;
            
        }
        count += 1;
        
        }
        
    }

// printf("String Present at index : %d\n", count-1);

}