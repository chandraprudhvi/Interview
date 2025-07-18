'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4], [7,6,4,3,1, 100]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

class BestTimeToBuyAndSellStock:
    def solution(self, input: list[int]) -> int:

        p2 = 1
        p1 = 0
        maxprofit = 0

        while p2 < len(input):
            profit = input[p2] - input[p1]
            if (profit > 0):

                maxprofit = max(profit, maxprofit)
                p2 = p2 + 1
            else:
                p1 = p2
                p2 = p2+1

        return maxprofit



instance = BestTimeToBuyAndSellStock()
print(instance.solution([7,9,14,37,1, 10]))
