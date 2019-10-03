/**
 * @filename 10-3-2019.cpp
* @author   Zach Stoebner
* @date     10-3-2019
* @descrip  Given the head of a singly linked list, swap every two nodes and return its head.
*
* For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
*/

#include <iostream>
#include "LinkedList.h"

int main() {

    LinkedList<size_t> test;
    for (size_t i = 0; i < 10; ++i) {
        test.push(i);
    }
    std::cout << test.LLswap().data << std::endl;

  return 0;
}





