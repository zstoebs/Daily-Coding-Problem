//
// Created by Zachary Stoebner on 2019-08-05.
//

#include "Parentheses.h"
#include <cstdlib>
#include <stack>
#include <string>

/*
     * default constructor
     */
Parentheses::Parentheses() : count(0) {} //nothing left to do

/*
 * alt constructor
 * calls numToRemove within constructor to initialize count
 */
Parentheses::Parentheses(const std::string& str) : count(0) {

    numToRemove(str);

}


/*
 * numToRemove
 * returns the min num of parenths to remove
 * pre: Parentheses class constructed
 * post: count incremented appr. and returned
 */
size_t Parentheses::numToRemove(const std::string& str) {

    for (size_t i = 0; i < str.length(); ++i) {

        if (str[i] == '(') {

            parenthStck.push('(');

        }

        if (str[i] == ')') {

            if (!parenthStck.empty() && parenthStck.top() == '(') {

                parenthStck.pop();

            } else {

                ++count;

            }

        }

    }

    count += parenthStck.size();

    return count;
}

/*
 * getCount
 * returns count of parenths to remove
 * pre: alt constructor called
 * post: min num parenths to remove returned
 */
size_t Parentheses::getCount() const {

    return count;

}
