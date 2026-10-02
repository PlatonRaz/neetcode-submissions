class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapA = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapA:
                return [mapA[diff], i]
            mapA[n] = i




        
        