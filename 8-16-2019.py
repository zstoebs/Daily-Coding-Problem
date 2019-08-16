"""
Author: Zach Stoebner
Created on: 8-16-2019
Descrip:

Write a map implementation with a get function
that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

set(key, value, time): sets key to value for t = time.
get(key, time): gets the key at t = time.

"""
#Map class
#Note: data structure that pairs a key and value
#the "value" for the key can be a list of tuples pairing
# passed value with passed time
#Can only have one value at a given start time
class Map(object):

    def __init__(self,**kwargs):
        self.map = dict([])
        for k,v in kwargs.items():
            self.map[k] = v

    #set
    #Note: updates map dictionary with value at appropriate place in key's list
    def set(self,key,value,time):
        if key in self.map.keys():
            for i in range(len(self.map[key])): #loop through all timestamps
                timestamp = self.map[key][i][0]
                if timestamp == time: #replace at time with new value
                    self.map[key][i] = (time,value)
                    return
                elif timestamp > time: #insert value before next greater time
                    self.map[key].insert(i,(time,value))
                    return
            self.map[key].append((time,value)) #insert at end if time greater than all timestamps
        else:
            self.map[key] = list([(time,value)])

    #get
    #Note: returns value that is live at a given time,
    # if no live value returns None
    def get(self,key,time):
        if key in self.map.keys():
            prev_time = None
            prev_val = None
            for cur in self.map[key]:
                cur_time = cur[0]
                if time < cur_time:
                    return prev_val #returns None if no entry prior to passed time, else returns prior entry
                prev_time = cur_time
                prev_val = cur[1]
            return prev_val #if time greater than all entries, return latest entry
        return None #if doesn't have key, return None
        
### TESTS
d = Map()
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
print(d.get(1, 1)) # get key 1 at time 1 should be 1
print(d.get(1, 3)) # get key 1 at time 3 should be 2
e = Map()
e.set(1, 1, 5) # set key 1 to value 1 at time 5
print(e.get(1, 0)) # get key 1 at time 0 should be null
print(e.get(1, 10)) # get key 1 at time 10 should be 1
f = Map()
f.set(1, 1, 0) # set key 1 to value 1 at time 0
f.set(1, 2, 0) # set key 1 to value 2 at time 0
print(f.get(1, 0)) # get key 1 at time 0 should be 2
