"""
Author: Zach Stoebner
Data: 9-2-2019
Descrip:

Given a string and a set of delimiters,
reverse the words in the string while
maintaining the relative order of the
delimiters. For example, given "hello/world:here",
return "here/world:hello"

Follow-up: Does your solution work
for the following cases: "hello/world:here/",
"hello//world:here"

"""
#can't assume delimiter list is sorted in order of appearance
#can use string's split method to break apart to the string and then reconstruct from reverse
#perhaps recursion?
#need to store the order of the delimiters
#could store as a tree?

#Help from: https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
#delimiter_split
#Note: returns reversed string around delimiters
#Complexity:
def delimiter_split(string,delimiters):

    #saving each split into a dictionary
    limits = dict([])
    for delimiter in delimiters:
        limits[delimiter] = string.split(delimiter)

    #finding order
    delim_order = list([])
    all_delims = False
    while not all_delims:

        for limit in limits.keys():
            state = True
            for delim in delimiters:
                if delim in limits[limit][0] and delim not in delim_order:
                    state = False
            if state:
                delim_order.append(limit)

        #determining whether all delimiters have been added
        all_delims = True
        for delim in delimiters:
            if delim not in delim_order:
                all_delims = False

    #breaking down string into words
    new_str = ""
    for delimiter in delimiters:
        if delimiter == delimiters[0]:
            new_str = string.replace(delimiter,',')
        else:
            new_str = new_str.replace(delimiter,',')

    words = new_str.split(',')

    delim_ind = 0
    rev_str = ""
    for word in reversed(words):
        if delim_ind >= len(delimiters):
            rev_str += word
        else:
            rev_str += word + delim_order[delim_ind]
            delim_ind += 1

    return rev_str

string = "hello/world:here"
print(delimiter_split(string,['/',':'])) #here/world:hello
string = "hello/world:here/"
print(delimiter_split(string,['/',':'])) #/here:worldhello -- doesn't work; can't handle duplicates
string = "hello//world:here"
print(delimiter_split(string,['//',':'])) #here//world:hello
