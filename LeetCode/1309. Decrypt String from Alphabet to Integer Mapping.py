#1309. Decrypt String from Alphabet to Integer Mapping

#Detailed Explanation : https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/discuss/1820897/Python-Easy-Solution-w-chr()-ord()-Explained

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        i = len(s)-1
        
        while i >=0:
            
            if s[i] == "#":
                val = chr(int(s[i-2:i])+ord("a")-1)
                res.append(val)
                i -=3
            else:
                val = chr(int(s[i])+ord("a")-1)
                res.append(val)
                i -=1
                
        return "".join(x for x in res[::-1]) 
        
