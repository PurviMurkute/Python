prices = [7,1,5,3,6,4]

def maxProfit(prices):
    maximumProfit = 0
    minPrice = prices[0]

    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        if prices[i] > minPrice:
            profit = prices[i] - minPrice
            maximumProfit = max(profit, maximumProfit)

    return maximumProfit

print(maxProfit(prices))