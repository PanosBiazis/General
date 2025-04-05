#include <stdio.h>
#include <string.h>

#define MAX_PASSWORD_LENGTH 100
#define CORRECT_PASSWORD "0"

int main() {
    int choice;
    char password[MAX_PASSWORD_LENGTH];

    do {
        printf("Enter your password: ");
        scanf("%99s", password); // use %99s to prevent buffer overflow

        if (strcmp(password, CORRECT_PASSWORD) == 0) {
            printf("You remember your password!!!\n");

            printf("Would you like to try again?\n");
            printf("1. Yes\n");
            printf("2. No\n");
            printf("Enter your choice: ");
            scanf("%d", &choice);

            if (choice != 1 && choice != 2) {
                printf("Wrong choice!!!\nTry Again!!!\n");
                continue;
            }
        } else {
            printf("Wrong password!!!\nTry Again!!!\n");
            continue;
        }
    } while (choice == 1);

    return 0;
}