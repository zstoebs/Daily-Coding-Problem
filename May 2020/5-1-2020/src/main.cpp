/**
 * @author Zach Stoebner
 * @date 5-1-2020
 * @details Implement a queue using a set of fixed-length arrays.
 *          The queue should support enqueue, dequeue, and get_size operations.
 */

#include "../include/FixedQueue.h"
#include <iostream>
#include <stdexcept>

int main() {

  typedef FixedQueue<int> Q;

  Q test;

  if (test.get_size() == 0) {
    std::cout << "Init size. PASS" << std::endl;
  } else {
    std::cout << "Init size. Return: " << test.get_size() << " FAIL"
              << std::endl;
  }

  try {
    test.dequeue();
    std::cout << "Underflow error. FAIL" << std::endl;
  } catch (const std::underflow_error &e) {
    std::cout << "Underflow error. PASS" << std::endl;
  }

  for (int i = 0; i < 97; ++i)
    test.enqueue(i);

  if (test.get_size() == 97) {
    std::cout << "Enqueue size. PASS" << std::endl;
  } else {
    std::cout << "Enqueue size. FAIL" << std::endl;
  }

  for (int i = 0; i < 5; ++i)
    std::cout << test.dequeue() << " ";
  std::cout << std::endl;

  return 0;
}
