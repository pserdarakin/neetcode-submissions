class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# SECOND SUBMISSION
        # int -> int 
        # [3,4,5,6],key 7
        #  0 1 2 3  value
        #  nums[0] nums[1] = 7
        # return [0,1]
        # if sum = target
        # i would like to loop through the list
        # and add the numbers if its not equal to target
        dictt = {}

        for i in range(len(nums)):
            num = nums[i]
            need = target - num
            if need in dictt:
                return [dictt[need], i]
            else:
                dictt[num] = i














        #integer -> integer
        # [3,4,5,6] 7         
        # do you need two exactly, or can be 3 number sums (check the topic)
        # [1,2,3,4,5,6] 8 => [1,3]
        # [1,2,3] 3 => [0,1]
        #brute force, hashmaps, i wanna create a dictionary for nums, where i can hold keys and values 
        
        #brute force option, O(n^2), O(n) = O(1)
        # we are going through the entire array of length and 

# FIRST SUBMISSION
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        # return [] 

        # hashmap option
        # twosum = {}

        # for i in range(len(nums)):
        #     count(nums[i]) == 1 + count.get(nums[i], 0)

                