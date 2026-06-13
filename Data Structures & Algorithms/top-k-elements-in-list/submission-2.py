class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
          d = {}
          frequent = 0
          m = []
          for i in nums:
               d[i]= d.get(i,0)+1
          pairs = list(d.items())
          pairs.sort(key=lambda x:x[1] , reverse=True)
          actual = pairs[:k]
          result = []
          for value,key in actual:
               result.append(value)
          return result     
               
                      

obj = Solution() 
print(obj.topKFrequent([1,2,3,3,3,4,4,4,4], k = 2))         
        
     


