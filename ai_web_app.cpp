// #include "Crow/include/crow.h" // Include the Crow library for web server functionality
// #include <thread> // For threading
// #include <atomic> // For atomic variables
// #include <chrono> // For time functions
// #include <cmath>  // For AI data simulation
// #include <unistd.h>// For sleep functions
// #include <iostream> // For standard I/O
// #include <stdexcept> // For exception handling
// #include <string> // For string manipulation
// #include <cstring> // For string manipulation
// #include <csignal> // For signal handling

// // Atomic variables to store AI data, allowing safe updates across threads
// std::atomic<double> ai_data_1(0.0);
// std::atomic<double> ai_data_2(0.0);
// .
// #include <csignal>

// void signal_handler(int sig) {
//     if (sig == SIGINT || sig == SIGTSTP) {
//         // Stop the Crow server here
//         // You'll need to access the Crow app instance from here
//         // One way to do this is to make the app instance a global variable
//         // or pass it as an argument to the signal_handler function
//         app.stop();
//     }
// }



// // Simulate AI data processing in a separate thread
// void ai_worker() {
//     while (true) {
//         try {
//             // Update AI data with some dummy calculations
//             ai_data_1 = std::sin(std::chrono::system_clock::now().time_since_epoch().count() / 1e9);
//             ai_data_2 = std::cos(std::chrono::system_clock::now().time_since_epoch().count() / 1e9);
//             // Sleep for a short duration to simulate time between data updates
//             std::this_thread::sleep_for(std::chrono::milliseconds(500));
//         } catch (const std::exception& e) {
//             std::cerr << "Error in AI worker thread: " << e.what() << std::endl;
//         }
//         // // Update AI data with some dummy calculations
//         // ai_data_1 = std::sin(std::chrono::system_clock::now().time_since_epoch().count() / 1e9);
//         // ai_data_2 = std::cos(std::chrono::system_clock::now().time_since_epoch().count() / 1e9);
//         // // Sleep for a short duration to simulate time between data updates
//         // std::this_thread::sleep_for(std::chrono::milliseconds(500));
//     }
// }

// int main() {
//     try {
//         // Before your app initialization
//         char cwd[1024];
//         if (getcwd(cwd, sizeof(cwd)) != NULL) {
//             std::cout << "Current working directory: " << cwd << std::endl;
//         } else {
//             throw std::runtime_error("getcwd() error");
//         }

//         // std::string cwd_str(cwd);
//         // std::string html_file_path = cwd_str + "/index.html";
//         std::string filePath = "./index.html"; // Path to the HTML file
//         std::string html_file_path = filePath; // Path to the HTML file

//         // Load the HTML file using Crow's mustache template engine
//         // Print the current working directory
//     // char cwd[1024];
//     // if (getcwd(cwd, sizeof(cwd)) != NULL) {
//     //     std::cout << "Current working directory: " << cwd << std::endl;
//     // } else {
//     //     perror("getcwd() error");
//     // }


//         // Launch the AI data processing thread
//         std::thread ai_thread(ai_worker);
//     // // cwd = strcat(cwd, "./index.html");// Concatenate the path to the file
//     // cwd = concat(cwd, "/index.html"); // Concatenate the path to the file
//     // // Load the HTML file using Crow's mustache template engine
//     // // Print the current working directory
//     // std::cout << "Current working directory: " << cwd << std::endl;

//         // Create a Crow application instance
//         crow::SimpleApp app;
//     // // Launch the AI data processing thread
//     // std::thread ai_thread(ai_worker);

//         // Route to serve the main page
//         CROW_ROUTE(app, "/")([html_file_path]() {//mutable {
//             return crow::mustache::load(html_file_path).render();
//         });
//     // // Create a Crow application instance
//     // crow::SimpleApp app;

//         // Route to provide AI data in JSON format
//         CROW_ROUTE(app, "/data")([]() {
//             crow::json::wvalue data;
//             data["value1"] = ai_data_1.load();
//             data["value2"] = ai_data_2.load();
//             return data;
//         });
//     // // Route to serve the main page
//     // CROW_ROUTE(app, "/")([]() {
//     //     return crow::mustache::load(cwd).render();
//     // });

//     std::signal(SIGINT, signal_handler);
//     std::signal(SIGTSTP, signal_handler);
//         // Start the server on port ////8080
//         app.port(8106).multithreaded().run();
//     // // Route to provide AI data in JSON format
//     // CROW_ROUTE(app, "/data")([]() {
//     //     crow::json::wvalue data;
//     //     data["value1"] = ai_data_1.load();
//     //     data["value2"] = ai_data_2.load();
//     //     return data;
//     // });

//     // Signal handler to release the port when the server is stopped
//     // void signal_handler(int sig) {
//     //     if (sig == SIGINT || sig == SIGTSTP) {
//     //         app.stop();
//     //     }
//     // }

//     // Register the signal handler
//     std::signal(SIGINT, signal_handler);
//     std::signal(SIGTSTP, signal_handler);


//     // Ensure the AI thread continues running
//     ai_thread.join();
//     } catch (const std::exception& e) {
//         std::cerr << "Error in main: " << e.what() << std::endl;
//         return 1;
//     }    // // Start the server on port ////8080
//     // app.port(8105).multithreaded().run();
//     // // Ensure the AI thread continues running
//     // ai_thread.join();

//     return 0;
// }

#include "Crow/include/crow.h"
#include <thread>
#include <atomic>
#include <chrono>
#include <cmath>
#include <unistd.h>
#include <iostream>
#include <stdexcept>
#include <string>
#include <fstream>
#include <csignal>
#include <filesystem>

std::atomic<double> ai_data_1(0.0);
std::atomic<double> ai_data_2(0.0);
crow::SimpleApp app;

void signal_handler(int sig) {
    if (sig == SIGINT || sig == SIGTSTP) app.stop();
}

void ai_worker() {
    while (true) {
        auto now = std::chrono::system_clock::now().time_since_epoch().count() / 1e9;
        ai_data_1 = std::sin(now);
        ai_data_2 = std::cos(now);
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
}

int main() {
    try {
        char cwd[1024];
        getcwd(cwd, sizeof(cwd));
        std::cout << "CWD: " << cwd << "\n";

        // Configure template paths
        crow::mustache::set_base(".");
        std::string html_file = "templates/index.html";
        
        // Verify template path
        std::filesystem::path full_path = std::filesystem::path(cwd) / html_file;
        if (!std::filesystem::exists(full_path)) {
            std::cerr << "Template missing at: " << full_path << "\n";
            return 1;
        }

        // Start server components
        std::thread ai_thread(ai_worker);
        
        CROW_ROUTE(app, "/")([html_file](const crow::request&, crow::response& res) {
            try {
                auto tpl = crow::mustache::load(html_file);
                res.body = tpl.render().dump();
                res.end();
            } catch (const std::exception& e) {
                res.code = 500;
                res.body = "ERROR: " + std::string(e.what());
                res.end();
            }
        });

        CROW_ROUTE(app, "/data")([] {
            crow::json::wvalue data;
            data["value1"] = ai_data_1.load();
            data["value2"] = ai_data_2.load();
            return data;
        });

        std::signal(SIGINT, signal_handler);
        std::signal(SIGTSTP, signal_handler);
        
        std::cout << "Server starting on port 8106\n";
        app.port(8106).loglevel(crow::LogLevel::Warning).multithreaded().run();
        
        ai_thread.join();
    } catch (const std::exception& e) {
        std::cerr << "Fatal error: " << e.what() << "\n";
        return 1;
    }
    return 0;
}