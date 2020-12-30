class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = nums[0]
        mx = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            candidates = (nums[i], mx*nums[i], mn*nums[i])
            mx = max(candidates)
            mn = min(candidates)
            ans = max(ans, mx)
        return ans