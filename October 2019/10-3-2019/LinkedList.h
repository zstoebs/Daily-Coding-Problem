/**
 * @filename LinkedList.h
* @author   Zach Stoebner
* @date     10-3-2019
* @descrip  Given the head of a singly linked list, swap every two nodes and return its head.
*
* For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
*/

#ifndef OCTOBER_2019_LINKEDLIST_H
#define OCTOBER_2019_LINKEDLIST_H

#include <cstdint>
#include <stdexcept>

template <typename T>
class LinkedList {

public:
    struct Node {
        Node* next;
        T data;

        Node() : next(nullptr),data(T()) {}

    };
    typedef Node* NodePtr;

    LinkedList();
    LinkedList(const LinkedList<T>&);
    ~LinkedList();
    LinkedList & operator=(const LinkedList<T>&);
    void push(const T&);
    T pop();
    T& peek() const;
    bool isEmpty() const;
    uint32_t getSize() const;
    const Node& LLswap();

private:

    NodePtr head;
    uint32_t size;

};

#include "LinkedList.cpp"

#endif //OCTOBER_2019_LINKEDLIST_H
