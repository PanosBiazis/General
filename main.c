// A preprocessor is a program which is executed before passing the source program to the compiler.
//(#) c uses hash to execute smalls fuction in preprocessor
#include <stdio.h> // is a header file which contains definitions of input/output operations.
#include <stdlib.h>// is another header file in c which contain memory managemet utilities and string conversion functions.
#include <string.h>//for strings fuctions
// #define is used to define a macro
#define STATES 29
#define IP 14.30
#define meme "program 2.0"
// #undef is used to undefine a macro,opposite of what  #define does
// #include is used to include a header file
// #if and #else can be used to check if a condition is true even before the source is compiled 
// #ifdef is used to check if a macro is define.if the macro is defined it returns true
// #ifndef is used to check if a macro is not defined.if the macro isn't defined it returns true
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
/* wow*/
#include <math.h> //is a header file which contains mathematical function which can be directlynused to perform numerous operations.
#include <time.h> // contains functions to perform operations on time.
// #include <conio.h>
#define KMS_PER_MILE 1.609
enum days_of_week{Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday};//Enumeration (or enum) is a user defined data type in C. It is mainly used to assign names to integral constants, the names make a program easy to read and maintain.
enum year{null,Jan, Feb, Mar, Apr, May, Jun, Jul,Aug, Sep, Oct, Nov, Dec};


void face1(){
	printf("\t\t\t\t*\n");
	printf("\t\t\t*\t\t*\n");
	printf("\t\t*\t  [*]   \t[*]\t*\n");
	printf("\t*\t\t\t\t\t\t*\n");
	printf("\t\b*\t\t\t\t\t\t\t\b\b\b\b\b\b\b*\n");
	printf("\t\b\b|\t\t\t\t\t\t\t\t\b\b\b\b\b\b|\n");
	printf("\t\b*\t\t\t\t\t\t\t\b\b\b\b\b\b\b*\n");
	printf("\t*\t\t\t\t\t\t*\n");
	printf("\t\t*\t\t\t\t*\n");
	printf("\t\t\t*\t(----)\t*\n");
	printf("\t\t\t\t*\n");	
	}
	

	void tringle(){
	printf("............/\\\n");
	printf("...........*..*\n");
	printf("..........*....*\n");	
	printf(".........*......*\n");
	printf("........*........*\n");
	printf(".......*..........*\n");
	printf("......*............*\n");
	printf(".....*..............*\n");
	printf("....*................*\n");
	printf("...*..................*\n");
	printf("..*....................*\n");
	printf(".*......................*\n");
	printf("*........................*\n");
	printf("--------------------------\n");
	}
	
	void circle(){
	printf("..................**********\n");
	printf(".............*...................*\n");
	printf("..........*........................*\n");
	printf(".......*.............................*\n");	
	printf("......*................................*\n");
	printf("....*....................................*\n");
	printf("...*......................................*\n");
	printf("..*........................................*\n");
	printf(".*..........................................*\n");
	printf(".*..........................................*\n");
	printf(".*..........................................*\n");
	printf(".*..........................................*\n");
	printf(".*..........................................*\n");
	printf("..*.........................................*\n");
	printf("...*.......................................*\n");
	printf("....*.....................................*\n");
	printf(".....*..................................*\n");
	printf(".......*..............................*\n");
	printf(".........*..........................*\n");
	printf("...........*......................*\n");
	printf(".............*..................*\n");
	printf("..................**********\n");
	}
	
	int Main_Menu(int selection){
Begin:;
	printf("1.General Graphics\n2.Specific Graphics\n3.Exit\n");
	printf("Selection >>");
	scanf("%d",&selection);
	printf("Selected:%d\n",selection);
	switch(selection){
		case 1:
			Shape_selection:;
			printf("Which of the shapes do you want to print:\n");
			printf("1.Tringle\n2.Circle\n3.Exit\n");
			printf("Shape Selection>>");
			scanf("%d",&selection);
			printf("Selected:%d\n",selection);
			switch(selection){
				case 1:
					tringle();
					break;
				case 2:
					circle();
					break;
				case 3:
					printf("OK!!!\a\n");
					break;
				default:
					printf("Select again!!!\a\n");
					goto Shape_selection;
			}
			break;
		case 2:
			face1();
			face1();
			break;
		case 3:
			printf("OK!!!\a\n");
			break;
		default:
			printf("ERROR\a\nWrong input!!!\nTry again\n");
			goto Begin;
			break;
	}
	return selection;
	}

void colourfulF(){
	/*
    Black \033[0;30m
	Red \033[0;31m
	Green \033[0;32m
	Yellow \033[0;33m
	Blue \033[0;34m
	Purple \033[0;35m
	Cyan \033[0;36m
	White \033[0;37m	*/
	printf("\033[0;31m");//colour
	printf("******\n******\n******\n******\n");
	printf("\033[0m");//end the colour
	for (int j=0;j<5;j++){
	printf("\033[0;31m");
	printf("*");
	printf("\033[0m");
	printf("\033[0;32m");
	printf("*");
	printf("\033[0m");
	printf("\033[0;34m");
	printf("*");
	printf("\033[0m\n");
}
}

void name_PANOS_F(int times){
if (times==0) {
	printf("OK!!\n");
}
	for(int i=0;i<times;i++){
	printf("\033[0;31m");
	printf("_______________________________________________________________________________________________________\n");//zero point
	printf("\033[0m");
	printf("\033[0;32m");
	printf("| ____________........^..............||\\.........||...............========..............****...........|\n");//+2 dot
	printf("\033[0m");
	printf("\033[0;33m");
	printf("| ||........||......//.\\.............||.\\........||............*..........*..........*......*..........|\n");//+3 dots
	printf("\033[0m");
	printf("\033[0;34m");
	printf("| ||........||.....//...\\............||..\\.......||...........*............*........*........*.........|\n");//+3 dots
	printf("\033[0m");
	printf("\033[0;35m");
	printf("| ||._______||....//.....\\...........||...\\......||..........*..............*........*.................|\n");//+3 dots
	printf("\033[0m");
	printf("\033[0;36m");
	printf("| |||............//_______\\..........||....\\.....||..........*..............*............*.............|\n");//+3 dots
	printf("\033[0m");
	printf("\033[0;37m");
	printf("| |||...........//---------\\.........||.....\\....||..........*..............*..............*...........|\n");//+3 dots
	printf("\033[0m");
	printf("\033[0;31m");
	printf("| |||..........//...........\\........||......\\...||...........*............*.........*.......*.........|\n");//+3 dots
	printf("\033[0m");
	printf("\033[0;32m");
	printf("| |||.........//.............\\.......||.......\\..||............*..........*...........*......*.........|\n");//+3 dots
	printf("\033[0m");
	printf("\033[0;33m");
	printf("| |||........//...............\\......||........\\.||..............========...............****...........|\n");//+3 dots
	printf("\033[0m");
	printf("\033[0;34m");
	printf("|______________________________________________________________________________________________________|\n");//zero point
	printf("\033[0m");
}
}
void myfunction(){
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
	gets(myArray2);
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
	for(int j=0;j<5;j++){
		system("pause");
		printf("\aERROR\n");
	}
int xy=10;
printf("Hi\n");
for(int i=0;i<10;i++){
	printf("%d\n",i);
if (i==5) {
	printf("It's ok!!\n");
	break;
}
}
printf("\033[1;33m");
printf("Hello world\n");
printf("\033[0m");
}

float Addition(float num1,float num2){
	float result;
	result=num1+num2;
	return result;
}

float subtraction(float num1,float num2){
	float result;
	result=num1-num2;
	return result;
}

float multiplication(float num1,float num2){
	float result;
	result=num1*num2;
	return result;
}

float division_quotient(float num1,float num2){
	division_quotient:;
	float result;
	result=num1 / num2;
	if( num2==0){
		printf("\033[1;31m");
        printf("ERROR\a\n");
		printf("Try again!!!\n");
        printf("\033[0m");
        goto division_quotient;
    }
	return result;
}

int division_remainder(int num1,int num2){
	division_remainder:;
	float result;
	result=num1 % num2;
	if (num2==0){
		printf("\033[1;31m");
        printf("ERROR\a\n");
		printf("Try again!!!\n");
        printf("\033[0m");
        goto division_remainder;
    }
	return result;
}

void sayHi(){
	printf("Hi\n");
}

void recursiveCall(int i){
	while(i<5) {
	printf("%d\n",i);
	if(i=1){
		//exit condition
		break;
	}
	recursiveCall(i-1); //Calling recursiveCall recursively
}
}

	void delay(int number_of_seconds)
{
    // Converting time into milli_seconds
    int milli_seconds = 1 * number_of_seconds;
 
    // Storing start time
    clock_t start_time = clock();
 
    // looping till required time is not achieved
    while (clock() < start_time + milli_seconds);
}

void delay2(int number_of_seconds)
{
    // Converting time into milli_seconds
    int milli_seconds = 1000 * number_of_seconds;
 
    // Storing start time
    clock_t start_time = clock();
 
    // looping till required time is not achieved
    while (clock() < start_time + milli_seconds);
}

char carf(){
	char *car="\033[0;31m***\033[0m";
	printf("%4s",car);
	return 0;
}


void frameSpace(int times){
	for(int i=0;i<times;i++){
	printf("\033[0;32m");
	printf("[\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t]\n");
	printf("\033[0m");
	delay(50);
}
printf("\033[0;32m");
printf("[");
printf("\033[0m");
carf();
printf("\033[0;32m");
printf("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t]\n");
printf("\033[0;32m");
printf("[");
printf("\033[0m");
carf();
printf("\033[0;32m");
printf("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t]\n");
printf("\033[0m");
for(int i=0;i<48;i++){
printf("\033[0;32m");
printf("[\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t]\n");
printf("\033[0m");
delay(100);	
}
}

int main(int argc, char *argv[]) {
	printf("hi\n"); //displays hi and  go to the next line to lay out hi2
	printf("hi2\n"); 
	int a;
	int b;
	a=6;
	b=4;
	char c='J';
	float d=6.52;
	double e=6.523456;
	printf("%d\n",a);
	printf("value of b is: %d\n",b);
	printf("%c\n",c);
	printf("%f\n",d);
	printf("%lf\n",e);
	int plus;
	plus=a+b;
	printf("the value is : %d\n",plus);
	if (plus==11){
		printf("Plus equals to 11.\n");
	} else {
		printf("The plus variable is: %d\n",plus);
	}
	for (int cat=1; cat<5; cat++){
		printf("The cat variable on the for-loop is: %d\n",cat);
	}
	int cat2=0;
	while (cat2<5){
		printf("The cat2 variable on the while-loop is: %d\n",cat2);
		cat2++;
	}
	do{
		printf("The cat2 variable on the do while-loop is: %d\n",cat2);
		cat2++;
	}while (cat2<10);
	int myArray[5];
	myArray[0]=1;
	myArray[1]=2;
	myArray[2]=3;
	myArray[3]=4;
	myArray[4]=5;
	int myArray2[5]={5,6,7,8,9};
	for(int i=0;i<5;i++){
		printf("value at the element %d is:%d\n",i,myArray[i]);
	}
	for(int y=0;y<5;y++){
		printf("value at the element %d is:%d\n",y,myArray2[y]);
	}
	float number_1;
	float number_2;
	printf("Give a random number\n");
	scanf("%f",&number_1);
	printf("Give again a random number\n");
	scanf("%f",&number_2);
	float result;
	result=number_1+number_2;
	printf("The result is :%f\n",result);
	float add;
	add=Addition(number_1,number_2);
	printf("Addition is %f\n",add);
	sayHi();
	sayHi();
	recursiveCall(3); //calling recursiveCall and pass value 3
					//(break;) break statement will terminate the execution of current block and the execution will move out of the block.
					//(continue;) continue statement skips the following statements moves to next iteration and then executes normally.
					//(goto there;) goto statement is used to transfer the control of the program to some other part of the program.
	for (int i=0;i<7;i++){
		if(i==4){
			goto there;
		}
		printf("%d\n",i);
	}
	there:
		printf("That's it\n");
	char str[6]={'H','E','L','L','O'};//the length of the string is always one more than the number of characters in it.
	printf("%s\n",str);
	char str2[9]="whatever";
	printf("%s\n",str2);
	int len=strlen(str);
	int len2=strlen("hi");//STRLEN FUNCTION IS USED TO FIND LENGTH OF THE STRING
	char str3[]="Lion";
	int len3=strlen(str3);
	printf("%d\n",len);
	printf("%d\n",len2);
	printf("%d\n",len3);
	strcat(str2,str3);//strcat function is used to combine two or more words to one word
	printf("%s\n",str2);
	char str4[20];
	strcpy(str4,str3);//strcpy function is used to copy one string to another string
	printf("%s\n",str4);
	int k=strcmp(str2,str3);//strcmp function is used to compare two string lexicographically and print the number between the number of two strings 
	printf("%d\n",k);
	int m=strcmp(str3,str2);
	printf("%d\n",m);
	int o=strcmp(str2,str2);
	printf("%d\n",o);
	int *point=&a; // (*) for the value of the pointers and (&) for the value of the address of the pointers
	printf("%x\n",point);// x for hexadecimental format
	printf("%x\n",*point);
	printf("%x\n",&a); 
	struct Car{ //structures to  store and collect different types of data
		//members
		char model[25];
		int modelNumber;
		int numberOfGears;
		char color[20];
		float horsepower;
	};
	struct Car Car1, Car2, Car3;
	Car1.numberOfGears=6;//(.) dot is of the access of the data on a structure
	printf("%d\n",Car1.numberOfGears);
	strcpy(Car1.model,"Ford Ecosport");
	printf("%s\n",Car1.model);
	union Car4{ //Union to store and collect different types of  and uses amount of memory of the largest type of data ex 25 and only one mumber at the time
		//members
		char model[25];
		int modelNumber;
		int numberOfGears;
		char color[20];
		float horsepower;
	};
	union Car4 Car5;
	Car5.numberOfGears=10;//(.) dot is of the access of the data on a structure
	printf("%d\n",Car5.numberOfGears);
	strcpy(Car5.model,"Ford Ecosport");
	printf("%d\n",Car5.numberOfGears);//trying to access two members at one time , this number gererated by the compiler
	printf("%d\n",STATES);
	printf("%f\n",IP);
	printf("%s\n",meme);
	int input;
	int minus;
	printf("Switch section\n");
	printf("1. Plus\n");
	printf("2. Minus\n");
	printf("3. Exit\n");
	printf(" Selection: ");
	scanf("%d",&input);
	printf("\n");
	switch (input) { 
	//switch statements are also used when we need our program to make a certain decision based on a condition and then execute accordingly.
		case 1://Plus case
			printf("Give a number\n");
			scanf("%d",&a);
			printf("Give a number again\n");
			scanf("%d",&b);
			plus=a+b;
			printf("The result is:%d\n",plus);
			break;
		case 2://Minus case
			printf("Give a number\n");
			scanf("%d",&a);
			printf("Give a number again\n");
			scanf("%d",&b);
			minus=a-b;
			printf("The result is:%d\n",minus);
			break;
		case 3://Exit case
			printf("OK!\n");
			break;
		default://Else case
		printf("Bad input, quitting!\n");
		break;	
	}
	//int numb = malloc(12);  //memory function to allocates numb memory of 12 bytes and returns numb pointer which is stored in numb
	//printf("%d\n",numb);
	/*calloc is the same of the malloc function but calloc is also used to allocate memory to arrays and structures and return a pointer to the first memory location.
	It takes two arguments.The number of elements in array and size of each element in the array.*/
	//calloc(num,size);
	//calloc() is used in cases where we don't know the size of the array and want to allocate memory dynamically.
	//calloc(12,2);//passing 12 as the number of the elements and 2 as the size of each element.
	// free() is used to free or release the memory.As we are manually allocating memory, it is a good practice to remove it once it is not required.
	// free(variableName); or free(num);
	// realloc() is used to resize the memory already allocated to a variable
	// realloc(num,size); is similar syntax to calloc() and realloc() will assign a new location with new block size.
	// to perform any operation on the file, we first need to open that file.Use fopen() function.if the file isn't found ,it creates a new file.
	/* The fopen() function takes in two parameters- name of the file and mode of opening.
	 r - read mode, w - write mode or overwrite, a- append mode It searches for the last character in the file and starts writing from there.
	  r+ -read +write mode, w+ - write +read mode if the file exists,its content is overwritten.
	  a+ -read + write mode the same with a but starts from the last character reading or writing */
	// fopen("file_name","mode"); 
	//FILE *f; //is a pointer file whic contains information about the file, its name, current position and whether the file is being read or written
	//f=fopen("programming.txt","r");
	//fgetc(FILE *f); this function reads only one character at a time.it will read the character to which FILE pointer points.
	/*fgets(char buffer, n, FILE *f); this function reads a stream of characters.
	It reads from the character pointed by f to n-1 characters and it stores the read stream into buffer.
	If it encounters the end of file or a line break, it stops reading the file there*/
	/*fscanf(FILE *f,format,buffer); -This function is also used to read strings from a file.
	Where pointer points to the first character,format specifies the type of data we are reading, %s in most cases,and buffer stores the read string.
	If fscanf() encounters a space it stops reading.*/
	//char buffer[120];
	//f=fopen("programming.txt","r");
	//fgets(buffer,120,f);//Here we used fgets(), similary fscanf() and fgetc() can also be used.
	//fputc(data, FILE *f); -This function writes one character at a time.It writes the character in data to the position as poined by f.
	//fputs(data, FILE *f); -This function writes a string to the file.It writes the string in data to the position as pointed by f.
	/*f=fopen("programming.txt","w");
	//fgets("Hey! Let's write something here.",f);*/
	/*fclose(FILE *f); takes in only one arguement,that is the file pointer variable.*/
	//fclose(f);
	double miles,kms; //Conversion miles into kilometers
	printf("Give the distance in miles> "); 
	scanf("%lf",&miles);
	kms = KMS_PER_MILE * miles;
	printf("This match in %f kilometers.\n",kms);
	//reduction of int to double and the opposite
	int num_students;
	int total_score;
	printf("Give the number of the students who complete the test> ");
	scanf("%d",&num_students);
	printf("Give the total score of the students> ");
	scanf("%d",&total_score);
	double average;
	average =(double)total_score / (double) num_students;
	printf("The Average is %lf.\n",average);
	double x; 
	printf("Give a number to convert into integer>");
	scanf("%lf",&x);
	int rounded_x;
	rounded_x=(int)(x+0.5);
	printf("The rounded-x is %d.\n",rounded_x);
	char qmark_code;
	qmark_code =(int)'?';
	printf("Code for '?' = %d\n",qmark_code);
	int selection;
	printf("Select:\n");
	printf("1. >>Create a random number\n");
	printf("2. >>Give the number you want\n");
	printf("Selection>>");
	scanf("%d",&selection);
	int random_number = rand();
	int your_number;
	switch (selection){
		case 1:
  		printf("The random number is %d\n", random_number);
  		break;
		case 2:
			printf("Your number>>");
			scanf("%d",&your_number);
			break;
		default:
			printf("Wrong input. Quitting!!!\n");
			break;
	}
	char *fullname= "Biazis Panagiotis";
    char *birthdate="04/05/2003";
    char *city="Athens";
    char *specialisation="Technical Engineer";
    printf("Full name: %s\n",fullname);
    printf("Birthdate: %s\n",birthdate);
    printf("The city where you born: %s\n",city);
    printf("Your specialisation: %s\n",specialisation);
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("[\t\t\t\t\t\t\t\t\t\t]\n");
    printf("\n");
    printf("\n");
    printf("\n");
    myfunction();
    colourfulF();
    for (int i=0;i<5;i++){
    face1();
}
int times;
printf("How many times you want to print the name PANOS?\n");
printf("Times:");
scanf("%d",&times);
name_PANOS_F(times);
printf("\a");
system("pause");
for (int i = 0; i < 5; i++) {
        // delay of one second
        delay(100);
        printf("%d seconds have passed\n", i + 1);
    }
frameSpace(50);
system("pause");
printf("\a\n");
printf("\033[0;31m");
char something[100];
printf("Write something:");
scanf("%s",&something);
printf("%s",something);
printf("\033[0m\n");
printf("\033[0;32m");
char something2[100];
printf("Write something again:");
scanf("%s",&something2);
printf("%s",something2);
printf("\033[0m\n");
int default1=0;
Main_Menu(default1);
division:;
float diereteos,dieretis,apotelesma;
printf("Dwse ton diereteo:");
scanf("%f",&diereteos);
printf("Dwse ton diereti:");
scanf("%f",&dieretis);
if(dieretis==0){
	printf("Einai adinath\a\n");
	printf("Try again\n");
	goto division;
}
else{
	apotelesma=diereteos / dieretis;
	printf("To piliko einai:%.4f\n",apotelesma);
}
int myNumber3=10;
if(myNumber3>10){
printf("That's bad!!!\n\a");
}
else if(myNumber3==10){
printf("Now we're talking\n");
}
else {
printf("This is really bad!!\a\n");
}
division2:;
int diereteos2,dieretis2,apotelesma2;
printf("Dwse ton diereteo:");
scanf("%d",&diereteos2);
printf("Dwse ton diereti:");
scanf("%d",&dieretis2);
if(dieretis2==0){
	printf("Einai adinath\a\n");
	printf("Try again\n");
	goto division2;
}
else{
	apotelesma2=diereteos2 % dieretis2;
	printf("To ypolipo einai:%d\n",apotelesma2);
}
enum days_of_week day2;
enum days_of_week day[10];
char One_day[10];
printf("Write the day you want like(Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday):");
scanf("%s",&One_day);
day[10]=One_day[10];
printf("%10s\n",day);
day2=Monday;
printf("%d\n",day2);
for (int i=Jan; i<=Dec; i++) {
      printf("%d ", i);
  }
printf("\n");
//volatile data_type variable_name;
const volatile int prepBuddy = 125; //is just a qualifier used by the programmer when declaring a variable in source code. It tells the compiler that the variable value can be modified at any point without needing any task from the source code.
int *ptr = ( int* ) &prepBuddy;
printf("The initial value of the prepBuddy is  : %d\n", prepBuddy);
*ptr = 251; 
printf("The modified value of the prepBuddy is : %d\n", prepBuddy);
return 0;
}
