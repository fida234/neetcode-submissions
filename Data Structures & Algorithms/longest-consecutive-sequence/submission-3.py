class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in s:
            if i-1 in s:
                continue
            else:
                current = i
                length = 1
                while current+1 in s:
                    current+=1
                    length+=1
                longest = max(length,longest)    
        return longest
obj = Solution() 
print(obj.longestConsecutive([0,3,2,5,4,6,1,1]
))               

                    
        