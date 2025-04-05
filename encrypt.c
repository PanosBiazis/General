// #include <stdio.h>
// #include <stdlib.h>
// #include <ctype.h>

// #define KEY 3 // Adjust the key as needed

// void encrypt(char *text) {
//     for (int i = 0; text[i] != '\0'; ++i) {
//         if (isalpha(text[i])) {
//             text[i] = (text[i] + KEY - 'A') % 26 + 'A';
//         }
//     }
// }

// int main() {
//     char text[100];

//     printf("Enter text: ");
//     fgets(text, sizeof(text), stdin);

//     encrypt(text);

//     printf("Encrypted text: %s\n", text);

//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

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

int main() {
    char text[100];

    printf("Enter text: ");
    fgets(text, sizeof(text), stdin);

    encrypt(text);

    printf("Encrypted text: %s\n", text);

    return 0;
}

