#include <iostream>
#include <fstream>
#include <string>

#define FILENAME "table.txt"
#define MAX_RECORD_SIZE 256

void addRecord(const std::string& record) {
    std::ofstream file(FILENAME, std::ios::app);
    if (!file) {
        std::cerr << "Error opening file for writing" << std::endl;
        return;
    }
    file << record << std::endl;
    file.close();
}

void readRecords() {
    std::ifstream file(FILENAME);
    if (!file) {
        std::cerr << "Error opening file for reading" << std::endl;
        return;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }
    file.close();
}

int main() {
    int choice;
    std::string record;

    while (true) {
        std::cout << "\nDatabase Menu:\n";
        std::cout << "1. Add Record\n";
        std::cout << "2. Read Records\n";
        std::cout << "3. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;
        std::cin.ignore(); // Consume newline character left in buffer

        switch (choice) {
            case 1:
                std::cout << "Enter record to add: ";
                std::getline(std::cin, record);
                addRecord(record);
                std::cout << "Record added." << std::endl;
                break;
            case 2:
                std::cout << "Records in file:\n";
                readRecords();
                break;
            case 3:
                std::cout << "Exiting..." << std::endl;
                return 0;
            default:
                std::cout << "Invalid choice. Please try again." << std::endl;
        }
    }

    return 0;
}
