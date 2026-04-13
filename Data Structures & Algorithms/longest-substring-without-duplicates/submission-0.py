class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Charset = set()
        l = 0
        r= 0
        res =0
        while r<len(s):
            while s[r] in Charset:
                Charset.remove(s[l])
                l+=1
            Charset.add(s[r])
            res = max(res,r-l+1)
            r+=1
        return res
                
