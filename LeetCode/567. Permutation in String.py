# 567. Permutation in String

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False
        
        s1count = [0]*26
        s2count = [0]*26

        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')] +=1
            s2count[ord(s2[i])-ord('a')] +=1
            
        print(s1count)
        print(s2count)
        
        matches = 0
        
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches +=1
                
        print(matches)
        
        left = 0
        
        for right in range(len(s1), len(s2)):
            
            if matches ==26:
                return True
            
            index = ord(s2[right]) - ord('a')
            
            s2count[index]+=1
            
            if s1count[index] == s2count[index]:
                matches +=1
                
            elif s1count[index]+1 == s2count[index]:
                matches -=1
                
            index = ord(s2[left]) - ord('a')
            
            s2count[index] -=1
            
            if s1count[index] == s2count[index]:
                matches +=1
                
            elif s1count[index]-1 == s2count[index]:
                matches -=1
                
            left+=1
                
        return matches == 26