"""
Author: Zach Stoebner
Data: 9-1-2019
Descrip:

Given a string of words delimited by spaces,
reverse the words in string. For example,
given "hello world here", return "here world hello"

Follow-up: given a mutable string representation,
can you perform this operation in-place?

"""

## Python doesn't support mutable strings naturally so I won't do it here.
##  Although it would be fairly straight forward in C++.
"""

void reverseWords(std::string& str) {

    length = str.length();
    startInd = 0;
    for (size_t i = length-1; i > startInd; i = length-1) {

        if (str[i] == ' ') {

            // preprending last word to beginning
            for (size_t j = i+1; j < length; ++j) {

                str.insert(startInd,str[j]);
                ++startInd;
                str.erase(j+1,1);

            }

            // prepending space at end
            str.insert(startInd,str[length-1]);
            ++startInd;
            str.erase(length-1,1);

        }

    }

}

"""

#reverse_words
#Note: reverses words in a string
#Complexity: O(n) time
def reverse_words(string):

    word_list = string.split(' ')
    rev_word = ""
    for word in reversed(word_list):
        if word == word_list[0]:
             rev_word += word
        else:
             rev_word += word + ' '

    return rev_word

string = "hello world here"
print(reverse_words(string))
string = "je t'aime"
print(reverse_words(string))
