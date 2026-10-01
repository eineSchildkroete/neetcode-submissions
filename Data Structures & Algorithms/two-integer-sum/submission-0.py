class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gesehen = dict()

        for index, wert in enumerate(nums):
            fehlend  = target - wert
            if fehlend in gesehen:
                return [gesehen[fehlend], index]
            gesehen[wert] = index
        