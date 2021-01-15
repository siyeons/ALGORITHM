class Solution: 
    def rob(self, nums: List[int]) -> int: 
        if not nums: 
            return 0 
        s = [nums[i] for i in range(len(nums))] 
        for i in range(1, len(nums)): 
            if i == 1: s[1] = max(s[1], s[0]) 
            else: s[i] = max(s[i-1], s[i] + s[i-2]) 
        return s[len(nums)-1]