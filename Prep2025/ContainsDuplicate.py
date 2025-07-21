"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.
"""
from operator import truediv


class ContainsDuplicate:
    def sol(self, nums: list[int]):

        counter = {}
        for i in range(len(nums)):
            if nums[i] in counter.keys():
                return True
            else:
                counter[nums[i]] = i
        return False
x = ContainsDuplicate()
nums = [1,2,3]
print(x.sol(nums))

