# 953. Verifying an Alien Dictionary

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
   
        order_list = {c: i for i, c in enumerate(order)}
        
        for index in range(len(words)-1):
            word1 = words[index]
            word2 = words[index+1]
            minLength = min(len(word1), len(word2))

            if(word1[:minLength] == word2[:minLength]) and (len(word1) > len(word2)):
                return False
            
            for i in range(minLength):
                if word1[i] != word2[i]:
                    if order_list[word1[i]] > order_list[word2[i]]:
                        return False
                    break
        return True
