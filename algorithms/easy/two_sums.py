from typing import List

# n^2 complexity -> made it better in future
def twoSums(nums : List[int], target):
    for i in range(0, len(nums)):
        first = nums[i]
        second = target - first
        try:
            si = nums.index(second, i + 1)
        except ValueError:
            continue
        if si:
            return [i, si]

def twoSums_on(nums: List[int], target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i 

print(twoSums([2,7,11, 15], 9))
print(twoSums([3,2,4], 6))
print(twoSums([3,3], 6))
print(twoSums_on([2,7,11, 15], 9))
print(twoSums_on([3,2,4], 6))
print(twoSums_on([3,3], 6))
