class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i in range(len(nums)):
            need=target-nums[i]
            if need in d:
                return[d[need],i] 
            d[nums[i]] = i
obj = Solution()
print(obj.twoSum([3,4,5,6],7))
                   
                
           