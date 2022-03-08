# 350. Intersection of Two Arrays II

# Time complexity = O(m+n)  - m and n are lengths of the arrays

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        hashmap1 = {}
        
        for num in nums1:
            hashmap1[num] = hashmap1.get(num, 0) + 1
        
        res = []
        for num in nums2:
		    # If num not in hashmap, flag returns 0 by default and if exists, it returns the count it appears in list
            flag = hashmap1.get(num, 0)
			
			# true if more than 0
            if flag:
                res.append(num)
                hashmap1[num] -= 1
                
        return res
        

