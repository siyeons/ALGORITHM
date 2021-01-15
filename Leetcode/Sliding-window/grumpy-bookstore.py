class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        sum = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                sum += customers[i]
            
        maxSum = sum
        for i in range(X):
            if grumpy[i] == 1:
                sum += customers[i]
        if sum > maxSum:
            maxSum = sum
            
        j = X
        i = 0
        while j < len(customers):
            if grumpy[j] == 1:
                sum += customers[j]
            if grumpy[i] == 1:
                sum -= customers[i]
            if sum > maxSum:
                maxSum = sum
            j += 1
            i += 1
        return maxSum