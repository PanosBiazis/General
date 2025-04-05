// #include <stdio.h>
// #include <stdlib.h>
// #include <ctype.h>

// #define KEY 3 // Adjust the key as needed

// void encrypt(char *text) {
//     for (int i = 0; text[i] != '\0'; ++i) {
//         if (isalpha(text[i])) {
//             if (isupper(text[i])) {
//                 text[i] = (text[i] - 'A' + KEY) % 26 + 'A';
//             } else {
//                 text[i] = (text[i] - 'a' + KEY) % 26 + 'a';
//             }
//         }
//     }
// }


// void decrypt(char *text) {
//     for (int i = 0; text[i] != '\0'; ++i) {
//         if (isalpha(text[i])) {
//             if (isupper(text[i])) {
//                 text[i] = (text[i] - KEY - 'A' + 26) % 26 + 'A';
//             } else {
//                 text[i] = (text[i] - KEY - 'a' + 26) % 26 + 'a';
//             }
//         } else {
//             // Handle non-alphabetic characters (e.g., leave them unchanged)
//         }
//     }
// }




// int main() {

// int flag = 1;

// char text[100];

// char text2[100];

// int choice;


// while(flag == 1){
    
//     start:;
    
//     printf("1.Encrypt text\n");
    
//     printf("2.Decrypt text\n");
    
//     printf("3.Exit\n");
    
//     printf("Enter your choice: ");
    
//     scanf("%d",&choice);
    
//     switch(choice){
    
//         case 1: 

//             printf("Enter text to encrypt: ");
  
//             fgets(text, sizeof(text), stdin);

//             encrypt(text);

//             printf("Encrypted text: %s\n", text);
            
//             break;
        
//         case 2:

//             printf("Enter encrypted text: ");
    
//             fgets(text2, sizeof(text2), stdin);

//             decrypt(text2);

//             printf("Decrypted text: %s\n", text2);
            
//             break;
       
//         case 3:
       
//             flag--;
       
//             break;
       
//         default:
       
//             printf("Invalid choice\n");
       
//             goto start;
    
//     }
//     // if(choice == 3){
//     //     flag--;
//     // }

// }
// return 0;

// }





// #include <stdio.h>
// #include <stdlib.h>
// #include <ctype.h>
// #include <string.h>

// #define KEY 3 // Adjust the key as needed

// void encrypt(char *text) {
//     for (int i = 0; text[i] != '\0'; ++i) {
//         if (isalpha(text[i])) {
//             if (isupper(text[i])) {
//                 text[i] = (text[i] - 'A' + KEY) % 26 + 'A';
//             } else {
//                 text[i] = (text[i] - 'a' + KEY) % 26 + 'a';
//             }
//         }
//     }
// }

// void decrypt(char *text) {
//     for (int i = 0; text[i] != '\0'; ++i) {
//         if (isalpha(text[i])) {
//             if (isupper(text[i])) {
//                 text[i] = (text[i] - 'A' - KEY + 26) % 26 + 'A';
//             } else {
//                 text[i] = (text[i] - 'a' - KEY + 26) % 26 + 'a';
//             }
//         }
//     }
// }

// int main() {
//     int flag = 1;
//     char text[100];

//     while (flag == 1) {
//         printf("1. Encrypt text\n");
//         printf("2. Decrypt text\n");
//         printf("3. Exit\n");
//         printf("Enter your choice: ");

//         int choice;
//         if (scanf("%d", &choice) != 1) {
//             printf("Invalid input\n");
//             continue;
//         }

//         switch (choice) {
//             case 1:
//                 printf("Enter text to encrypt: ");
//                 fgets(text, sizeof(text), stdin);
//                 text[strcspn(text, "\n")] = '\0'; // Remove newline character
//                 encrypt(text);
//                 printf("Encrypted text: %s\n", text);
//                 break;

//             case 2:
//                 printf("Enter encrypted text: ");
//                 fgets(text, sizeof(text), stdin);
//                 text[strcspn(text, "\n")] = '\0'; // Remove newline character
//                 decrypt(text);
//                 printf("Decrypted text: %s\n", text);
//                 break;

//             case 3:
//                 flag--;
//                 break;

//             default:
//                 printf("Invalid choice\n");
//                 break;
//         }
//     }

//     return 0;
// }



// #include <stdio.h>
// #include <stdlib.h>
// #include <ctype.h>
// #include <string.h>

// #define KEY 3 // Adjust the key as needed

// void encrypt(char *text) {
//     for (int i = 0; text[i] != '\0'; ++i) {
//         if (isalpha(text[i])) {
//             if (isupper(text[i])) {
//                 text[i] = (text[i] - 'A' + KEY) % 26 + 'A';
//             } else {
//                 text[i] = (text[i] - 'a' + KEY) % 26 + 'a';
//             }
//         }
//     }
// }

// void decrypt(char *text) {
//     for (int i = 0; text[i] != '\0'; ++i) {
//         if (isalpha(text[i])) {
//             if (isupper(text[i])) {
//                 text[i] = (text[i] - 'A' - KEY + 26) % 26 + 'A';
//             } else {
//                 text[i] = (text[i] - 'a' - KEY + 26) % 26 + 'a';
//             }
//         }
//     }
// }

// int main() {
//     int flag = 1;
//     char text[100];

//     while (flag == 1) {
//         printf("1. Encrypt text\n");
//         printf("2. Decrypt text\n");
//         printf("3. Exit\n");
//         printf("Enter your choice: ");

//         int choice;
//         if (scanf("%d", &choice) != 1) {
//             printf("Invalid input\n");
//             while (getchar() != '\n'); // Clear input buffer
//             continue;
//         }

//         switch (choice) {
//             case 1:
//                 printf("Enter text to encrypt: ");
//                 fgets(text, sizeof(text), stdin);
//                 text[strcspn(text, "\n")] = '\0'; // Remove newline character
//                 encrypt(text);
//                 printf("Encrypted text: %s\n", text);
//                 break;

//             case 2:
//                 printf("Enter encrypted text: ");
//                 fgets(text, sizeof(text), stdin),
//                 text[strcspn(text, "\n")] = '\0'; // Remove newline character
//                 decrypt(text);
//                 printf("Decrypted text: %s\n", text);
//                 break;

//             case 3:
//                 flag--;
//                 break;

//             default:
//                 printf("Invalid choice\n");
//                 break;
//         }
//     }

//     return 0;
// }


#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define KEY 3 // Adjust the key as needed

void encrypt(char *text) {
    for (int i = 0; text[i] != '\0'; ++i) {
        if (isalpha(text[i])) {
            if (isupper(text[i])) {
                text[i] = (text[i] - 'A' + KEY) % 26 + 'A';
            } else {
                text[i] = (text[i] - 'a' + KEY) % 26 + 'a';
            }
        }
    }
}

void decrypt(char *text) {
    for (int i = 0; text[i] != '\0'; ++i) {
        if (isalpha(text[i])) {
            if (isupper(text[i])) {
                text[i] = (text[i] - 'A' - KEY + 26) % 26 + 'A';
            } else {
                text[i] = (text[i] - 'a' - KEY + 26) % 26 + 'a';
            }
        }
    }
}

int main() {
    int flag = 1;
    char text[100];

    while (flag == 1) {
        printf("1. Encrypt text\n");
        printf("2. Decrypt text\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");

        int choice;
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input\n");
            while (getchar() != '\n'); // Clear input buffer
            continue;
        }

        getchar(); // Consume the newline left in the input buffer after scanf

        switch (choice) {
            case 1:
                printf("Enter text to encrypt: ");
                fgets(text, sizeof(text), stdin);
                text[strcspn(text, "\n")] = '\0'; // Remove newline character
                encrypt(text);
                printf("Encrypted text: %s\n", text);
                break;

            case 2:
                printf("Enter encrypted text: ");
                fgets(text, sizeof(text), stdin);
                text[strcspn(text, "\n")] = '\0'; // Remove newline character
                decrypt(text);
                printf("Decrypted text: %s\n", text);
                break;

            case 3:
                flag = 0; // Set flag to 0 to exit the loop
                break;

            default:
                printf("Invalid choice\n");
                break;
        }
    }

    return 0;
}
