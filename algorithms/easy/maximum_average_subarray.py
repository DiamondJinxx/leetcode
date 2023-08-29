class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        answ = s
        for i in range(k, len(nums)):
            s += nums[i]
            s -= nums[i - k]
            answ = max(answ, s)
        return answ / k
