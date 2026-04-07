class Solution:
    def isPalindrome(self, s: str) -> bool:
        strl = "".join(ch for ch in s if ch.isalnum()).lower()
        strr = list(strl)
        l = 0
        n= len(strr)
        r= n-1

        while l<r:
            strr[l],strr[r] = strr[r],strr[l]
            l+=1
            r-=1
        ri = "".join(strr)

        if ri == strl:
            return True 
        else:
            return False


