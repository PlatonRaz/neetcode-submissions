class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}

        for num in nums:
            count_dict[num] = 0

        for num in nums:
            if num or num == 0:
                count_dict[num] += 1
        
        for key in count_dict:
            if count_dict[key] > 1:
                return True

        return False
        