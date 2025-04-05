#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <direct.h> // For chdir(), getcwd() on Windows
#include <windows.h> // For CreateProcess(), WaitForSingleObject()

#define MAX_INPUT 1024

void execute_command(char *command) {
    char *args[MAX_INPUT / 2 + 1];
    int i = 0;

    // Tokenize the command
    args[i] = strtok(command, " \n");
    while (args[i] != NULL) {
        i++;
        args[i] = strtok(NULL, " \n");
    }

    // Handle built-in commands
    if (args[0] == NULL) {
        return;
    } else if (strcmp(args[0], "cd") == 0) {
        if (args[1] == NULL) {
            fprintf(stderr, "cd: expected argument\n");
        } else {
            if (_chdir(args[1]) != 0) {
                perror("cd failed");
            }
        }
    } else if (strcmp(args[0], "exit") == 0) {
        exit(0);
    } else {
        // Execute external commands
        STARTUPINFO si;
        PROCESS_INFORMATION pi;
        
        ZeroMemory(&si, sizeof(si));
        si.cb = sizeof(si);
        ZeroMemory(&pi, sizeof(pi));

        // Create the process
        if (!CreateProcess(NULL, command, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi)) {
            fprintf(stderr, "CreateProcess failed (%d).\n", GetLastError());
        } else {
            // Wait until the process exits
            WaitForSingleObject(pi.hProcess, INFINITE);
            CloseHandle(pi.hProcess);
            CloseHandle(pi.hThread);
        }
    }
}

int main() {
    char input[MAX_INPUT];
    char cwd[MAX_PATH];

    while (1) {
        // Get the current working directory
        if (_getcwd(cwd, sizeof(cwd)) != NULL) {
            printf("%s> ", cwd);
        } else {
            perror("getcwd error");
        }

        // Read input
        if (fgets(input, sizeof(input), stdin) == NULL) {
            break;
        }

        // Execute the command
        execute_command(input);
    }

    return 0;
}
