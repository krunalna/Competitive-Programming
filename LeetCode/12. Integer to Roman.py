#12. Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        symbolList =  [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400], ["D",500],["CM",900], ["M",1000]]
        
        result = ""
        for key, value in reversed(symbolList):
            
            if num//value:
                
                count = num//value
                result += (key*count)
                num = num%value
                
        return result
                