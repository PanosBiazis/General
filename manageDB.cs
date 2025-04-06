using System;
using System.Data.SQLite;

public class DatabaseOperations
{
    private string connectionString = "Data Source=test.db;Version=3;";

    public void CreateDatabase()
    {
        using (var connection = new SQLiteConnection(connectionString))
        {
            connection.Open();

            string createRandomNumbersTable = @"
                CREATE TABLE IF NOT EXISTS RandomNumbers (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NUMBER REAL NOT NULL
                );";

            string createAIResultsTable = @"
                CREATE TABLE IF NOT EXISTS AIResults (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    RESULT REAL NOT NULL
                );";

            using (var command = new SQLiteCommand(createRandomNumbersTable, connection))
            {
                command.ExecuteNonQuery();
            }

            using (var command = new SQLiteCommand(createAIResultsTable, connection))
            {
                command.ExecuteNonQuery();
            }
        }
    }

    public void InsertRandomNumber(double number)
    {
        using (var connection = new SQLiteConnection(connectionString))
        {
            connection.Open();

            string insertQuery = "INSERT INTO RandomNumbers (NUMBER) VALUES (@number);";
            using (var command = new SQLiteCommand(insertQuery, connection))
            {
                command.Parameters.AddWithValue("@number", number);
                command.ExecuteNonQuery();
            }
        }
    }

    public void InsertAIResult(double result)
    {
        using (var connection = new SQLiteConnection(connectionString))
        {
            connection.Open();

            string insertQuery = "INSERT INTO AIResults (RESULT) VALUES (@result);";
            using (var command = new SQLiteCommand(insertQuery, connection))
            {
                command.Parameters.AddWithValue("@result", result);
                command.ExecuteNonQuery();
            }
        }
    }
}

