"""
@author Zach Stoebner
@date 12-29-2019
@descrip Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists,
overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
"""

class PrefixMapSum:

    def __init__(self):
        self.map = dict()

    def insert(self,key: str,value: int):
        self.map[key] = value

    def sum(self,prefix: str) -> int:
        n = len(prefix)
        sum = 0
        for key in self.map.keys():
            if key[:n] == prefix:
                sum += self.map[key]
        return sum

### TESTS
mapsum = PrefixMapSum()
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
# Doesn't throw an assertion error! --> PASS
