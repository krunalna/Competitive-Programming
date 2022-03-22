#557. Reverse Words in a String III

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s.split(" "))
        res= []
        for item in slist:
            res.append(item[::-1])
        
        return " ".join(res)
            

