class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = dict()
        threshold = len(nums)//3

        for x in nums:
            counts[x] = counts.get(x, 0) + 1


        keys = [k for k, v in counts.items() if v > threshold]
        return keys