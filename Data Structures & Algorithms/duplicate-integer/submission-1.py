class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for zahl in nums:
            if zahl in seen:
                return True
            else:
                seen.add(zahl)
        return False