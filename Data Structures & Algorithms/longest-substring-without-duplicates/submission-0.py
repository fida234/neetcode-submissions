class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left]) 
                left+=1
            seen.add(s[right]) 
            length = right-left+1
            max_len = max(max_len,length)   
        return max_len
obj = Solution() 
print(obj.lengthOfLongestSubstring("zxyzxyz"))            
             