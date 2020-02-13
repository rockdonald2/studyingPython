def maxProfit(prices):
    profit = 0

    i = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]

        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]

        profit = (profit + (peak - valley))

    return profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
