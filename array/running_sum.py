class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = 0
        result = []
        for i in nums:
            result.append(i + count)
            count += i
        return result
