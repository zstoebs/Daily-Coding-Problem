/**
 * @author Zach Stoebner
 * @date 5-1-2020
 * @details Implement a queue using a set of fixed-length arrays.
 *          The queue should support enqueue, dequeue, and get_size operations.
 */

#ifndef INC_5_1_2020_FIXEDQUEUE_H
#define INC_5_1_2020_FIXEDQUEUE_H

/**
 * Implements a queue with a set of fixed-size arrays
 * @tparam T the obj type that the FixedQueue holds
 */
template <typename T, unsigned int SIZE = 5> class FixedQueue {

public:
  /**
   * FixedQueue ctor
   */
  FixedQueue();

  /**
   * FixedQueue copy ctor
   */
  FixedQueue(const FixedQueue<T, SIZE> &rhs);

  /**
   * Initializes the queue
   * @param arr an array of T objs to initialize the queue
   */
  FixedQueue(const T arr[]);

  /**
   * FixedQueue dtor
   */
  ~FixedQueue() noexcept;

  /**
   * Assignment operator
   */
  FixedQueue<T, SIZE> &operator=(const FixedQueue<T, SIZE> &rhs);

  /**
   * Enqueues obj to the back of the queue
   * @param obj
   */
  void enqueue(const T &obj);

  /**
   * Removes the first obj in queue
   * @return a copy of dequeued obj
   */
  T dequeue();

  /**
   * Gets the size of the queue
   * @return positive size int
   */
  unsigned int get_size() const;

private:
  /**
   * Increases the master buffer as a copy
   * @return ptr to a new buffered copy of master
   */
  T **buff_master() const;

  /**
   * Deletes the master array
   */
  void delete_master() noexcept;

  /**
   * Copies master array
   */
  T **copy_master() const;

  T **master;
  unsigned int size;
  unsigned int master_len;
};

#include "../src/FixedQueue.cpp"
#endif // INC_5_1_2020_FIXEDQUEUE_H
