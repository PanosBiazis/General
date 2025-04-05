#include <iostream>
#include <string>
#include <cstring>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

const int PORT = 8080;
const int BUFFER_SIZE = 1024;

std::string httpResponse =
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html\r\n"
    "Connection: close\r\n"
    "\r\n"
    "<html><body><h1>Hello, World!</h1></body></html>";

void handleClient(SOCKET clientSocket) {
    char buffer[BUFFER_SIZE];
    std::memset(buffer, 0, BUFFER_SIZE);

    // Read the client's request
    int bytesReceived = recv(clientSocket, buffer, BUFFER_SIZE - 1, 0);
    if (bytesReceived > 0) {
        std::cout << "Received request:\n" << buffer << std::endl;

        // Send the HTTP response
        send(clientSocket, httpResponse.c_str(), httpResponse.length(), 0);
    } else {
        std::cerr << "Error reading request from client.\n";
    }

    // Close the client connection
    closesocket(clientSocket);
}

int main() {
    WSADATA wsaData;
    int wsaStartupResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (wsaStartupResult != 0) {
        std::cerr << "WSAStartup failed: " << wsaStartupResult << "\n";
        return 1;
    }

    SOCKET serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == INVALID_SOCKET) {
        std::cerr << "Failed to create socket. Error: " << WSAGetLastError() << "\n";
        WSACleanup();
        return 1;
    }

    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = INADDR_ANY;
    serverAddress.sin_port = htons(PORT);

    // Bind the socket to the specified port
    if (bind(serverSocket, (sockaddr*)&serverAddress, sizeof(serverAddress)) == SOCKET_ERROR) {
        std::cerr << "Bind failed. Error: " << WSAGetLastError() << "\n";
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    // Start listening for connections
    if (listen(serverSocket, 3) == SOCKET_ERROR) {
        std::cerr << "Listen failed. Error: " << WSAGetLastError() << "\n";
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    std::cout << "Server is listening on port " << PORT << "...\n";

    while (true) {
        sockaddr_in clientAddress;
        int clientAddrLen = sizeof(clientAddress);

        // Accept a new connection
        SOCKET clientSocket = accept(serverSocket, (sockaddr*)&clientAddress, &clientAddrLen);
        if (clientSocket == INVALID_SOCKET) {
            std::cerr << "Failed to accept connection. Error: " << WSAGetLastError() << "\n";
            closesocket(serverSocket);
            WSACleanup();
            return 1;
        }

        // Handle the client's request in a separate function
        handleClient(clientSocket);
    }

    // Close the server socket
    closesocket(serverSocket);
    WSACleanup();

    return 0;
}
// Explanation of Changes:
// Windows Sockets API (Winsock):

// Included <winsock2.h> and <ws2tcpip.h>, which are required for network programming on Windows.
// Used WSAStartup() to initialize the Winsock library and WSACleanup() to clean up when done.
// Replaced Unix socket functions (like close()) with their Winsock equivalents (like closesocket()).
// Used #pragma comment(lib, "ws2_32.lib") to link against the Winsock library.
// Handling Socket Operations:

// Replaced Unix socket operations (like read() and write()) with their Winsock equivalents (recv() and send()).