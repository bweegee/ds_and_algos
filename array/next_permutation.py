class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index_target = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                index_target = i
                
        if index_target == -1:
            nums.sort()
            return nums
        
        # check if there is a smaller weighted candidate after the least peak 
        index_to_swap = index_target - 1
        num_to_swap = nums[index_to_swap]
        for i in range(index_target, len(nums)):
            if nums[i] > num_to_swap and nums[i] < nums[index_target]:
                index_target = i
                
        nums[index_to_swap] = nums[index_target]
        nums[index_target] = num_to_swap
        nums[index_to_swap + 1 : len(nums)] = sorted(nums[index_to_swap + 1 : len(nums)])
        
        return nums
