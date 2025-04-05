#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

#define PORT 8080
#define BUFFER_SIZE 1024
#define HTML_FILE_PATH "F:\\panag\\Documents\\website\\html\\index.html" // Specify the path to your HTML file

char *readHtmlFile(const char *filePath) {
    FILE *file = fopen(filePath, "r");
    if (!file) {
        // Return a simple 404 Not Found HTML page
        const char *notFound = "<html><body><h1>404 Not Found</h1></body></html>";
        char *response = (char *)malloc(strlen(notFound) + 1);
        if (response != NULL) {
            strcpy(response, notFound);
        }
        return response;
    }

    // Read the file into a dynamically allocated string
    fseek(file, 0, SEEK_END);
    long fileSize = ftell(file);
    fseek(file, 0, SEEK_SET);

    char *content = (char *)malloc(fileSize + 1);
    if (content == NULL) {
        fclose(file);
        return NULL;
    }

    fread(content, 1, fileSize, file);
    content[fileSize] = '\0';
    fclose(file);
    return content;
}

void handleClient(SOCKET clientSocket) {
    char buffer[BUFFER_SIZE];
    memset(buffer, 0, BUFFER_SIZE);

    // Read the client's request
    int bytesReceived = recv(clientSocket, buffer, BUFFER_SIZE - 1, 0);
    if (bytesReceived > 0) {
        printf("Received request:\n%s\n", buffer);

        // Read the HTML file
        char *htmlContent = readHtmlFile(HTML_FILE_PATH);
        if (htmlContent == NULL) {
            printf("Error reading HTML file.\n");
            return;
        }

        // Form the HTTP response
        char httpResponse[BUFFER_SIZE];
        snprintf(httpResponse, sizeof(httpResponse),
                 "HTTP/1.1 200 OK\r\n"
                 "Content-Type: text/html\r\n"
                 "Content-Length: %lu\r\n"
                 "Connection: close\r\n"
                 "\r\n%s",
                 strlen(htmlContent), htmlContent);

        // Send the HTTP response
        send(clientSocket, httpResponse, strlen(httpResponse), 0);
        free(htmlContent);
    } else {
        fprintf(stderr, "Error reading request from client.\n");
    }

    // Close the client connection
    closesocket(clientSocket);
}

int main() {
    WSADATA wsaData;
    int wsaStartupResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (wsaStartupResult != 0) {
        fprintf(stderr, "WSAStartup failed: %d\n", wsaStartupResult);
        return 1;
    }

    SOCKET serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == INVALID_SOCKET) {
        fprintf(stderr, "Failed to create socket. Error: %d\n", WSAGetLastError());
        WSACleanup();
        return 1;
    }

    struct sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = INADDR_ANY;
    serverAddress.sin_port = htons(PORT);

    // Bind the socket to the specified port
    if (bind(serverSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) == SOCKET_ERROR) {
        fprintf(stderr, "Bind failed. Error: %d\n", WSAGetLastError());
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    // Start listening for connections
    if (listen(serverSocket, 3) == SOCKET_ERROR) {
        fprintf(stderr, "Listen failed. Error: %d\n", WSAGetLastError());
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    printf("Server is listening on port %d...\n", PORT);

    while (1) {
        struct sockaddr_in clientAddress;
        int clientAddrLen = sizeof(clientAddress);

        // Accept a new connection
        SOCKET clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddress, &clientAddrLen);
        if (clientSocket == INVALID_SOCKET) {
            fprintf(stderr, "Failed to accept connection. Error: %d\n", WSAGetLastError());
            closesocket(serverSocket);
            WSACleanup();
            return 1;
        }

        // Handle the client's request
        handleClient(clientSocket);
    }

    // Close the server socket
    closesocket(serverSocket);
    WSACleanup();

    return 0;
}
