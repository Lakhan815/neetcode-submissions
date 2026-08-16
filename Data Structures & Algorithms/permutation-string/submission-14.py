class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0, len(s1)-1
        res = False
        s1Dict = {}
        for char in s1:
            s1Dict[char] = s1Dict.get(char,0)+1
        while(r<len(s2)):
            s2Dict = {}
            for char in s2[l:r+1]:
                s2Dict[char] = s2Dict.get(char,0)+1
            if s1Dict==s2Dict:
                return True
            l+=1
            r+=1
        return res