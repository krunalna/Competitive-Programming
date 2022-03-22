#167. Two Sum II - Input Array Is Sorted


#method1 - as array is sorted, this is a hint and we can try binary search



#Method2 - Linear time O(n)

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for idx, element in enumerate(numbers):
            
            if (target - element) in hashmap and idx != hashmap[target-element]:
                index2 = idx+1
                index1 = hashmap[target-element]+1
                return [index1, index2]

            hashmap[element] = idx
            
        
        print(hashmap)
        