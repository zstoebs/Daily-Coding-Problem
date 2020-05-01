/**
 * @author Zach Stoebner
 * @date 5-1-2020
 * @details Implement a queue using a set of fixed-length arrays.
 *          The queue should support enqueue, dequeue, and get_size operations.
 */

#ifndef FIXEDQUEUE_CPP
#define FIXEDQUEUE_CPP

#include <algorithm>
#include <stdexcept>

/// METHODS

/**
 * FixedQueue ctor
 */
template <typename T, unsigned int SIZE>
FixedQueue<T, SIZE>::FixedQueue() : master(nullptr), size(0), master_len(0) {}

/**
 * FixedQueue copy ctor
 */
template <typename T, unsigned int SIZE>
FixedQueue<T, SIZE>::FixedQueue(const FixedQueue<T, SIZE> &rhs)
    : master(rhs.copy_master()), size(rhs.size), master_len(rhs.master_len) {}

/**
 * Initializes the queue
 * @param arr an array of T objs to initialize the queue
 */
template <typename T, unsigned int SIZE>
FixedQueue<T, SIZE>::FixedQueue(const T arr[])
    : master(), size(*(&arr + 1) - arr), master_len(0) {

  try {

    for (int i = 0; i < size; ++i)
      enqueue(arr[i]);

  } catch (const std::exception &e) {
    delete_master();
  }
}

/**
 * FixedQueue dtor
 */
template <typename T, unsigned int SIZE>
FixedQueue<T, SIZE>::~FixedQueue() noexcept {
  delete_master();
}

/**
 * Assignment operator
 */
template <typename T, unsigned int SIZE>
FixedQueue<T, SIZE> &FixedQueue<T, SIZE>::
operator=(const FixedQueue<T, SIZE> &rhs) {

  if (this != &rhs) {
    FixedQueue<T, SIZE> tmp(rhs);

    std::swap(master, tmp.master);
    std::swap(size, tmp.size);
    std::swap(master_len, tmp.master_len);
  }

  return *this;
}

/**
 * Enqueues obj to the back of the queue, handles buffering the master array
 * @param obj element to add
 */
template <typename T, unsigned int SIZE>
void FixedQueue<T, SIZE>::enqueue(const T &obj) {

  T **newArr;
  int curr_ind = size % SIZE;

  if (curr_ind == 0) {

    // copy and buffer
    newArr = buff_master();
    newArr[master_len][curr_ind] = obj;

    // garbage collection
    delete_master();

    ++master_len;

  } else {

    // copy
    newArr = copy_master();
    newArr[master_len - 1][curr_ind] = obj;

    // garbage collection
    delete_master();
  }

  master = newArr;
  ++size;
}

/**
 * Removes the first obj in queue
 * @return a copy of dequeued obj
 */
template <typename T, unsigned int SIZE> T FixedQueue<T, SIZE>::dequeue() {

  if (size == 0) {
    throw std::underflow_error("Error: no elements in queue");
  }

  // get first element
  T obj = master[0][0];

  // enqueue all elements to a temp FixedQueue, except for the first element
  FixedQueue<T, SIZE> tmp;

  for (int count = 1, i = 0; count < size; ++count) {

    int j = count % SIZE;
    if (j == 0)
      ++i;

    tmp.enqueue(master[i][j]);
  }

  std::swap(master, tmp.master);
  std::swap(size, tmp.size);
  std::swap(master_len, tmp.master_len);

  return obj;
}

/**
 * Gets the size of the queue
 * @return positive size int
 */
template <typename T, unsigned int SIZE>
unsigned int FixedQueue<T, SIZE>::get_size() const {
  return size;
}

/// HELPERS

/**
 * Increases the master buffer as a copy
 * @return ptr to the new buffered copy of master
 */
template <typename T, unsigned int SIZE>
T **FixedQueue<T, SIZE>::buff_master() const {

  T **newArr;

  // copy
  newArr = new T *[master_len + SIZE];
  for (int i = 0; i < master_len; ++i) {
    newArr[i] = new T[SIZE];

    for (int j = 0; j < SIZE; ++j) {
      newArr[i][j] = master[i][j];
    }
  }

  newArr[master_len] = new T[SIZE];

  return newArr;
}

/**
 * Deletes the master array
 */
template <typename T, unsigned int SIZE>
void FixedQueue<T, SIZE>::delete_master() noexcept {

  if (master_len > 0) {
    for (int i = 0; i < master_len; ++i)
      delete[] master[i];
    delete[] master;
  }
  master = nullptr;
}

/**
 * Copies master array
 */
template <typename T, unsigned int SIZE>
T **FixedQueue<T, SIZE>::copy_master() const {

  T **newArr = new T *[master_len];
  for (int i = 0; i < master_len; ++i) {
    newArr[i] = new T[SIZE];

    for (int j = 0; j < SIZE; ++j)
      newArr[i][j] = master[i][j];
  }
  return newArr;
}

#endif // FIXEDQUEUE_CPP
