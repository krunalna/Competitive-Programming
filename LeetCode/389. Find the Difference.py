# 389. Find the Difference


#Bitwise
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # Initialize ch with 0, because 0 ^ X = X
        # 0 when XORed with any bit would not change the bits value.
        ch = 0

        # XOR all the characters of both s and t.
        for char_ in s:
            #print(ch, ord(char_), char_)
            ch ^= ord(char_)
            
        print()
        for char_ in t:
            #print(ch, ord(char_), char_)
            ch ^= ord(char_)

        # What is left after XORing everything is the difference.
        return chr(ch)



#Sort

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Sort both the strings
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        # Character by character comparison
        i = 0
        while i < len(s):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
            i += 1

        return sorted_t[i]