class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in accounts:
            sumed = sum(i)
            if sumed > max:
                max = sumed
        return max