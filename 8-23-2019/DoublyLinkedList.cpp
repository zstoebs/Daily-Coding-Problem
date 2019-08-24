/*
 * DoublyLinkedList.cpp
 * Author: Zach Stoebner
 * Created on: 8-23-2019
 * Descrip: Defining a doubly linked list class to solve 8-23 DCP
 *    Determine whether a doubly linked
 *    list is a palindrome. What if it’s singly linked?
 *    For example, 1 -> 4 -> 3 -> 4 -> 1
 *    returns True while 1 -> 4 returns False.
 */

 #include <cstdlib>

 /**
  * @brief Default constructor
  */
 template<typename T>
 DoublyLinkedList<T>::DoublyLinkedList() : size(0), head(nullptr), tail(nullptr) {}
 //nothing left to do

 /**
  * @brief Copy constructor
  */
 template<typename T>
 DoublyLinkedList<T>::DoublyLinkedList(const DoublyLinkedList<T>& rhs) : size(rhs.size), head(nullptr) {

   if (rhs.head != nullptr) {

     //copying first node to get a handle
     head = new Node;
     head->data = rhs.head->data;
     head->prev = nullptr;
     head->nxt = nullptr;

     //copying remaining nodes
     NodePtr cur, nxt;
     for (cur = head, nxt = rhs.head->nxt;
       nxt != nullptr;
       nxt = nxt->nxt, cur = cur->nxt) {

         cur->nxt = new Node;
         cur->nxt->data = nxt->data;
         cur->nxt->prev = cur;
         cur->nxt->nxt = nullptr;
         tail = cur;

     }

   }

 }

 /**
  * @brief Destructor
  */
 template<typename T>
 DoublyLinkedList<T>::~DoublyLinkedList() {

   tail = nullptr;

   while (head != nullptr) {

     NodePtr tmp = head;
     head = head->nxt;
     head->prev = nullptr;

     tmp->nxt = nullptr;
     delete tmp;
     tmp = nullptr;

   }

   size = 0;

 }

 /**
  * @brief Copy assignment operator
  */
 template<typename T>
 DoublyLinkedList<T> & DoublyLinkedList<T>::operator=(const DoublyLinkedList<T>& rhs) {

   if (this != &rhs) {

     DoublyLinkedList<T> tmp(rhs);

     std::swap(size,tmp.size);
     std::swap(head,tmp.head);
     std::swap(tail,tmp.tail);

   }

   return *this;

 }

 /**
  * @brief Inserts node with data after prior
  * @details Returns true if successfully inserted, else returns false
  * @param <data> data to insert
  * @param <prior> prior data to insert data after
  * @return truth value of insert
  * @pre data and prior are correct type and passed
  * @post data inserted after prior data and true, otherwise false
  */
 template<typename T>
 bool DoublyLinkedList<T>::insert(const T& data, const T& prior) {

   if (isEmpty()) {

     head = new Node;
     head->data = data;
     head->prev = nullptr;
     head->nxt = nullptr;
     tail = head;

     ++size;
     return true;

   }

   NodePtr cur = head;
   while (cur != nullptr && cur->data != prior) {
     cur = cur->nxt;
   }

   if (cur != nullptr) {

     NodePtr nxt = cur->nxt;
     NodePtr newInsert = new Node;
     newInsert->data = data;

     newInsert->prev = cur;
     cur->nxt = newInsert;

     newInsert->nxt = nxt;
     nxt->prev = newInsert;

     ++size;
     return true;

   }

   return false;

 }

 /**
  * @brief Pushes node to end of list
  * @param <data> data to push
  */
 template<typename T>
 void DoublyLinkedList<T>::push(const T& data) {

   if (isEmpty()) {

     head = new Node;
     head->data = data;
     head->prev = nullptr;
     head->nxt = nullptr;
     tail = head;

   } else {

     tail->nxt = new Node;
     NodePtr tmp = tail;
     tail = tail->nxt;
     tail->data = data;
     tail->prev = tmp;
     tail->nxt = nullptr;

   }

 }

 /**
  * @brief Removes node with data that matches target
  * @details Removes first instance node with target data, returns true
  *          if found and removed, else returns false
  * @param <target> target data to remove
  * @return truth value of removal
  * @pre target is correct type and passed
  * @post node with target data is removed
  */
 template<typename T>
 bool DoublyLinkedList<T>::remove(const T& target) {

   NodePtr cur = head;
   while (cur != nullptr && cur->data != target) {
     cur = cur->nxt;
   }

   if (cur != nullptr) {

     NodePtr prev = cur->prev, nxt = cur->nxt;

     prev->nxt = nxt;
     nxt->prev = prev;

     cur->prev = cur->nxt = nullptr;

     delete cur;
     cur = nullptr;

     --size;
     return true;

   }

   return false;

 }

 /**
  * @brief Checks if linked list is empty
  * @details Checks if size, head, and tail are their default values
  *          to determine emptiness
  * @return truth value of emptiness
  * @pre DLL is declared
  * @post bool returned
  */
 template<typename T>
 bool DoublyLinkedList<T>::isEmpty() {

   return (size == 0 && head == nullptr && tail == nullptr);

 }

 /**
  * @brief Checks if linked list is a palindrome
  * @details Iterates from both ends of linked list, if all
  *          analogous values equal returns true, else false
  * @return truth value of palindrome attrib
  * @pre DLL is declared
  * @post bool returned
  */
 template<typename T>
 bool DoublyLinkedList<T>::isPalindrome() {

   NodePtr left = head, right = tail;

   if (left != nullptr && right != nullptr) {

     while (left->prev != right) {

       if (left->data != right->data) {
         return false;
       }

       left = left->nxt;
       right = right->prev;

     }

     return true;

   }

   return false;

 }
