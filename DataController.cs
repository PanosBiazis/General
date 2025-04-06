using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Data.SqlClient;

namespace WebApp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class DataController : ControllerBase
    {
        [HttpGet]
        public IActionResult GetProcessedNumbers()
        {
            string connectionString = "Server=your_server;Database=RandomNumbersDB;Trusted_Connection=True;";
            var data = new List<object>();

            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                string query = "SELECT OriginalNumber, PredictedValue FROM ProcessedNumbers";
                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            data.Add(new
                            {
                                Original = reader.GetFloat(0),
                                Predicted = reader.GetFloat(1)
                            });
                        }
                    }
                }
            }

            return Ok(data);
        }
    }
}
