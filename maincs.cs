// // See https://aka.ms/new-console-template for more information
// Console.WriteLine("Hello, World!");
using System;

public class MainCS
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Hello from C#!");

        // Equivalent to system("pause");
        // Console.WriteLine("Press any key to continue...");
        // Console.ReadKey();  // Waits for the user to press a key
        // Pause with a user prompt
        Console.WriteLine("Press Enter to continue...");

        // Read input from the console to pause the program
        // This works whether the program is launched directly or by Rust
        Console.ReadLine();
    }
}
