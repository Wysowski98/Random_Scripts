#include <iostream>
#include <SFML/Graphics.hpp>
#include <vector>

using namespace sf;
using namespace std;


// Compile and run it
// g++ triangle.cpp -o triangle -lsfml-graphics -lsfml-window -lsfml-system && ./triangle


// Pick 3 points.
// Pick a random number (Equally chance to pick either of the points) and go half of the distance from the actual position to the point.


// Constants
const int SPEED = 2900;
const int SIZE = 600;
const int CIRCLE_RADIUS = 1;

const int ALPHA = 100; // The alpha of the points
const Color CIRCLE_COLOR = Color(0, 0, 0, ALPHA);

// Set the points
Vector2i point1 = { 300, 50 };
Vector2i point2 = { 100, 500 };
Vector2i point3 = { 500, 500 };




int main(){
	RenderWindow window(VideoMode(SIZE, SIZE), "Sierpinski's Triangle");
	window.setFramerateLimit(SPEED);
	Vector2i actualPoint = {SIZE/2, SIZE/2};
	window.clear(Color::White);


	while (window.isOpen()){
		Event e;
		while (window.pollEvent(e)){
			if (e.type == Event::Closed) window.close();
		}


	CircleShape circle;

	circle.setFillColor(CIRCLE_COLOR);
	circle.setRadius(CIRCLE_RADIUS);

	// Uncomment this if you want rainbow circles
	//circle.setFillColor( rand() % 256, rand() % 256 ,rand() % 256);

	

	// We pick a random value between 0 and 2
	int randomChance = rand() % 3;
	
	// if randomChance == 0 then we go to point 1
	// if randomChance == 1 then we go to point 2
	// if randomChance == 2 then we go to point 3

	if (randomChance == 0) {
			actualPoint.x = (actualPoint.x + point1.x)/2;
			actualPoint.y = (actualPoint.y + point1.y)/2;
	}
	if (randomChance == 1) {
			actualPoint.x = (actualPoint.x + point2.x)/2;
			actualPoint.y = (actualPoint.y + point2.y)/2;
	}
	if (randomChance == 2) {
			actualPoint.x = (actualPoint.x + point3.x)/2;
			actualPoint.y = (actualPoint.y + point3.y)/2;
	}

	circle.setPosition(actualPoint.x, actualPoint.y);
	window.draw(circle);

	window.display();
	}
	return 0;
}
