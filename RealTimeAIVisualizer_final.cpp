#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <sqlite3.h>
#include </dlib-master/dlib-master/dlib/mlp.h>
#include "/civetweb/include/civetweb.h"

// Assuming training_sample_type and training_label_type are matrices from dlib
typedef matrix<double, 1, 1> training_sample_type;  // A row vector with 1 element
typedef double training_label_type;

using namespace dlib;

// Function to create the database and tables
void createDatabase() {
    sqlite3 *db;
    char *errMsg = 0;

    int rc = sqlite3_open("test.db", &db);
    if (rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    const char *sql1 = "CREATE TABLE IF NOT EXISTS RandomNumbers("
                       "ID INT PRIMARY KEY NOT NULL,"
                       "NUMBER REAL NOT NULL);";

    const char *sql2 = "CREATE TABLE IF NOT EXISTS AIResults("
                       "ID INT PRIMARY KEY NOT NULL,"
                       "RESULT REAL NOT NULL);";

    sqlite3_exec(db, sql1, 0, 0, &errMsg);
    sqlite3_exec(db, sql2, 0, 0, &errMsg);

    sqlite3_close(db);
}

// Function to insert random numbers into the database
void insertRandomNumbers(int count) {
    sqlite3 *db;
    char *errMsg = 0;
    int rc = sqlite3_open("test.db", &db);

    srand(static_cast<unsigned int>(time(0)));

    for (int i = 0; i < count; ++i) {
        double randomNumber = static_cast<double>(std::rand()) / RAND_MAX;
        std::string sql = "INSERT INTO RandomNumbers (ID, NUMBER) VALUES (" + 
                          std::to_string(i + 1) + ", " + 
                          std::to_string(randomNumber) + ");";

        char *errMsg = 0;
    sqlite3_exec(db, sql.c_str(), 0, 0, &errMsg);
    }

    sqlite3_close(db);
}

// Function to train AI model and store results
void trainAIModel() {
    sqlite3 *db;
    sqlite3_open("test.db", &db);
    sqlite3_stmt *stmt;

    std::vector<double> numbers;
    std::string sql = "SELECT NUMBER FROM RandomNumbers";

    sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, 0);
    while (sqlite3_step(stmt) == SQLITE_ROW) {
        numbers.push_back(sqlite3_column_double(stmt, 0));
    }

    sqlite3_finalize(stmt);
    sqlite3_close(db);

    // Setup the MLP network
    mlp::kernel_1a_c net(1, 5, 1);
    std::vector<training_sample_type> samples;
    std::vector<training_label_type> labels;
    std::vector<training_label_type> labels;

    for (double num : numbers) {
        training_sample_type sample;
        sample(0) = num;
        samples.push_back(sample);
        labels.push_back(num * num);  // For simplicity, using square as label
    }

    net.set_learning_rate(0.1);
    net.set_minimum_iterations_without_progress(200);
    net.train(samples, labels);

    sqlite3_open("test.db", &db);

    for (size_t i = 0; i < samples.size(); ++i) {
        double result = net(samples[i]);
        std::string sql = "INSERT INTO AIResults (ID, RESULT) VALUES (" +
                          std::to_string(i + 1) + ", " +
                          std::to_string(result) + ");";
        char *errMsg = 0;
    sqlite3_exec(db, sql.c_str(), 0, 0, &errMsg);
    }

    sqlite3_close(db);
}

// HTTP callback for CivetWeb server to serve AI results
int handle_request(struct mg_connection *conn, void *ignored) {
    sqlite3 *db;
    sqlite3_stmt *stmt;

    sqlite3_open("test.db", &db);

    std::string content = "[";
    std::string sql = "SELECT RESULT FROM AIResults";
    sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, 0);

    while (sqlite3_step(stmt) == SQLITE_ROW) {
        content += std::to_string(sqlite3_column_double(stmt, 0)) + ",";
    }

    content.pop_back();  // Remove trailing comma
    content += "]";

    sqlite3_finalize(stmt);
    sqlite3_close(db);

    mg_printf(conn, "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n");
    mg_printf(conn, "%s", content.c_str());

    return 200;
}

int main() {
    createDatabase();
    insertRandomNumbers(100);
    trainAIModel();

    const char *options[] = {"document_root", ".", "listening_ports", "8080", nullptr};
    struct mg_callbacks callbacks;
    memset(&callbacks, 0, sizeof(callbacks));

    struct mg_context *ctx = mg_start(&callbacks, 0, options);
    mg_set_request_handler(ctx, "/results", handle_request, 0);

    std::cout << "Server started on port 8080. Open http://localhost:8080 in your browser." << std::endl;
    getchar();  // Wait until user hits "Enter"

    mg_stop(ctx);
    return 0;
}
