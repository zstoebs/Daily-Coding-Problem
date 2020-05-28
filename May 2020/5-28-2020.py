"""
@author Zach Stoebner
@date 5-28-2020
@details Implement the function embolden(s, lst) which takes in a string s and list of
substrings lst, and wraps all substrings in s with an HTML bold tag <b> and </b>.

If two bold tags overlap or are contiguous, they should be merged.

For example, given s = abcdefg and lst = ["bc", "ef"], return the string a<b>bc</b>d<b>ef</b>g.

Given s = abcdefg and lst = ["bcd", "def"], return the string a<b>bcdef</b>g, since they overlap.
"""

# embolden
# Inserts HTML bold tags around the specified substrings
# Complexity: O()
def embolden(s: str, lst: list) -> str:

    # to keep track of indices in original string that should have a tag before them
    tags = dict()
    for i in range(len(s)+1):
        tags[i] = []

    # split around each substr, keep track of curr index to add to dict
    for sub in lst:
        split = s.split(sub)
        cur_ind = 0
        for i, ss in enumerate(split):
            if i == 0:
                cur_ind += len(ss)
                tags[cur_ind] += ["<b>"]
            elif i == len(split)-1:
                cur_ind += len(sub)
                tags[cur_ind] += ["</b>"]
            else:
                cur_ind += len(sub)
                tags[cur_ind] += ["</b>"]
                cur_ind += len(ss)
                tags[cur_ind] += ["<b>"]

    # use a stack to remove tags wrapped in other tags
    stk = []
    keys = [key for key in tags.keys()]
    for key in keys:
        if len(tags[key]) == 0: # remove unnecessary indices
            del tags[key]
        elif len(stk) == 0: # if stk is empty (and tags[key]) isn't, add a start tag
            tags[key] = "<b>"
            stk += [(key,tags[key])]
        else: # if stk and tags[key] aren't empty,
            if "</b>" in tags[key]: # if an end tag is here, then it's an overlap
                tags[key] = "</b>"
                if stk[-1][1] == "</b>": # overlapping
                    del tags[stk[-1][0]]
                    stk[-1] = (key,tags[key])
                else: # non-overlapping
                    stk += [(key,tags[key])]
            else:
                tags[key] = "<b>"
                if stk[-1][1] == "</b>": # non-overlapping
                    stk = [(key,tags[key])]
                else: # overlapping
                    del tags[key]


    chars = [c for c in s]
    keys = [key for key in tags.keys()]
    for key in reversed(keys):
        if key == len(s):
            chars += tags[key]
        else:
            chars.insert(key,tags[key])

    bolded = ""
    for c in chars:
        bolded += c

    return bolded

### TESTS
print(embolden("abcdefg",["bc","ef"]))
print(embolden("abcdefg",["bcd","def"]))
print(embolden("abcdefg",["bcd","def","g"]))
