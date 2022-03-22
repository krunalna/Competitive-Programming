#35. Search Insert Position


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        left, right = 0, len(nums)-1
        
        while left<=right:
            
            mid = left+ (right-left)//2
            print(mid)
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
                
            else:
                return mid
    
        return left 