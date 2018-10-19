#include <stdio.h>
#include <math.h>
#include <iostream>

double randn() {
	double x, y, radius;
	do {
		x = 2 * (rand() / ((double) RAND_MAX + 1)) - 1;
		y = 2 * (rand() / ((double) RAND_MAX + 1)) - 1;
		radius = (x * x) + (y * y);
	} while((radius >= 1.0) || (radius == 0.0));
	radius = sqrt(-2 * log(radius) / radius);
	x *= radius;
	y *= radius;
	return x;
}
int main() {
    int count = 1000;
    double random_value, max, min,sum;
    max = 0.0;
    min = 0.0;
    sum = 0.0;
    srand(2);
    for (size_t i = 0; i < count; i++) {
        random_value = randn();
        if (random_value > max){
            max = random_value;
        }
        if (random_value < min){
            min = random_value;
        }
        sum += random_value;
    }
    double mean = sum / count;
    std::cout << "mean: " << mean << std::endl;
    std::cout << "max: " << max << std::endl;
    std::cout << "min: " << min << std::endl;

}
