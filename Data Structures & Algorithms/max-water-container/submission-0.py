class Solution:
    def maxArea(self, l: List[int]) -> int:
        left = 0
        right = len(l)-1
        max_ = 0
        while left<right:
            indexdiff = right-left
            containerwithshorter = min(l[left],l[right])
            maximumamount = indexdiff*containerwithshorter
            max_ = max(max_,maximumamount)
            if l[left] <l[right]:
                left+=1
            else:
                right-=1
        return max_
obj = Solution() 
print(obj.maxArea( [1,7,2,5,4,7,3,6]))               

        