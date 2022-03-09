# 709. To Lower Case

#method one - To re-implement the s.lower() method 

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        is_upper = lambda x: 'A' <= x <= 'Z'
        to_lower = lambda x : chr(ord(x) | 32)
        
        slist = []
        for x in s:
            if is_upper(x):
                slist.append(to_lower(x))
            else:
                slist.append(x)
        
        return "".join(slist)


#method2 : use in-built s.lower() method

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """

        return s.lower()



