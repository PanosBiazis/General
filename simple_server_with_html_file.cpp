#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

const int PORT = 8080;
const int BUFFER_SIZE = 1024;
const std::string HTML_FILE_PATH = "./index.html"; // Specify the path to your HTML file

std::string readHtmlFile(const std::string& filePath) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        return "<html><body><h1>404 Not Found</h1></body></html>"; // Return 404 if file not found
    }

    std::stringstream buffer;
    buffer << file.rdbuf(); // Read the file into a string buffer
    return buffer.str();
}

void handleClient(SOCKET clientSocket) {
    char buffer[BUFFER_SIZE];
    std::memset(buffer, 0, BUFFER_SIZE);

    // Read the client's request
    int bytesReceived = recv(clientSocket, buffer, BUFFER_SIZE - 1, 0);
    if (bytesReceived > 0) {
        std::cout << "Received request:\n" << buffer << std::endl;

        // Read the HTML file
        std::string htmlContent = readHtmlFile(HTML_FILE_PATH);

        // Form the HTTP response
        std::string httpResponse =
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Content-Length: " + std::to_string(htmlContent.size()) + "\r\n"
            "Connection: close\r\n"
            "\r\n" + htmlContent;

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
// How This Works:
// readHtmlFile Function:

// This function reads the content of the HTML file specified by HTML_FILE_PATH and returns it as a string. If the file is not found, it returns a simple "404 Not Found" HTML page.
// Handling the Client Request:

// When a client connects, the server reads the HTML file using readHtmlFile() and sends the content back as the HTTP response.
// The response includes headers like Content-Type, Content-Length, and Connection, followed by the actual HTML content.
// HTML File Path:

// You can specify the path to your HTML file in the HTML_FILE_PATH variable. For example, you could place an index.html file in the same directory as your C++ code or provide a full path.