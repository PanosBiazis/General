// #include <iostream>
// #include <vector>
// #include </dlib-master/dlib-master/dlib/matrix.h>
// #include </dlib-master/dlib-master/dlib/mlp.h>
// #include <sqlite3.h>

// // Typedefs for convenience
// typedef dlib::matrix<double, 1, 1> training_sample_type;  // A row vector with 1 element
// typedef double training_label_type;

// void trainAIModel() {
//     std::vector<training_sample_type> samples;
//     std::vector<training_label_type> labels;

//     // Sample data preparation
//     for (int num = 0; num < 10; ++num) {
//         training_sample_type sample;
//         sample(0, 0) = num;  // Accessing the matrix element (0,0) because it's 1x1
//         samples.push_back(sample);
//         labels.push_back(num * num);  // Example label: the square of the number
//     }

//     // Initialize the neural network
//     dlib::mlp::kernel_1a_c net(1, 5, 1);  // 1 input, 5 hidden neurons, 1 output
//     net.set_learning_rate(0.1);
//     net.set_minimum_iterations_without_progress(200);
//     net.train(samples, labels);

//     // Displaying results
//     for (size_t i = 0; i < samples.size(); ++i) {
//         double result = net(samples[i])(0, 0);  // Properly using the dlib::matrix result
//         std::cout << "Input: " << samples[i](0, 0) << " -> Prediction: " << result << "\n";
//     }

//     // Database interaction example
//     sqlite3 *db;
//     char *errMsg = 0;
//     int rc = sqlite3_open("test.db", &db);
    
//     if (rc) {
//         std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
//     } else {
//         std::cout << "Opened database successfully\n";
//     }

//     std::string sql = "CREATE TABLE IF NOT EXISTS RESULTS("
//                       "ID INT PRIMARY KEY NOT NULL,"
//                       "INPUT REAL NOT NULL,"
//                       "PREDICTION REAL NOT NULL);";
    
//     rc = sqlite3_exec(db, sql.c_str(), 0, 0, &errMsg);
//     if (rc != SQLITE_OK) {
//         std::cerr << "SQL error: " << errMsg << std::endl;
//         sqlite3_free(errMsg);
//     } else {
//         std::cout << "Table created successfully\n";
//     }

//     // Inserting results into the database
//     for (size_t i = 0; i < samples.size(); ++i) {
//         sql = "INSERT INTO RESULTS (ID, INPUT, PREDICTION) VALUES (" +
//               std::to_string(i) + ", " +
//               std::to_string(samples[i](0, 0)) + ", " +
//               std::to_string(net(samples[i])(0, 0)) + ");";
//         rc = sqlite3_exec(db, sql.c_str(), 0, 0, &errMsg);
//         if (rc != SQLITE_OK) {
//             std::cerr << "SQL error: " << errMsg << std::endl;
//             sqlite3_free(errMsg);
//         } else {
//             std::cout << "Record inserted successfully\n";
//         }
//     }

//     sqlite3_close(db);
// }

// int main() {
//     trainAIModel();
//     return 0;
// }



#include <iostream>
#include <vector>
#include "dlib/matrix.h"
#include "dlib/mlp.h"
#include <sqlite3.h>

// // Typedefs for convenience
// typedef dlib::matrix<double> sample_type;  // A dynamic matrix
// typedef double label_type;

// void trainAIModel() {
//     std::vector<sample_type> samples;
//     std::vector<label_type> labels;

//     // Sample data preparation
//     for (int num = 0; num < 10; ++num) {
//         sample_type sample(1,1);
//         sample(0, 0) = num;  // Accessing the matrix element (0,0) because it's 1x1
//         samples.push_back(sample);
//         labels.push_back(num * num);  // Example label: the square of the number
//     }

//     // Convert vectors to dlib matrices for training
//     dlib::matrix<double> sample_matrix(samples.size(), 1);
//     dlib::matrix<double> label_matrix(labels.size(), 1);

//     for (size_t i = 0; i < samples.size(); ++i) {
//         sample_matrix(i, 0) = samples[i](0, 0);
//         label_matrix(i, 0) = labels[i];
//     }

//     // Initialize the neural network
//     dlib::mlp::kernel_1a_c net(1, 5, 1);  // 1 input, 5 hidden neurons, 1 output
//     net.train(sample_matrix, label_matrix);

//     // Displaying results
//     for (size_t i = 0; i < samples.size(); ++i) {
//         double result = net(sample_matrix(i, 0));
//         std::cout << "Input: " << samples[i](0, 0) << " -> Prediction: " << result << "\n";
//     }

//     // Database interaction example
//     sqlite3 *db;
//     char *errMsg = 0;
//     int rc = sqlite3_open("test.db", &db);
    
//     if (rc) {
//         std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
//     } else {
//         std::cout << "Opened database successfully\n";
//     }

//     std::string sql = "CREATE TABLE IF NOT EXISTS RESULTS("
//                       "ID INT PRIMARY KEY NOT NULL,"
//                       "INPUT REAL NOT NULL,"
//                       "PREDICTION REAL NOT NULL);";
    
//     rc = sqlite3_exec(db, sql.c_str(), 0, 0, &errMsg);
//     if (rc != SQLITE_OK) {
//         std::cerr << "SQL error: " << errMsg << std::endl;
//         sqlite3_free(errMsg);
//     } else {
//         std::cout << "Table created successfully\n";
//     }

//     // Inserting results into the database
//     for (size_t i = 0; i < samples.size(); ++i) {
//         sql = "INSERT INTO RESULTS (ID, INPUT, PREDICTION) VALUES (" +
//               std::to_string(i) + ", " +
//               std::to_string(samples[i](0, 0)) + ", " +
//               std::to_string(net(sample_matrix(i, 0))) + ");";
//         rc = sqlite3_exec(db, sql.c_str(), 0, 0, &errMsg);
//         if (rc != SQLITE_OK) {
//             std::cerr << "SQL error: " << errMsg << std::endl;
//             sqlite3_free(errMsg);
//         } else {
//             std::cout << "Record inserted successfully\n";
//         }
//     }

//     sqlite3_close(db);
// }

// int main() {
//     trainAIModel();
//     return 0;
// }




// Typedefs for convenience
typedef dlib::matrix<double> sample_type;  // A dynamic matrix
typedef double label_type;

void trainAIModel() {
    std::vector<sample_type> samples;
    std::vector<label_type> labels;

    // Sample data preparation
    for (int num = 0; num < 10; ++num) {
        sample_type sample(1,1);
        sample(0, 0) = num;  // Accessing the matrix element (0,0) because it's 1x1
        samples.push_back(sample);
        labels.push_back(num * num);  // Example label: the square of the number
    }

    // Convert vectors to dlib matrices for training
    dlib::matrix<double> sample_matrix(samples.size(), 1);
    dlib::matrix<double> label_matrix(labels.size(), 1);

    for (size_t i = 0; i < samples.size(); ++i) {
        sample_matrix(i, 0) = samples[i](0, 0);
        label_matrix(i, 0) = labels[i];
    }

    // Initialize the neural network
    dlib::mlp::kernel_1a_c net(1, 5, 1);  // 1 input, 5 hidden neurons, 1 output
    net.train(sample_matrix, label_matrix);

    // Displaying results
    for (size_t i = 0; i < samples.size(); ++i) {
        // Wrap input into a matrix for prediction
        sample_type input(1,1);
        input(0, 0) = samples[i](0, 0);

        double result = net(input)(0, 0);  // Extracting the scalar prediction from the matrix
        std::cout << "Input: " << samples[i](0, 0) << " -> Prediction: " << result << "\n";
    }

    // Database interaction example
    sqlite3 *db;
    char *errMsg = 0;
    int rc = sqlite3_open("test.db", &db);
    
    if (rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
    } else {
        std::cout << "Opened database successfully\n";
    }

    std::string sql = "CREATE TABLE IF NOT EXISTS RESULTS("
                      "ID INT PRIMARY KEY NOT NULL,"
                      "INPUT REAL NOT NULL,"
                      "PREDICTION REAL NOT NULL);";
    
    rc = sqlite3_exec(db, sql.c_str(), 0, 0, &errMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
    } else {
        std::cout << "Table created successfully\n";
    }

    // Inserting results into the database
    for (size_t i = 0; i < samples.size(); ++i) {
        // Wrap input into a matrix for prediction
        sample_type input(1,1);
        input(0, 0) = samples[i](0, 0);

        double prediction = net(input)(0, 0);  // Extracting the scalar prediction from the matrix

        sql = "INSERT INTO RESULTS (ID, INPUT, PREDICTION) VALUES (" +
              std::to_string(i) + ", " +
              std::to_string(samples[i](0, 0)) + ", " +
              std::to_string(prediction) + ");";

        rc = sqlite3_exec(db, sql.c_str(), 0, 0, &errMsg);
        if (rc != SQLITE_OK) {
            std::cerr << "SQL error: " << errMsg << std::endl;
            sqlite3_free(errMsg);
        } else {
            std::cout << "Record inserted successfully\n";
        }
    }

    sqlite3_close(db);
}

int main() {
    trainAIModel();
    return 0;
}
