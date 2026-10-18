class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counts = dict()

        for x in nums:
            counts[x] = counts.get(x, 0) + 1

            max_counts = max(counts, key=counts.get)
        return max_counts
