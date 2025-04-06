// #include <math.h>
// #include <time.h>
// #include <conio.h> 
// #include <windows.h>
// #include <io.h>
#include <stdio.h>
// #include <stdlib.h>
#include <string.h>


void get_info_f(char dat[11][11], char dat2[11][11]) {
    // Get 10 strings for dat and 10 strings for dat2
    for (int l = 0; l < 10; l++) {
        printf("Give an information: ");
        fgets(&dat[l][0], 10, stdin); // + l to store the string at the correct index
        dat[l][strcspn(dat[l], "\n")] = 0; // Remove newline character
        printf("The %dth data is %s\n", l + 1, dat[l]);
    }

    for (int m = 0; m < 10; m++) {
        printf("Give another information: ");
        fgets(&dat2[m][0], 10, stdin);
        dat2[m][strcspn(dat2[m], "\n")] = 0; // Remove newline character
        printf("The %dth data2 is %s\n", m + 1, dat2[m]);
    }
}

int main() {
    char data[11][11], data2[11][11];
    get_info_f(data, data2);

    printf("Data: ");
    for (int i = 0; i < 10; i++) {
        printf("%s ", data[i]);
    }
    printf("\n");

    printf("Data2: ");
    for (int k = 0; k < 10; k++) {
        printf("%s ", data2[k]);
    }
    printf("\n");

    return 0;
}
