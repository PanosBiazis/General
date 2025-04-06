using System;
using System.Data.SqlClient;

namespace ConsoleApp
{
    public static class RandomNumberGenerator
    {
        public static void GenerateNumbers(int count)
        {
            string connectionString = "Server=localhost,3306;Database=RandomNumbersDB;Trusted_Connection=True;";
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();

                for (int i = 0; i < count; i++)
                {
                    double randomNumber = new Random().NextDouble() * 100;
                    string query = "INSERT INTO RandomNumbers (Number) VALUES (@Number)";
                    using (SqlCommand command = new SqlCommand(query, connection))
                    {
                        command.Parameters.AddWithValue("@Number", randomNumber);
                        command.ExecuteNonQuery();
                    }
                }
            }
        }
    }
}
