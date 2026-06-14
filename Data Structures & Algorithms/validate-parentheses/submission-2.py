class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        match = {
    ')': '(',
    ']': '[',
    '}': '{'
              }
        balanced = True
        for i in s:

            if i in "[{(":
                stack.append(i)

             
            elif i in "]})":  

                if not stack:
                    return False
                   
                if stack[-1] != match[i]:
                    return False 

                stack.pop()
        if len(stack)==0:
   
            return True
        else:
            

            return  False    
  
obj  = Solution()   
print(obj.isValid("([{}])")) 






