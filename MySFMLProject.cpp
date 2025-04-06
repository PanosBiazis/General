#include <SFML/Graphics.hpp>

int main() {
    sf::RenderWindow window(sf::VideoMode(1900, 1200), "SFML Window Test");

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        // Draw your SFML content here
        window.display();
    }

    return 0;
}
