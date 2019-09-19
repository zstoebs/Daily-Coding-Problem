"""
@author Zach Stoebner
@date 9-18-2019
@descrip Given an array of numbers representing the stock prices of a
  company in chronological order and an integer k, return the maximum
  profit you can make from k buys and sells. You must buy the stock
  before you can sell it, and you must sell the stock before you can
  buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""
#The trader doesn't have to buy chronologically. If they only have k=1 buys and sells,
# then they can prioritize whichever margin is most profitable, whether it be later or earlier

#max_profit
#Note: returns the max profit from k buys and sells
#Complexity: O(n)
def max_profit(stocks,k):

    #can't buy and sell if only one stock price
    assert len(stocks) > 1

    #computing price differences
    diffs = list([])
    prev = stocks[0]
    for stock in stocks[1:]:
        diffs.append(stock-prev)
        prev = stock

    #computing profit margins for periods of buy and sell
    i = 0
    margins = list([])
    cur_margin = 0
    while i < len(diffs):
        margin = diffs[i]
        if cur_margin + margin > cur_margin:
            cur_margin += margin
        elif cur_margin != 0:
            margins.append(cur_margin)
            cur_margin = 0
        i += 1

    #adding if last element was profit
    if cur_margin > 0:
        margins.append(cur_margin)

    #counting profit
    profit = 0
    while k > 0 and len(margins) > 0:

        #checking if margins can compare for max value
        if len(margins) > 1:
            cur_best = max(margins)
        else:
            cur_best = margins[0]

        profit += cur_best
        margins.remove(cur_best)
        k -= 1

    return profit

### TESTS
stocks = [5, 2, 4, 0, 1]
print(max_profit(stocks,2)) #3
stocks = [1,2,3,4,5]
print(max_profit(stocks,1)) #4
stocks.reverse()
print(max_profit(stocks,1)) #0
