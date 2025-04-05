#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX_CHOICE_SIZE 100
#define MAX_num_size 100
#define MAX_num_size2 100
int choice_size = MAX_CHOICE_SIZE;

void addition(long double num,long double num2,long double result){

    char bufferf[100];
    char bufferf2[100];
    char numb[100];
    char num2b[100];


    snprintf(numb, sizeof(numb),"Write a number do you want to add>>>");
    printf("%s",numb);

    if (fgets(bufferf, sizeof(num), stdin) != NULL) {
        printf("You entered: %Lf", num);
    } else {
        printf("Error reading input\n");
    }

    snprintf(num2b, sizeof(num2b),"Write another number do you want to add>>>");
    printf("%s",num2b);

    if (fgets(bufferf2, sizeof(num2), stdin) != NULL) {
        printf("You entered: %Lf", num2);
    } else {
        printf("Error reading input\n");
    }

    result = num + num2;
    printf("The result is: %Lf",result);

}

void discapitalize(char *str) {
    int i;
    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] == '+') {
            break;
        }
        str[i] = tolower(str[i]);
    }

}

void operation(char choice[]){
    char buffer[100];
    long double num;
    long double num2;
    long double result;
    snprintf(buffer, sizeof(buffer),"Write what operation do you want to do>>>");
    printf("%s",buffer);
    // if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
    //     // Remove newline character if present
    //     buffer[strcspn(buffer, "\n")] = '\0';
    //     // Process the input
    // } else {
    //     // Handle error
    // }
    // if (fgets(choice, sizeof(choice), stdin) != NULL) {
    //     printf("You entered: %s", choice);
    // } else {
    //     printf("Error reading input\n");
    // }
    if (fgets(choice, choice_size, stdin) != NULL) {
        printf("You entered: %s", choice);
    } else {
        printf("Error reading input\n");
    }
    discapitalize(choice);
    switch(choice[100]){
        case '+' || "addition" || "add":
        addition(num,num2,result);
        break;
    }
}

void main(){
    char buffer[100];
    char choice[20];
    // snprintf(buffer, sizeof(buffer),"Write what operation do you want to do?");
    // printf("%s\n",buffer);
    operation(choice);

}