#include <stdio.h>
#include <ctype.h>

#define KEY 3 // Adjust the key as needed

void decrypt(char *text) {
    for (int i = 0; text[i] != '\0'; ++i) {
        if (isalpha(text[i])) {
            if (isupper(text[i])) {
                text[i] = (text[i] - KEY - 'A' + 26) % 26 + 'A';
            } else {
                text[i] = (text[i] - KEY - 'a' + 26) % 26 + 'a';
            }
        } else {
            // Handle non-alphabetic characters (e.g., leave them unchanged)
        }
    }
}

int main() {
    char text[100];

    printf("Enter encrypted text: ");
    fgets(text, sizeof(text), stdin);

    decrypt(text);

    printf("Decrypted text: %s\n", text);

    return 0;
}