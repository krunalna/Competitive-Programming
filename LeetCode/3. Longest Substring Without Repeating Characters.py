# 3. Longest Substring Without Repeating Characters

#Method1 - Sliding Window  Time Complexity - O(n) & Space Complexity - O(n)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        res = 0 
        left = 0
        
        for right in range(len(s)):
            
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
                
            charSet.add(s[right])
            
            res = max(res, right-left+1)
            
        return res
            


# Method 2 : Optimized  Sliding Window
# 
# class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        n = len(s)
        i =0
        ans = 0
        hashmap = {}
        
        for j in range(n):
            if s[j] in hashmap:
                i = max(hashmap[s[j]], i)
            
            ans = max( ans, j-i+1)
            hashmap[s[j]] = j+1
            
        return ans       
        