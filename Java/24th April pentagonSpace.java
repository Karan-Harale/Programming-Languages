// class pentagon {
//     public static void main(String[] args) {
//  int sum=0;
// int num=13579;

// while(num>0){
//     int rem=num%10;
//     sum=sum+rem;
//     num=num/10;
//     System.out.println(rem);

// }
//     }
// }





class pentagon {
    public static void main(String[] args) {
int num=13579;
int rev=0;
while(num>0)
{
   int  rem=num%10;
    rev=(rev*10)+rem;
    num=num/10;

}
System.out.println(rev);

    }
}













