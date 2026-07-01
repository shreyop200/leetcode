class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final = list(nums)

        for i in range(1, len(nums)):
            final[i] += final[i-1]

        return final