class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for x in nums.copy():
            if x == val:
                nums.remove(x)
        k = len(nums)
        return k