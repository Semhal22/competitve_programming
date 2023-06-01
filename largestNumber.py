class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not any(map(bool, nums)):
            return '0'

        nums = list(map(str, nums))
        if len(nums) < 2:
            return "".join(nums)
        
        def compare(x, y):
            return (int(nums[x] + nums[y])) > (int(nums[y] + nums[x]))

        for x in range(len(nums) - 1):
            y = x + 1
            while y < len(nums):
                if not compare(x, y):
                    nums[y], nums[x] = nums[x], nums[y]
                y += 1
        return "".join(nums)
