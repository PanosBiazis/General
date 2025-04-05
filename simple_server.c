#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>

#define PORT 8080
#define BUFFER_SIZE 1024

void handle_client(SOCKET client_socket) {
    char buffer[BUFFER_SIZE];
    int read_size;
    
    // Read the client's request
    read_size = recv(client_socket, buffer, BUFFER_SIZE, 0);
    
    if (read_size > 0) {
        // Log the request (optional)
        printf("Received request:\n%s\n", buffer);

        // Prepare the response
        const char *response =
            "HTTP/1.1 200 OK\n"
            "Content-Type: text/html\n"
            "Connection: close\n\n"
            "<html><body><h1>Hello, World!</h1></body></html>";
        
        // Send the response to the client
        send(client_socket, response, strlen(response), 0);
    }

    // Close the client socket
    closesocket(client_socket);
}

int main() {
    WSADATA wsa;
    SOCKET server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    int client_len;

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("Failed to initialize Winsock. Error Code: %d\n", WSAGetLastError());
        return 1;
    }

    // Create a socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == INVALID_SOCKET) {
        printf("Could not create socket. Error Code: %d\n", WSAGetLastError());
        return 1;
    }

    // Prepare the sockaddr_in structure
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    // Bind the socket to the port
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) == SOCKET_ERROR) {
        printf("Bind failed. Error Code: %d\n", WSAGetLastError());
        return 1;
    }

    // Listen for incoming connections
    listen(server_socket, 3);

    printf("Server listening on port %d\n", PORT);

    // Accept and handle incoming connections in a loop
    while (1) {
        client_len = sizeof(struct sockaddr_in);
        client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &client_len);
        if (client_socket == INVALID_SOCKET) {
            printf("Accept failed. Error Code: %d\n", WSAGetLastError());
            continue;
        }

        // Handle the client request in a separate function
        handle_client(client_socket);
    }

    // Close the server socket (unreachable code)
    closesocket(server_socket);
    WSACleanup();
    
    return 0;
}
// Explanation of Changes:
// Winsock Initialization and Cleanup: WSAStartup() and WSACleanup() are specific to Windows and are necessary to initialize and clean up the Winsock library.
// Socket Types: On Windows, SOCKET is used instead of the int data type for socket handles.
// Functions: The standard Linux/Unix functions (read, write, close) are replaced by Winsock equivalents (recv, send, closesocket).