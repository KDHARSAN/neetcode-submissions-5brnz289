class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=set()
        n = len(s)
        l=0
        r=0
        length =0
        while r < n:
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            length = max(length,r-l+1) 
            r+=1
        return length
        





        