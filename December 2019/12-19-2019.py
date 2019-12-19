"""
@author Zach Stoebner
@date 12-19-2019
@descrip Given an absolute pathname that may have . or .. as part of it,
return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
"""

def standard_path(path=""):

    dirs = path.split('/')
    stand = []
    for dir in dirs:
        if dir == ".." and stand[0]:
            stand.pop()
        elif dir != ".." and dir != "." and dir != '':
            stand.append(dir)

    ret = "/"
    for dir in stand:
        ret += dir + "/"

    return ret

### TESTS
t1 = "/usr/bin/../bin/./scripts/../"
print(standard_path(t1)) #/usr/bin/
