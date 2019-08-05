/*
 * main.cpp
 * Author: Zach Stoebner
 * Created on: 8-5-2019
 * Descrip: executable for 8-5-2019 DCP
 *
 * Given a string of parentheses,
 * write a function to compute the minimum
 * number of parentheses to be removed to
 * make the string valid (i.e. each open
 * parenthesis is eventually closed).
 * For example, given the string "()())()",
 * you should return 1. Given the string ")(",
 * you should return 2, since we must remove
 * all of them.
 *
 */

#include <iostream>
#include <cstdlib>
#include <stack>
#include <string>
#include "Parentheses.h"

/*
 * validStr
 * checks if string is all parentheses
 * pre: console string entered
 * post: validity bool returned
 */
bool validStr(const std::string& str);

/*
 * realResp
 * converts input into a readable expression
 * pre: response given and passed
 * post: formatted string returned
 */
std::string realResp(const std::string& str);

int main() {

    bool cont = true;

    do {

        std::string pStr;
        bool valid = false;

        while(!valid) {

            std::cout << "Enter a string of parentheses: ";
            std::cin >> pStr;
            std::cout << std::endl;

            valid = validStr(pStr);

        }


        Parentheses p1 = Parentheses(pStr);
        std::cout << "Need to remove " << p1.getCount()
        << " for a valid string." << std::endl;

        std::string response;
        std::cout << "Would you like to enter another string? (Y | N) ";
        std::cin >> response;
        bool invalid = true;

        do {

            std::string realExp = realResp(response);
            if (realExp == "y" ||
            realExp == "yes") {

                invalid = false;

            } else if (realExp == "n" ||
            realExp == "no") {

                cont = false;
                invalid = false;

            } else {

                std::cout << "Please enter a valid response." << std::endl;

            }



        } while(invalid);




    } while (cont);



    return 0;
}

/*
 * validStr
 * checks if string is all parentheses
 * pre: console string entered
 * post: validity bool returned
 */
bool validStr(const std::string& str) {

    for (size_t i = 0; i < str.length(); ++i) {

        if (str[i] != '(' && str[i] != ')') {

            return false;

        }

    }

    return true;

}

/*
 * realResp
 * converts input into a readable expression
 * pre: response given and passed
 * post: formatted string returned
 */
std::string realResp(const std::string& str) {

    std::string r;
    for (size_t i = 0; i < str.length(); ++i) {

        r += char(std::tolower(str[i]));

    }

    return r;

}