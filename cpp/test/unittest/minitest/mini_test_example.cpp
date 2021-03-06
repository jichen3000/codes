#include <iostream>
#include "mini_test.h"
#include <stdexcept>
using namespace mt;

void max_between_positives() {
  int m = max(3, 7);
  ASSERT_EQ(m, 8);
  ASSERT_EQ("12", "34");
}

void max_between_negatives() {
  int m = max(-3, -7);
  ASSERT_EQ(m, -3);
}

int main() {
  RUN_TEST(max_between_positives);
  RUN_TEST(max_between_negatives);

  return 0;
}