class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char = ""
        for i in range(len(s)):
            if(s[i]=="(" or s[i]=="{" or s[i]=="["):
                stack.append(s[i])
            if stack: 
                if (s[i]==")"):
                    if(stack[-1]=="("):
                        stack.pop()
                    else:
                        return False
                elif (s[i]=="]"):
                    if(stack[-1]=="["):
                        stack.pop()
                    else:
                        return False
                elif (s[i]=="}"):
                    if(stack[-1]=="{"):
                        stack.pop()
                    else:
                        return False
            else:
                return False
        return not bool(stack)