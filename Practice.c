#include <stdio.h>
#include <stdlib.h>
// extern char *fgets (char *__restrict __s, int __n, FILE *__restrict __stream)

void main(){
	
	printf("Hello World\n");
	char *myFruit="Papaya";
	printf("What %8s is?\n",myFruit);
	int myNumber=909090;
	printf("My number is %d\n",myNumber);
	printf("\t*\v*\n");
	printf("\rwhat\r");
	char myArray[6]="PANOS";
	printf("Give your name:");
	puts(myArray);
	char myArray2[20];
	printf("Give your name>>");
	// fgets(myArray2);
	printf("%6s\n",myArray2);
	int x;
	printf("Give a number>>");
	scanf("%d",&x);
	printf("%d\n\a",x);
	system("pause");
	for (int i=0;i<5;i++){
		printf("\t\v*\n");
	}
	printf("\f");
	printf("What is it?\n");
	printf("%x\n%o\n",&x,&x);
	printf("%x\n",&x);
	printf("\v\v*\n");
	float myNumber2=90.55;
	printf("%5.2f\n",myNumber2);
	int myNumber3=(int)myNumber2;
	printf("%d\n",myNumber3);
	double myNumber4=(double)myNumber3;
	printf("%2.3f\a\n",myNumber4+0.455);
	// return 0;
}
