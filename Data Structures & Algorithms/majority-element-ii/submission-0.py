class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = dict()

        for x in nums:
            counts[x] = counts.get(x, -(len(nums)/3)) + 1


        keys = [k for k, v in counts.items() if v > 0]
        return keys