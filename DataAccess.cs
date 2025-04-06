// using System.Collections.Generic;
// using System.Data.SqlClient;
// using System.Linq;
// using Dapper;
// using Microsoft.ML;

// namespace ConsoleApp
// {
//     public static class DataAccess
//     {
//         // private static readonly string connectionString = "Server=localhost:5000;Database=RandomNumbersDB;Trusted_Connection=True;";
//         private static readonly string connectionString = "Server=localhost;Database=RandomNumbersDB;User Id=local;Password=local;";

        
//         public static IDataView LoadData()
//         {
//             var mlContext = new MLContext();
//             using (var connection = new SqlConnection(connectionString))
//             {
//                 connection.Open();
//                 string query = "SELECT Number FROM RandomNumbers";
//                 var data = connection.Query<float>(query)
//                     .Select(num => new NumberData { Number = num })
//                     .ToList();
//                 return mlContext.Data.LoadFromEnumerable(data);
//             }
//         }
//     }

//     public class NumberData
//     {
//         public float Number { get; set; }
//     }
// }
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using Dapper;
using Microsoft.ML;

namespace ConsoleApp
{
    public static class DataAccess
    {
        // Connection string with SQL Authentication
        private static readonly string connectionString = "Server=localhost,3306;Database=RandomNumbersDB;User Id=root;Password=;";

        public static IDataView LoadData()
        {
            var mlContext = new MLContext();
            try
            {
                using (var connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    
                    // SQL query to select numbers
                    string query = "SELECT Number FROM RandomNumbers";
                    
                    // Fetch data using Dapper
                    var data = connection.Query<float>(query)
                        .Select(num => new NumberData { Number = num })
                        .ToList();
                    
                    // Load data into ML.NET IDataView
                    return mlContext.Data.LoadFromEnumerable(data);
                }
            }
            catch (SqlException sqlEx)
            {
                Console.WriteLine($"SQL Error: {sqlEx.Message}");
                throw;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"General Error: {ex.Message}");
                throw;
            }
        }
    }

    // Class representing the data structure
    public class NumberData
    {
        public float Number { get; set; }
    }
}
