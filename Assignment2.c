#include<stdlib.h>
#include<stdio.h>

int main(){

 int height;   
 printf("Enter the Height of the Pyramid: \n"); 
 printf("Note: Min Height is 2 and Max Height is 5 \n");
 scanf("%d",&height);

 if (height == 2){
   printf(" /|\\\n");
   printf("/_|_\\\n");

 } else if (height ==3){
   printf("  /|\\\n");
   printf(" / | \\\n");
   printf("/__|__\\\n");
   
 }  else if (height ==4){
   printf("   /|\\\n");
   printf("  / | \\\n");
   printf(" /  |  \\\n");
   printf("/___|___\\\n");

 } else if (height ==5){
   printf("    /|\\\n");
   printf("   / | \\\n");
   printf("  /  |  \\\n");
   printf(" /   |   \\\n");
   printf("/____|____\\\n");

 } else{  
  printf("Invalid Height \n");
 }

 return 0;
}
