using System;
using System.Net;
using System.Text;

public class SimpleWebServer
{
    private HttpListener listener;

    public SimpleWebServer(string[] prefixes)
    {
        listener = new HttpListener();
        foreach (string prefix in prefixes)
        {
            listener.Prefixes.Add(prefix);
        }
    }

    public void Start()
    {
        listener.Start();
        Console.WriteLine("Web server running...");

        while (true)
        {
            HttpListenerContext context = listener.GetContext();
            HttpListenerRequest request = context.Request;
            HttpListenerResponse response = context.Response;

            string responseString = "<html><body>Hello World</body></html>";
            byte[] buffer = Encoding.UTF8.GetBytes(responseString);
            response.ContentLength64 = buffer.Length;

            using (var output = response.OutputStream)
            {
                output.Write(buffer, 0, buffer.Length);
            }
        }
    }

    public void Stop()
    {
        listener.Stop();
    }
}
