class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i , r in enumerate(nums):
            diff = target - r
            
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[r]=i
        return
