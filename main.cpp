#include <SFML/Graphics.hpp>
#include <iostream>
#include <windows.h>

using namespace std;
void circleF(){
    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML TUTORIAL");
    sf::CircleShape shape(200.f);
    shape.setFillColor(sf::Color::Blue);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        window.draw(shape);
        window.display();
    }

}

int draw_and_text(){
    // Create a window
    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Shapes and Text");

    // Create a circle shape
    sf::CircleShape circle(50);
    circle.setFillColor(sf::Color::Red);
    circle.setPosition(100, 100);

    // Create a rectangle shape
    sf::RectangleShape rectangle(sf::Vector2f(100, 50));
    rectangle.setFillColor(sf::Color::Blue);
    rectangle.setPosition(300, 200);

    // Create a text object
    sf::Font font;
    if (!font.loadFromFile("arial.ttf")) {
        // Error handling
        return -1;
    }
    sf::Text text("SFML Shapes and Text", font, 30);
    text.setFillColor(sf::Color::White);
    text.setPosition(200, 400);

    // Main loop
    while (window.isOpen()) {
        // Process events
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Clear the window
        window.clear();

        // Draw shapes and text
        window.draw(circle);
        window.draw(rectangle);
        window.draw(text);

        // Display the window contents
        window.display();
    }

}

void inputf(){
    // Create a window
    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Keyboard Input");

    // Create a shape
    sf::RectangleShape rectangle(sf::Vector2f(100, 100));
    rectangle.setFillColor(sf::Color::Green);
    rectangle.setPosition(100, 100);

    // Main loop
    while (window.isOpen()) {
        // Process events
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
            // Handle keyboard input
            if (event.type == sf::Event::KeyPressed) {
                if (event.key.code == sf::Keyboard::Left)
                    rectangle.move(-10, 0);
                else if (event.key.code == sf::Keyboard::Right)
                    rectangle.move(10, 0);
                else if (event.key.code == sf::Keyboard::Up)
                    rectangle.move(0, -10);
                else if (event.key.code == sf::Keyboard::Down)
                    rectangle.move(0, 10);
            }
        }

        // Clear the window
        window.clear();

        // Draw the shape
        window.draw(rectangle);

        // Display the window contents
        window.display();
    }

}


int main()
{
	Start:;
    std::cout<<"Choose one of the below choices:"<<"\n";
    std::cout<<"1. Circle"<<"\n";
    std::cout<<"2. Text"<<"\n";
    std::cout<<"3. Input"<<"\n";
    std::cout<<"4. Exit"<<"\n";
    int choice;
    std::cout<<"Selected:";
    std::cin>>choice;
    switch(choice){
        case 1:
            circleF();
            std::cout << "Press any key to continue...";
    		std::cin.get(); // Wait for a key press
            break;
        case 2:
            draw_and_text();
            std::cout << "Press any key to continue...";
   			std::cin.get(); // Wait for a key press
            break;
        case 3:
            inputf();
            std::cout << "Press any key to continue...";
    		std::cin.get(); // Wait for a key press
            break;
        case 4:
        	std::cout<<"OK!!!";
        	std::cout << "Press any key to continue...";
    		std::cin.get(); // Wait for a key press
            break;
        default:
            std::cout<<"Invalid choice"<<"\n";
            std::cout << "Press any key to continue...";
    		std::cin.get(); // Wait for a key press
    		goto Start;
    }
    return 0;
}
