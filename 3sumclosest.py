#https://leetcode.com/problems/3sum-closest/description/

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         diff = 100000
#         res = 0
#         for i in range(len(nums) - 2):
#             left = i + 1
#             right = len(nums) - 1
#             while left < right:
#                 s = nums[i] + nums[left] + nums[right]
#                 if abs(target - s) < diff:
#                     diff = abs(target - s)
#                     res = s
#                 if s < target:
#                     left += 1
#                 else:
#                     right -= 1
#         return res