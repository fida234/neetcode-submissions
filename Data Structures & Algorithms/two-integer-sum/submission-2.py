class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i in range(len(nums)):
            need=target-nums[i]
            if need in d:
                return[d[need],i] 
            d[nums[i]] = i#key access the thing written inside [] directly so the [nums[i]] access every elwmnt in the list and = is the value so value is i that is index
obj = Solution()
print(obj.twoSum([3,4,5,6],7))
                   
                
           