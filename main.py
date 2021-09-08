#include<stdio.h>
int main()
{
   int num1,num2;
   int add,sub,mul,modulo;
   float div;
   printf("Enter two number from user : ");
   scanf("%d%d",& num1,&num2) ;
   add=num1 + num2;
   sub=num1 - num2;
   mul=num1 * num2;
   div=num1 / num2;
   modulo=num1 % num2;
   printf("The sum is:%d\n",add);
   printf("the sub is :%d\n",sub);
   printf("the mul is :%d\n",mul);
   printf("the div is :%d\n",div);
   printf("the modulo is :%f\n",modulo);
   return 0;
}   
