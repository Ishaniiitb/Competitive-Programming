#https://leetcode.com/problems/3sum/description/

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         count=0
#         res=[]
#         for i in range(len(nums)-2):
#             s=-nums[i]
#             begin=i+1
#             last=len(nums)-1
#             ans=nums[begin]+nums[last]
#             while(begin<last):
#                 if (ans==s and begin!=last):
#                     a=[nums[i],nums[begin],nums[last]]
#                     if a not in res:
#                         res.append(a)
#                     begin=begin+1
#                     ans=nums[begin]+nums[last]
#                 elif(ans>s):
#                     last=last-1
#                     ans=nums[begin]+nums[last]
#                 elif(ans<s):
#                     begin=begin+1
#                     ans=nums[begin]+nums[last]
#         return res