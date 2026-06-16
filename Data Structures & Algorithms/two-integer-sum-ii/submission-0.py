class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        while left<right:
            currentsum = numbers[left]+numbers[right]
            if currentsum<target:
                left+=1
            elif currentsum>target:
                right-=1
            elif currentsum==target:
                return [left+1,right+1]
obj =  Solution()
print(obj.twoSum([1,2,3,4],3))                 
            
        