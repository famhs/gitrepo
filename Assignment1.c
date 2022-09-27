#include <stdio.h>
#include <stdlib.h>

int main()
{
double num1;
double num2;
double num3;
printf("Enter the value of the first number: "); 
scanf("%lf",&num1);
printf("Enter the value of the second number: ");
scanf("%lf",&num2);
printf("Enter the value of the third number: ");
scanf("%lf",&num3);

printf("The Sum is: %f\n", num1+num2+num3);
printf("The Average is: %f\n",(num1+num2+num3)/3.0);

return 0;
}