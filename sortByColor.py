class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        
        for i in nums:
            counts[i] += 1
        
        colors = [0, 1, 2]
        index = 0
        for color in colors:
            for i in range(counts[color]):
                nums[index] = color
                index += 1