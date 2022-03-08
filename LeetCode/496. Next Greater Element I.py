# 496. Next Greater Element I

#method 1 - Nested list   - Time complexity O(mn)

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        ans = []
        
        for element in nums1:
            idx = nums2.index(element)
            for i in range(idx, len(nums2)):
                if nums2[i] > element:
                    ans.append(nums2[i])
                    break
            else:
                ans.append(-1)
                
        return ans


#method2: Using Hashmap  - Time Complexity O(mn) 

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        hashmap = {}
        
        for idx, element in enumerate(nums2):
            hashmap[element] = idx

        for i in range(len(nums1)):
            for j in range(hashmap[nums1[i]]+1, len(nums2)):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
                
        return ans

#method3 : Using Stack and hashmap  - Time Complexity O(n)

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        hashmap = {}
        stack = []
        
        for i in range(len(nums2)):
            
            while stack and nums2[i]>stack[-1]:
                hashmap[stack.pop()] = nums2[i]
            
            stack.append(nums2[i])
            
        while stack:
            hashmap[stack.pop()] = -1
            
        ans = []
        
        for i in range(len(nums1)):
            ans.append(hashmap[nums1[i]])
            
        return ans
            