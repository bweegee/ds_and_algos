class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        
        for i in range(len(nums)):
            if hash.has_key(target - nums[i]):
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
