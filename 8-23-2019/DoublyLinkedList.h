/*
 * DoublyLinkedList.h
 * Author: Zach Stoebner
 * Created on: 8-23-2019
 * Descrip: Defining a doubly linked list class to solve 8-23 DCP
 *    Determine whether a doubly linked
 *    list is a palindrome. What if it’s singly linked?
 *    For example, 1 -> 4 -> 3 -> 4 -> 1
 *    returns True while 1 -> 4 returns False.
 */

 #ifndef DOUBLY_LLINKED_LIST_H
 #define DOUBLY_LLINKED_LIST_H

 #include <cstdlib>

 /**
 * @brief   Declares a doubly linked list
 * @details Pushes to the end of the list, has an isPalindrome method,
 *          doesn't implement all standard DLL methods (e.g. reverse)
 * @author  Zach Stoebner
 */
template<typename T>
class DoublyLinkedList {

    private:

      //defining a Node with attribs for DLL
      struct Node {
          T data;
          Node *prev;
          Node *nxt;
      };
      typedef Node* NodePtr;

      size_t size; //list size
      NodePtr head; //pointer to head
      NodePtr tail; //pointer to tail

    public:

      /**
       * @brief Default constructor
       */
      DoublyLinkedList();

      /**
       * @brief Copy constructor
       */
      DoublyLinkedList(const DoublyLinkedList& rhs);

      /**
       * @brief Destructor
       */
      ~DoublyLinkedList();

      /**
       * @brief Copy assignment operator
       */
      DoublyLinkedList & operator=(const DoublyLinkedList& rhs);

      /**
       * @brief Inserts node with data after prior
       * @details Returns true if successfully inserted, else returns false
       * @param <data> data to insert
       * @param <prior> prior data to insert data after
       * @return truth value of insert
       * @pre data and prior are correct type and passed
       * @post data inserted after prior data and true, otherwise false
       */
      bool insert(const T& data, const T& prior);

      /**
       * @brief Pushes node to end of list
       * @param <data> data to push
       */
      void push(const T& data);

      /**
       * @brief Removes node with data that matches target
       * @details Removes first instance node with target data, returns true
       *          if found and removed, else returns false
       * @param <target> target data to remove
       * @return truth value of removal
       * @pre target is correct type and passed
       * @post node with target data is removed
       */
      bool remove(const T& target);

      /**
       * @brief Checks if linked list is empty
       * @details Checks if size, head, and tail are their default values
       *          to determine emptiness
       * @return truth value of emptiness
       * @pre DLL is declared
       * @post bool returned
       */
      bool isEmpty();

      /**
       * @brief Checks if linked list is a palindrome
       * @details Iterates from both ends of linked list, if all
       *          analogous values equal returns true, else false
       * @return truth value of palindrome attrib
       * @pre DLL is declared
       * @post bool returned
       */
      bool isPalindrome();

 };

 #include "DoublyLinkedList.cpp"

 #endif //DOUBLY_LLINKED_LIST_H
