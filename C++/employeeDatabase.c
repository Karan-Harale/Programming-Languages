#include <stdio.h>

typedef struct employeeDatabase
{
    char name[50];
    int employeecode;
    int salary;

} employee;

void read(employee db[], int n);

void modify(employee st[], int n);

void print(employee db[], int n);

void sort(employee st[], int n);

int search(employee st[], int n);

void exit();

void main(void)
{

    employee db[50];

    int choice, n, position, s;

    printf("Enter Start Key : ");
    scanf("%d", &s);

    if (s == 7788)
    {
        while (1)
        {
            printf("\n\t\t1.read\n\t\t2.modify\n\t\t3.print\n\t\t4.search\n\t\t5.sort\n\t\t00.Exit\n\n\tChoice: ");

            scanf("%d", &choice);

            switch (choice)
            {
            case 1:
                printf("Enter number of Employees : ");
                scanf("%d", &n);

                read(db, n);

                break;
            case 2:
                modify(db, n);

                break;

            case 3:
                printf("Enter number of Data want to see : ");
                scanf("%d", &n);

                print(db, n);

                break;
            case 4:
                search(db, n);

                break;

            case 5:

                sort(db, n);

                break;

            case 00:
                exit(0);

                break;

            default:
                printf("Invalid choice!!!\n");
                break;
            }
        }
    }
    else
    {
        printf("Unable to START : Invalid Key!!!\nRun Again!\n\n");
    }
}

void read(employee db[], int n)
{

    for (int i = 0; i < n; i++)
    {
        printf("Enter the data for employee %d: ", i + 1);
        scanf("%s%d%d", db[i].name, &db[i].employeecode, &db[i].salary);
    }
}

void print(employee db[], int n)
{
    printf("Number of Employees: %d", n);

    printf("\n\nName\t\tEmployeecode\t\tSalary", n);

    for (int i = 0; i < n; i++)
    {
        printf("\n\n%s\t\t %d\t\t\t%d", db[i].name, db[i].employeecode, db[i].salary);
    }
}

void sort(employee db[], int n)
{
    employee temp;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - 1 - i; j++)
        {
            if (db[j].salary > db[j + 1].salary)
            {
                temp = db[j];

                db[j] = db[j + 1];

                db[j + 1] = temp;
            }
        }
    }
    printf("Sorted Successfully\n");
}

int search(employee db[], int n)
{
    int code;

    int result = 0;

    printf("\n Enter Employee code: ");
    scanf("%d", &code);

    for (int i = 0; i < n; i++)
    {
        if (db[i].employeecode == code)
        {
            printf("\n\nName\t\tEmployeecode\t\tSalary", n);
            printf("\n\n%s\t\t %d\t\t\t%d\n", db[i].name, db[i].employeecode, db[i].salary);
            break;
        }
        printf("\nEmployee Data not available!!!");
    }
}

void modify(employee db[], int n)
{
    char newname[20];
    int code;

    printf("\n Enter Employee code for fetching details: ");
    scanf("%d", &code);

    for (int i = 0; i < n; i++)
    {
        if (db[i].employeecode == code)
        {
            printf("\nEnter New Details : ");
            scanf("%s%d%d", db[i].name, &db[i].employeecode, &db[i].salary);

            printf("\n\nName\t\tEmployeecode\t\tSalary", n);
            printf("\n\n%s\t\t %d\t\t\t%d\n", db[i].name, db[i].employeecode, db[i].salary);
            break;
        }
    }
    printf("\n\n");
}