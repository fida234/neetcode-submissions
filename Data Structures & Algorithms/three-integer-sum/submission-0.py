class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = sorted(nums)
        n = len(l)
        result = []
        for i in range(n):
            left =i+1
            right = n-1
            if i>0 and l[i] ==l[i-1]:
                continue
            while left<right:
                currentsum = l[i]+l[left]+l[right] 
                if currentsum < 0:
                    left+=1
                elif currentsum > 0:
                    right-=1
                else:

                    result.append([l[i],l[left],l[right]])
                    while left< right and l[left]==l[left+1]:
                        left+=1
                    while left < right and l[right]==l[right-1]:
                        right-=1
                    left+=1
                    right-=1

                        
        return result      
obj = Solution()  
print(obj.threeSum([-1,0,1,2,-1,-4]))                  




