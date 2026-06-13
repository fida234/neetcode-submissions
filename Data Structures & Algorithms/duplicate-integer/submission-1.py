class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        d={}
        for i in nums:
            d[i] = d.get(i,0)+1
        for key,value in d.items():
            if value >= 2:
                return True
                break
        else:
            return False        

obj = Solution()      
print(obj.hasDuplicate([1,2,3,4]))               
        