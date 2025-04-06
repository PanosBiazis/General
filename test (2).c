#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h> // Add this header for sleep function

int main() {

    struct timespec ts = {1, 0}; // 2 seconds, 0 nanoseconds

    printf("Hello, World!\nPress any key to exit");
    
    nanosleep(&ts, NULL);
    printf(".");
    
    nanosleep(&ts, NULL);
    printf(".");
    
    nanosleep(&ts, NULL);
    printf(".");
    
    // printf(".");
    
    // sleep(2);
    
    // printf(".");
    
    // system("pause");

    // sleep(3);  // Delays for 3 seconds
    // Alternative method using Windows-specific delay:
    // Sleep(3000);  // Delays for 3 seconds (Windows)
    

    getchar();
    return 0;
}
