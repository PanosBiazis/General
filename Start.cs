public class Program
{
    static void Main()
    {
        DatabaseOperations dbOps = new DatabaseOperations();
        dbOps.CreateDatabase();

        // Insert a random number into the database
        Random random = new Random();
        double randomNumber = random.NextDouble();
        dbOps.InsertRandomNumber(randomNumber);

        // Perform AI operation and store the result
        AIOperations aiOps = new AIOperations();
        double aiResult = aiOps.PerformAICalculation(randomNumber);
        dbOps.InsertAIResult(aiResult);

        // Start a simple web server
        SimpleWebServer webServer = new SimpleWebServer(new string[] { "http://localhost:8080/" });
        webServer.Start();
    }
}
