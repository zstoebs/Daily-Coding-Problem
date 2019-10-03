/**
 * @filename LinkedList.cpp
* @author   Zach Stoebner
* @date     10-3-2019
* @descrip  Given the head of a singly linked list, swap every two nodes and return its head.
*
* For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
*/

template<typename T>
LinkedList<T>::LinkedList() : head(nullptr),size(0)
{
}

template<typename T>
LinkedList<T>::LinkedList(const LinkedList<T>& rhs) : head(nullptr),size(rhs.size) {

    if (!rhs.isEmpty()) {

        LinkedList<T> tmp;
        for (NodePtr cur = rhs.head; cur != nullptr; cur = cur->next) {
            tmp.push(cur->data);
        }
        std::swap(head,tmp.head);

    }

}

template<typename T>
LinkedList<T>::~LinkedList() {

    while (!isEmpty()) {
       pop();
    }
    size = 0;

}

template<typename T>
LinkedList<T> & LinkedList<T>::operator=(const LinkedList<T>& rhs) {

    if (this != &rhs) {

        LinkedList<T> tmp(rhs);
        std::swap(head,tmp.head);
        std::swap(size,tmp.size);

    }
    return *this;
}

template<typename T>
void LinkedList<T>::push(const T& item) {

    NodePtr tmp = new Node;
    tmp->data = item;
    tmp->next = head;
    head = tmp;
    ++size;

}

template<typename T>
T LinkedList<T>::pop() {

    if (isEmpty()) {

        throw std::underflow_error("List is empty");
    }

    NodePtr tmp = head;
    T item = tmp->data;

    head = head->next;
    delete tmp;

    --size;
    return item;

}

template<typename T>
T& LinkedList<T>::peek() const {

    if (isEmpty()) {

        throw std::underflow_error("List is empty");
    }

    return head->data;


}

template<typename T>
bool LinkedList<T>::isEmpty() const {

    return head == nullptr;
}

template<typename T>
uint32_t LinkedList<T>::getSize() const {
    return size;
}

///THIS IS THE MEAT BUT IT'S BROKEN.
template<typename T>
const typename LinkedList<T>::Node& LinkedList<T>::LLswap() {

    if (isEmpty()) {
        throw std::underflow_error("Stack is empty: nothing to swap.");
    }

    LinkedList<T> tmp(*this);
    enum STATE {ONE,TWO};
    STATE state = ONE;

    for (NodePtr cur = tmp.head, prev = cur,first = prev;
    cur != nullptr;
    first = prev, prev = cur,cur = cur->next) {

        switch (state) {

            case ONE:
                state = TWO;
            case TWO:

                if (first == tmp.head) {
                    tmp.head = cur;
                } else {
                    first->next = cur;
                }
                prev->next = cur->next;
                cur->next = prev;

                state = ONE;

        }

    }

    std::swap(head,tmp.head);
    return *head;

}



