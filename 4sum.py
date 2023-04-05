#https://leetcode.com/problems/4sum/description/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        count=0
        res=[]
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                s=target-nums[i]-nums[j]
                begin=j+1
                last=len(nums)-1
                ans=nums[begin]+nums[last]
                while(begin<last):
                    if (ans==s and begin!=last):
                        a=[nums[j],nums[i],nums[begin],nums[last]]
                        if a not in res:
                            res.append(a)
                        begin=begin+1
                        ans=nums[begin]+nums[last]
                    elif(ans>s):
                        last=last-1
                        ans=nums[begin]+nums[last]
                    elif(ans<s):
                        begin=begin+1
                        ans=nums[begin]+nums[last]
        return res