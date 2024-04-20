#include <stdio.h>
#include <stdlib.h>



typedef struct studentdata
{
    int rollno;
    float marks;
    char name[50];
} student;


void read(student st[], int);

void display(student st[], int);

void sortedElements(student st[], int);



int main()
{
    student st[50];

    int ch, n;

    printf("\n Enter the Number of Students: ");

    scanf("%d", &n);

    while(1)
    {
        printf("\n1.Read\n2.Display\n3.Sort\n4.Exit\n");

        printf("Enter Choice: ");
        scanf("%d", &ch);

        switch (ch)
        {
        case 1: read(st, n); break;
            
        case 2: display(st, n); break;

        case 3: sortedElements(st, n);
                // display(st, n);
                
                break;

        case 4: exit(0) ; break;


        default:printf("\nWrong Choice\n");
        
        }
    }
    return 0;
}


void read(student st[], int n)
{
    int i;

    printf("\n Enter the %d records in order ->name ,rollNo, marks\n", n);

    for (i=0; i<n; i++)
    {
        printf("\n Enter student %d record\n", i+1);

        scanf("%s%d%f", st[i].name, &st[i].rollno, &st[i].marks );
    }
}


void display(student st[], int n)
{
    int i;
      printf("\n\tStudent Data: \n");

    for (i=0; i<n; i++)
    {
        printf("\n\t%s\t%d\t%.2f\n", st[i].name, st[i].rollno, st[i].marks);
        
        }
}

void sortedElements(student st[], int n)
{

    student temp;

    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n-i-1; j++)
        {
            if (st[j].marks > st[j+1].marks)
            {
                temp = st[j];

                st[j] = st[j+1];

                st[j+1] = temp;

            } 
        }
    }

}