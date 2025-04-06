using System;
using System.Data.SqlClient;
using Dapper;
using Microsoft.ML;
using Microsoft.ML.Data;
using System.Linq; // For ToList() extension

namespace ConsoleApp
{
    public static class AIModel
    {
        public static ITransformer Train(IDataView data)
        {
            var mlContext = new MLContext();
            var pipeline = mlContext.Transforms.Concatenate("Features", "Number")
                .Append(mlContext.Regression.Trainers.Sdca(labelColumnName: "Label", maximumNumberOfIterations: 100));
            return pipeline.Fit(data);
        }

        public static void TestModel(ITransformer model)
        {
            var mlContext = new MLContext();
            var predictionEngine = mlContext.Model.CreatePredictionEngine<NumberData, NumberPrediction>(model);

            string connectionString = "Server=localhost,3306;Database=RandomNumbersDB;Trusted_Connection=True;";
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();

                string query = "SELECT ID, Number FROM RandomNumbers";
                var numbers = connection.Query<(int ID, float Number)>(query).ToList();

                foreach (var (ID, number) in numbers)
                {
                    var prediction = predictionEngine.Predict(new NumberData { Number = number });
                    double error = Math.Abs(prediction.PredictedValue - number);

                    string insertQuery = "INSERT INTO ProcessedNumbers (OriginalNumber, PredictedValue, Error) VALUES (@OriginalNumber, @PredictedValue, @Error)";
                    using (SqlCommand command = new SqlCommand(insertQuery, connection))
                    {
                        command.Parameters.AddWithValue("@OriginalNumber", number);
                        command.Parameters.AddWithValue("@PredictedValue", prediction.PredictedValue);
                        command.Parameters.AddWithValue("@Error", error);
                        command.ExecuteNonQuery();
                    }
                }
            }
        }
    }

    

    public class NumberPrediction
    {
        [ColumnName("Score")]
        public float PredictedValue { get; set; }
    }
}
