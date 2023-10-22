class Solution(object):
    def twoSum_1(self, nums, target):
        """
        Brute force solution
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_2(self, nums, target):
        """
        Optimized solution
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        latest_indexes = {}
        for i in range(len(nums)):
            if (target - nums[i] in nums) and (i!=nums.index(target - nums[i])):
                latest_indexes[i] = nums.index(target - nums[i])
        return [latest_indexes.keys()[0], latest_indexes.values()[0]]
