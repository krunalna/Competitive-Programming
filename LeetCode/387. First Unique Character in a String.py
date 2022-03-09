#387. First Unique Character in a String

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap  ={}
        
        for char in s:
            hashmap[char] = hashmap.get(char,0)+1
            
        for char in s:
            if hashmap[char] == 1:
                return s.index(char)
            
        return -1
        

