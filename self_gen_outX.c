#include <stdio.h>
#include <stdlib.h>
#include <conio.h> // For getch()

void generate_code(int times) {
    const char *code = "#include <stdio.h>%c#include <stdlib.h>%c#include <conio.h> // For getch()%c%cvoid generate_code(int times) {%c    const char *code = %c%s%c;%c    for (int i = 1; i <= times; i++) {%c        char filename[50];%c        sprintf(filename, %cself_generating_%%d.c%c, i);%c        FILE *fp = fopen(filename, %cw%c);%c        if (fp == NULL) {%c            perror(%cCould not create file%c);%c            return;%c        }%c        fprintf(fp, code, 10, 10, 10, 10, 10, 34, code, 34, 10, 10, 10, 34, 34, 34, 34, 119, 10, 34, 34, 10, 10);%c        fclose(fp);%c        printf(%cGenerated: %%s\\n%c, filename);%c    }%c}%c%cint main() {%c    int times;%c    printf(%cEnter the number of times to generate the code: %c);%c    scanf(%c%%d%c, &times);%c%c    generate_code(times);%c%c    printf(%cPress ESC to exit the program.\\n%c);%c    while (1) {%c        if (_kbhit()) {%c            int ch = _getch();%c            if (ch == 27) { // 27 is the ASCII code for ESC%c                printf(%cExiting...\\n%c);%c                break;%c            }%c        }%c    }%c%c    return 0;%c}";

    for (int i = 1; i <= times; i++) {
        char filename[50];
        sprintf(filename, "self_generating_%d.c", i);
        FILE *fp = fopen(filename, "w");
        if (fp == NULL) {
            perror("Could not create file");
            return;
        }
        fprintf(fp, code, 10, 10, 10, 10, 10, 34, code, 34, 10, 10, 10, 34, 34, 34, 34, 119, 10, 34, 34, 10, 10);
        fclose(fp);
        printf("Generated: %s\n", filename);
    }
}

int main() {
    int times;
    printf("Enter the number of times to generate the code: ");
    scanf("%d", &times);

    generate_code(times);

    printf("Press ESC to exit the program.\n");
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
