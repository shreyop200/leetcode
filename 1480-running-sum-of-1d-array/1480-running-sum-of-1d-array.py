class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final = list(nums)
        final[0] = nums[0]
        
        for i in range(1, len(nums)):
            final[i] = nums[i]+final[i-1]
            
        return final