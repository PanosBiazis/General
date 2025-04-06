using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;

class SimpleWebServer
{
    private const int PORT = 8080;
    private const int BUFFER_SIZE = 1024;
    private const string HTML_FILE_PATH = "F:\\panag\\Documents\\website\\html\\index.html"; // Specify the path to your HTML file

    public static void Main()
    {
        TcpListener server = null;
        try
        {
            // Start listening for client requests.
            server = new TcpListener(IPAddress.Any, PORT);
            server.Start();
            Console.WriteLine("Server started on port " + PORT);

            while (true)
            {
                // Perform a blocking call to accept requests.
                // You could also use server.AcceptTcpClientAsync() for async handling.
                TcpClient client = server.AcceptTcpClient();
                Console.WriteLine("Connected to a client!");

                // Handle client in a separate method
                HandleClient(client);
            }
        }
        catch (SocketException e)
        {
            Console.WriteLine("SocketException: {0}", e);
        }
        finally
        {
            // Stop listening for new clients.
            server.Stop();
        }
    }

    private static void HandleClient(TcpClient client)
    {
        byte[] buffer = new byte[BUFFER_SIZE];
        NetworkStream stream = client.GetStream();

        // Read the client's request (not processing request headers in this simple example)
        int bytesRead = stream.Read(buffer, 0, buffer.Length);
        if (bytesRead > 0)
        {
            Console.WriteLine("Received request:\n" + Encoding.ASCII.GetString(buffer, 0, bytesRead));

            // Read the HTML file
            string htmlResponse = ReadHtmlFile(HTML_FILE_PATH);

            // Create a basic HTTP response
            string httpResponse = "HTTP/1.1 200 OK\r\n" +
                                  "Content-Type: text/html\r\n" +
                                  "Content-Length: " + Encoding.UTF8.GetByteCount(htmlResponse) + "\r\n" +
                                  "\r\n" + htmlResponse;

            // Send the response back to the client
            byte[] responseBuffer = Encoding.UTF8.GetBytes(httpResponse);
            stream.Write(responseBuffer, 0, responseBuffer.Length);
        }

        // Shutdown and end connection
        client.Close();
    }

    private static string ReadHtmlFile(string filePath)
    {
        if (File.Exists(filePath))
        {
            return File.ReadAllText(filePath);
        }
        else
        {
            return "<html><body><h1>404 Not Found</h1></body></html>"; // Return 404 if file not found
        }
    }
}
