#include <cassert>
#include <iostream>

class Solution {
 public:
  static bool isPowerOfFour(int n) {
    return (n && !(n & (n - 1))) && n > 0 && (n & 0x55555555);
  }
};

int main(int argc, char *argv[]) {
  assert(Solution::isPowerOfFour(16) == true);
  assert(Solution::isPowerOfFour(15) == false);
  assert(Solution::isPowerOfFour(16777216) == true);
  return 0;
}
