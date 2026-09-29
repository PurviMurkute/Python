prices = [7,1,5,3,6,4]

def maxProfit(prices):
    maxP = 0

    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                maxP = max(profit, maxP)

    return maxP

print(maxProfit(prices))