class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_arr = []
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (nums[i] > nums[j]):
                    count += 1
            new_arr.append(count)
            count = 0
        return new_arr