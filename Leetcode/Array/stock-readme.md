내가 푼 풀이 방법: Timeout이 뜬다 ㅜㅜ 시간복잡도가 O(n^2)이라서..

    def maxProfit(self, prices: List[int]) -> int:
          max_price = 0
          for i, price in enumerate(prices):
              for j in range(i, len(prices)):
                  min_price = min(prices[i], prices[j])
                  max_price = max((prices[j] - min_price), max_price)
          return max_price

Best Practice: 저점과 현재 값의 차이를 계산한다.

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
    	min_price = sys.maxsize
    	for price in prices:
    		min_price = min(min_price, price)
    		profit = max(profit, price - min_price)
    	return profit

- 최솟값은 sys.maxsize로, 최댓값은 -sys.maxsize로 초기화해보자!
