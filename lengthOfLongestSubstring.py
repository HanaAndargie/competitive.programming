class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        maxLength=0
        left=0
        
        for right, character in enumerate(s):
            if character in seen and seen[character]>=left:
                left=seen[character]+1
            else:
                maxLength=max(maxLength,right-left+1)
            seen[character]=right
        return maxLength
        
        
