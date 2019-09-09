"""
@author Zach Stoebner
@date 9-9-2019
@descrip Given a string which we can delete at most k,
  return whether you can make a palindrome.

  For example, given 'waterrfetawx' and a k of 2,
  you could delete f and x to get 'waterretaw'.
"""
#need to remove all chars without a pair

#hasPalindrome
#Note: checks if a string with k removal opportunities has/is a palindrome
#Complexity: O(n^2) time
def has_palindrome(word, k=0):

    #helper function to detect if a string is a palindrome
    def is_palindrome(string):

        return string[::-1] == string

    #helper function to remove a char at a given index for a passed string
    def remove_char(string,index):
        new_string = ""
        for i in range(len(string)):
            if i != index:
                new_string += string[i]
        return new_string

    #helper function to half the string, if even returns a list of two strings
    #if length is even returns a list of two halves and bool if even or odd, else returns [first half,middle index,second half]
    # flips the last half
    def half_string(word):
        length = len(word)
        ret = list([])
        even = None
        if length % 2 == 0:
            half_point = length // 2
            ret.append(word[:half_point])

            last_half = word[half_point:]
            ret.append(last_half[::-1])

            even = True
        else:
            half_point = (length-1) // 2
            ret.append(word[:half_point])
            ret.append(word[half_point])

            last_half = word[half_point+1:]
            ret.append(last_half[::-1])

            even = False

        return ret,even

    #removing unpaired chars
    copy_string = word
    length = len(word)
    for i in range(length):
        if word.count(word[i]) < 2:
            copy_string = remove_char(copy_string,i)
            k -= 1

    if k < 0:
        return False
    elif is_palindrome(copy_string):
        return True

    #removing mismatched pairs
    while k > 0:
        splits,even = half_string(copy_string)
        if even:
            for i in len(splits[0]):
                if splits[0][i] not in splits[1]:
                    copy_string = remove_char(copy_string,i)
                    k -= 1
        else:
            for i in len(splits[0]):
                if splits[0][i] not in splits[2]:
                    copy_string = remove_char(copy_string,i)
                    k -= 1

    return is_palindrome(copy_string)

word = 'waterrfetawx'
print(has_palindrome(word,2)) #doesn't work :(
