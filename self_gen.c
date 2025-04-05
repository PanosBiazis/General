#include <stdio.h>
#include <stdlib.h>
#include <conio.h> // For getch()

int main() {
    // The program source code stored in a string
    const char *code = "#include <stdio.h>%c#include <stdlib.h>%c#include <conio.h>%c%cint main() {%c    // The program source code stored in a string%c    const char *code = %c%s%c;%c%c    // Open a file to write the code to%c    FILE *fp = fopen(%cself_generating.c%c, %cw%c);%c    if (fp == NULL) {%c        perror(%cCould not create file%c);%c        return 1;%c    }%c%c    // Write the code into the file%c    fprintf(fp, code, 10, 10, 10, 10, 10, 10, 34, code, 34, 10, 10, 10, 34, 34, 34, 119, 10, 10, 34, 34, 10, 10, 10, 10);%c    fclose(fp);%c%c    // Compile the new source code%c    system(%cgcc self_generating.c -o self_generating%c);%c%c    // Execute the compiled program%c    system(%c./self_generating%c);%c%c    // Wait for ESC key to exit%c    printf(%cPress ESC to exit.%c);%c    while (1) {%c        if (_kbhit()) {%c            int ch = _getch();%c            if (ch == 27) { // 27 is the ASCII code for ESC%c                printf(%cExiting...%c);%c                break;%c            }%c        }%c    }%c%c    return 0;%c}";

    // Open a file to write the code to
    FILE *fp = fopen("self_generating.c", "w");
    if (fp == NULL) {
        perror("Could not create file");
        return 1;
    }

    // Write the code into the file
    fprintf(fp, code, 10, 10, 10, 10, 10, 10, 34, code, 34, 10, 10, 10, 34, 34, 34, 119, 10, 10, 34, 34, 10, 10, 10, 10);
    fclose(fp);

    // Compile the new source code
    system("gcc self_generating.c -o self_generating");

    // Execute the compiled program
    system("./self_generating");

    // Wait for ESC key to exit
    printf("Press ESC to exit.\n");
    while (1) {
        if (_kbhit()) {
            int ch = _getch();
            if (ch == 27) { // 27 is the ASCII code for ESC
                printf("Exiting...\n");
                break;
            }
        }
    }

    return 0;
}
