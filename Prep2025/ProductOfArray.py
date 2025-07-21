"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

class Solution:
    def productOfSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)

        LP = [1] * length
        RP = [1] * length
        res = [1] * length

        for i in range(1, len(nums)):
            LP[i] = nums[i-1] * LP[i-1]

        for i in range(len(nums)-2, -1, -1):
            RP[i] = nums[i+1] * RP[i+1]

        for i in range(len(nums)):
            res[i] = LP[i] * RP[i]
        return res


x = Solution()
nums = [1,2,3,4]
print(x.productOfSelf(nums))