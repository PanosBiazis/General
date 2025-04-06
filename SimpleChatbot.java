import java.util.Scanner;

public class SimpleChatbot {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String userInput;
        System.out.println("Hello! I am a simple chatbot. Type 'exit' to quit.");

        while (true) {
            System.out.print("You: ");
            userInput = scanner.nextLine();

            if (userInput.equalsIgnoreCase("exit")) {
                System.out.println("Goodbye!");
                break;
            }

            if (userInput.contains("hello") || userInput.contains("hi")) {
                System.out.println("Bot: Hello! How can I assist you?");
            } else if (userInput.contains("your name")) {
                System.out.println("Bot: I am a chatbot created by a Java programmer.");
            } else if (userInput.contains("how are you")) {
                System.out.println("Bot: I'm just a program, but I'm doing fine!");
            } else {
                System.out.println("Bot: I'm sorry, I didn't understand that.");
            }
        }

        scanner.close();
    }
}
