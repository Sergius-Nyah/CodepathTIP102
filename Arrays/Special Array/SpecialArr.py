class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            # Check if adjacent elements are both even or odd
            if (nums[i] % 2 == 0 and nums[i+1] % 2 == 0) or (nums[i] % 2 != 0 and nums[i+1] % 2 != 0):
                return False
        return True
