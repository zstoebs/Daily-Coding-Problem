/* main.cpp
* Author: Zach Stoebner
* Created on: 8-5-2019
* Descrip: class to count min number of removable parentheses
*/
// Created by Zachary Stoebner on 2019-08-05.
//

#ifndef INC_8_5_2019_PARENTHESES_H
#define INC_8_5_2019_PARENTHESES_H

#include <cstdlib>
#include <stack>
#include <string>


class Parentheses {

private:

    size_t count; //count of parentheses to remove
    std::stack<char> parenthStck; //stack of unpaired parentheses

public:

    /*
     * default constructor
     */
    Parentheses();

    /*
     * alt constructor
     * calls numToRemove within constructor to initialize count
     */
    Parentheses(const std::string& str);


    /*
     * numToRemove
     * returns the min num of parenths to remove
     * pre: Parentheses class constructed
     * post: count incremented appr. and returned
     */
    size_t numToRemove(const std::string& str);

    /*
     * getCount
     * returns count of parenths to remove
     * pre: alt constructor called
     * post: min num parenths to remove returned
     */
    size_t getCount() const;


};


#endif //INC_8_5_2019_PARENTHESES_H
