/*
 * 8-23-2019.cpp
 * Author: Zach Stoebner
 * Created on: 8-23-2019
 * Descrip: Driving solver to 8-23 DCP
 *    Determine whether a doubly linked
 *    list is a palindrome. What if it’s singly linked?
 *    For example, 1 -> 4 -> 3 -> 4 -> 1
 *    returns True while 1 -> 4 returns False.
 */

 #include <cstdlib>
 #include <iostream>
 #include "DoublyLinkedList.h"

 /*
  * @brief Test driver for 8-23 solution
  */
 int main() {

   DoublyLinkedList<int> test1;
   test1.push(1);
   test1.push(4);
   test1.push(3);
   test1.push(4);
   test1.push(1);

   std::cout << test1.isPalindrome() << std::endl;

   return 0;

 }
