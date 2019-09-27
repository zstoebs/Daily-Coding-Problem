"""
@author   Zach Stoebner
@date     9-27-2019
@descrip  Given an iterator with methods next() and hasNext(),
create a wrapper iterator, PeekableInterface, which also
implements peek(). peek shows the next element that would be returned on next().

Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
"""
"""
I really don't know if this is correct. The difficulty is medium 
so I'm probs missing something here but alas it's another poorly
worded, ultra vague DCP.
"""
class PeekableInterface(object):
    def __init__(self, iterator):
        selt.iter = iterator

    def peek(self):
        tmp = self.iterator
        return tmp.next()

    def next(self):
        return self.iter.next()

    def hasNext(self):
        return self.iter.hasNext()
