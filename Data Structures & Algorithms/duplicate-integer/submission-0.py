class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # We do have brute force(loop, iterate through all input values) option, hash map option
        # declare variable with empty array and take input from user?
        # map through each given integer into the loop
        # check/compare each integers if they have same copy in the array
        # if yes return true, else return false

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False