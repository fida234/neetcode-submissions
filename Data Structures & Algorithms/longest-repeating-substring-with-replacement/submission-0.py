class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        d = {}
        maxlen = 0
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
            mostfreq = max(d.values())
            windowslen = i-left+1
            changesneeded = windowslen-mostfreq
            while changesneeded>k:
                d[s[left]] -= 1
                if d[s[left]]==0:
                    del d[s[left]]
                left+=1    
   
                mostfreq = max(d.values())
                windowslen = i-left+1
                changesneeded = windowslen-mostfreq
            maxlen = max(windowslen,maxlen) 
        return maxlen
obj = Solution()
print(obj.characterReplacement( "XYYX", 2))        


