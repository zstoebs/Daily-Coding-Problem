"""
@author Zach Stoebner
@date 5-14-2020
@details You’re tracking stock price at a given instance of time. Implement an API
with the following functions: add(), update(), remove(), which adds/updates/removes a
datapoint for the stock price you are tracking. The data is given as (timestamp, price),
where timestamp is specified in unix epoch time.

Also, provide max(), min(), and average() functions that give the max/min/average of all
values seen thus far.
"""

import time

# API
# main function implementing the API for a stock tracker
def API():
    commands = """
                {"add": ["price: float"],
                "update": ["timestamp: int", "new_price: float"],
                "remove": ["timestamp: int"],
                "max": "returns max price in datapoints",
                "min": "returns min price in datapoints",
                "average": "returns average price of all datapoints",
                "print": "prints the tracker info"}
                """
    trackers = {}

    while True:
        name = input("Enter the name of the stock or 'end' to end the program: ")

        if name == "end":
            break

        if not name in trackers.keys():
            trackers[name] = Stock_Tracker(name)

        print()
        print(commands)
        print()
        comm = input("Enter a command in the form '<command> [arg1] [arg2] ...' (e.g. 'add 1516.34') or 'end': ")

        if comm == 'end':
            break

        args = comm.split()
        fnc = args[0]
        if fnc == "add":
            if len(args) != 2:
                print("Incorrect number of arguments.")
            else:
                price = float(args[1])
                print(trackers[name].add(price))
        elif fnc == "update":
            if len(args) != 3:
                print("Incorrect number of arguments.")
            else:
                timestamp, new_price = int(args[1]), float(args[2])
                print(trackers[name].update(timestamp,new_price))
        elif fnc == "remove":
            if len(args) != 2:
                print("Incorrect number of arguments.")
            else:
                timestamp = float(args[1])
                try:
                    print(trackers[name].remove(timestamp))
                except BufferError as e:
                    print(e.message)
        elif fnc == "max":
            print(trackers[name].max())
        elif fnc == "min":
            print(trackers[name].min())
        elif fnc == "average":
            print(trackers[name].average())
        elif fnc == "print":
            print(trackers[name])
        else:
            print(fnc + " is not a command.")

        print()

class Stock_Tracker:

    def __init__(self, name: str):
        self.name = name
        self.data = {}

    def add(self, price: float):
        # getting the struct time
        stime = time.localtime()
        # getting the unix epoch time
        timestamp = time.mktime(stime)
        self.data[timestamp] = price
        return (timestamp, price)

    # timestamp must be in unix epoch time
    def update(self, timestamp: int, new_price: float):
        # updates price or adds a new price if timestamp didn't exist before
        self.data[timestamp] = new_price
        return (timestamp,  new_price)

    def remove(self, timestamp: int):
        if not timestamp in self.data.keys():
            raise BufferError("Underflow: " + timestamp + " is not a datapoint.")

        datapoint = (timestamp, self.data[timestamp])
        del self.data[timestamp]
        return datapoint

    def max(self):
        return max(self.data,key=self.data.get)

    def min(self):
        return min(self.data,key=self.data.get)

    def average(self):
        sum = 0
        for key in self.data.keys():
            sum += self.data[key]

        return sum / len(self.data)

    def __str__(self):
        return self.name + "\n" + str(self.data)

if __name__ == "__main__":
    API()
