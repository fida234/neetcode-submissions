class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = ""

        for i in s:
            if i.isalnum():
                ch+=i.lower()
        if ch[::-1] == ch:
                return True
        else:
                return False   
             
obj = Solution()      
print(obj.isPalindrome("Was it a car or a cat I saw?"))   

          
                                     
        