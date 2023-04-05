#https://leetcode.com/problems/sum-of-square-numbers/description/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=int(c**0.5) #1
        i=0
        j=a #1
        while(i<a and i<j):
            if (i**2)+(j**2)>c:
                j=j-1
            elif i**2+j**2==c:
                return True
            else:
                i=i+1
        print(i,j,c)
        if (i**2+j**2==c):
            return True
        return False