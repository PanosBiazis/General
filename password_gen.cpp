#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

std::string generatePassword(int length) {
    const std::string characters = 
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*()-_=+[]{}|;:,.<>?";

    std::string password;
    for (int i = 0; i < length; ++i) {
        password += characters[rand() % characters.size()];
    }

    return password;
}

void savePasswordToFile(const std::string& password, const std::string& filename) {
    std::ofstream outfile;
    outfile.open(filename, std::ios::app); // Append mode
    if (outfile.is_open()) {
        outfile << password << std::endl;
        outfile.close();
        std::cout << "Password saved to " << filename << std::endl;
    } else {
        std::cerr << "Unable to open file: " << filename << std::endl;
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0))); // Seed random number generator

    int passwordLength;
    std::string filename;

    std::cout << "Enter the desired password length: ";
    std::cin >> passwordLength;

    if (passwordLength < 1) {
        std::cerr << "Password length must be greater than 0." << std::endl;
        return 1;
    }

    std::cout << "Enter the filename to save the password: ";
    std::cin >> filename;

    std::string password = generatePassword(passwordLength);
    std::cout << "Generated Password: " << password << std::endl;

    savePasswordToFile(password, filename);

    return 0;
}

// How the Program Works:
// Generate Password:

// The generatePassword() function generates a random password based on the provided length. It selects random characters from a predefined set that includes lowercase letters, uppercase letters, digits, and special characters.
// Save Password:

// The savePasswordToFile() function appends the generated password to the specified text file. If the file does not exist, it will be created.
// Main Function:

// The user is prompted to input the desired password length and the filename to save the password.
// The generated password is displayed and saved to the file.



// This is a C++ program that generates a random password and saves it to a file. Here's a breakdown of the code:

// Function generatePassword

// This function generates a random password of a given length. It takes an integer passwordLength as input and returns a std::string containing the generated password.

// The function uses a loop to generate each character of the password. It uses the rand() function to generate a random number between 0 and 25, which corresponds to the ASCII values of the uppercase letters A to Z. The static_cast is used to convert the int value to a char. The generated character is then appended to the password string.

// Function savePasswordToFile

// This function saves a given password to a file. It takes two inputs: password, the password to be saved, and filename, the name of the file to save it to.

// The function opens the file in append mode (std::ios::app) using an std::ofstream object. If the file is successfully opened, it writes the password to the file followed by a newline character (std::endl). It then closes the file and prints a success message to the console. If the file cannot be opened, it prints an error message to the standard error stream (std::cerr).

// Main function

// The main function is the entry point of the program. It does the following:

// Seeds the random number generator using the current time (time(0)) to ensure that the generated passwords are different each time the program is run.
// Asks the user to input the desired password length and stores it in passwordLength.
// Checks if the input password length is valid (greater than 0). If not, it prints an error message and exits with a non-zero status code.
// Asks the user to input the filename to save the password to and stores it in filename.
// Calls the generatePassword function to generate a password of the desired length and stores it in password.
// Prints the generated password to the console.
// Calls the savePasswordToFile function to save the password to the specified file.
// Returns 0 to indicate successful execution.
// In summary, this program generates a random password of a user-specified length and saves it to a user-specified file.