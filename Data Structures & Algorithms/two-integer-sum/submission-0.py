class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #integer -> integer
        # [3,4,5,6] 7         
        # do you need two exactly, or can be 3 number sums (check the topic)
        # [1,2,3,4,5,6] 8 => [1,3]
        # [1,2,3] 3 => [0,1]
        #brute force, hashmaps, i wanna create a dictionary for nums, where i can hold keys and values 
        
        #brute force option, O(n^2), O(n) = O(1)
        # we are going through the entire array of length and 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return [] 

        # hashmap option
        # twosum = {}

        # for i in range(len(nums)):
        #     count(nums[i]) == 1 + count.get(nums[i], 0)

                