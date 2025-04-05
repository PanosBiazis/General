#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAX_PASSWORD_LENGTH 256

char *generatePassword(int length) {
    const char characters[] = 
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*()-_=+[]{}|;:,.<>?";

    // Ensure length is within bounds
    if (length <= 0) {
        return NULL;
    }

    // Allocate memory for the password
    char *password = (char *)malloc((length + 1) * sizeof(char));
    if (password == NULL) {
        printf("Memory allocation failed.\n");
        exit(1);
    }

    // Seed the random number generator
    srand((unsigned int)time(NULL));

    // Generate the password
    for (int i = 0; i < length; ++i) {
        password[i] = characters[rand() % (sizeof(characters) - 1)];
    }

    // Null-terminate the password string
    password[length] = '\0';

    return password;
}

void savePasswordToFile(const char *password, const char *filename) {
    FILE *file = fopen(filename, "a"); // Append mode

    if (file != NULL) {
        fprintf(file, "%s\n", password);
        fclose(file);
    } else {
        printf("Unable to open file: %s\n", filename);
    }
}

int main() {
    int passwordLength;
    char filename[MAX_PASSWORD_LENGTH];

    printf("Enter the desired password length: ");
    scanf("%d", &passwordLength);

    if (passwordLength < 1) {
        printf("Password length must be greater than 0.\n");
        return 1;
    }

    printf("Enter the filename to save the password: ");
    scanf("%s", filename);

    char *password = generatePassword(passwordLength);
    if (password != NULL) {
        printf("Generated Password: %s\n", password);
        savePasswordToFile(password, filename);
        printf("Password saved to file: %s\n", filename);

        free(password); // Free the allocated memory
    } else {
        printf("Failed to generate password.\n");
    }

    return 0;
}
