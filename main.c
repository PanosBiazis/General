#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

void addf(){
	int size;
	printf("Give the size of the table?\n");
	printf("Size:");
	scanf("%d",&size);
	printf("The size:%d\n",size);
	double num[size];
	printf("Give me a number:");
	scanf("%lf",&num[size]);
	printf("%lf\n",num[size]);
	double number;
	puts("Give another number to add?");
	printf("Number:");
	scanf("%lf",&number);
	int times;
	puts("Give how many times do you want to increase?");
	printf("Times:");
	scanf("%d",&times);
	for (int i=1;i<=times;i++){
		num[size]=num[size]+number;
		printf("The %d time,The number is %lf\n",i,num[size]);
	}
	for (int i=0;i<=size;i++){
	printf("The %d element of the table of the number is %lf\n",i,num[i]);
	}
}

int main(int argc, char *argv[]) {
	addf();
	return 0;
}
