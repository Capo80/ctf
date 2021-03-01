#include <stdlib.h>

void func(int a) {
	while(1) {}

}

void main() {
	void* test = malloc(100);
	func(1);
}
