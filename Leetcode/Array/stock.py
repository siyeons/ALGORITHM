def maxProfit(prices) -> int:
    max_price = 0
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            min_price = min(prices[i], prices[j])
            max_price = max((prices[j] - min_price), max_price)
    print(max_price)

maxProfit([7, 1, 5, 3, 6, 4])