#include <iostream>

using namespace std;

int main() {
  int x, y;
  for (x = 0; x <= 100; x++) {
    for (y = 0; y <= 100; y++) {
      if ((100 - x - y)%3 == 0 and 5 * x + y * 3 + (100 - x - y)/3 == 100) {
        cout << "鸡翁: " << x << ", 鸡母: " << y << ", 鸡雏: " << 100-x-y <<endl;
      }
    }
  }
}
