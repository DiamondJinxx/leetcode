from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, f in count.items():
            freq[f].append(n)

        result = []
        for i in range(len(nums) - 1, 0, -1):
            result.extend(freq[i])
            if len(result) >= k:
                result = result[:k]
                break
        return result
