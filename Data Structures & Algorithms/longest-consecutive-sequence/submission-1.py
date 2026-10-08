class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [1,3,4,5,8,9] -> 3
        # [3,9,4,5,1,8] -> 3
        # O(n*logn) using sorting algorithm
        # O(n) -> Hash Table
        # I want to sort this array so that i can find the lined numbers and decide if 
        # (key,value)

        # count = 0

        # for i in nums:
        #     if (nums[i] = nums[i+1] - 1):
        #         count += 1
        #     else:
        #         count = 1
        
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest










