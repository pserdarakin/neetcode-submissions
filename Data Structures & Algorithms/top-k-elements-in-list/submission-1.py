class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # I may sort and create dict? 

        counted = {}

        for num in nums:
            if num in counted:
                counted[num] += 1
            else:
                counted[num] = 1
        
        a = sorted(counted, key = counted.get, reverse=True)

        return a[:k]

            # I want to add nums [1, 2, 2, 3, 3, 3]
                                # . How many times each item is there
                                # counted = key, nums[i] = value in dict? if is not then start the count of that number as 1 














        # Integer + Integer -> Integer
        # My first question is "k" is counted together with the elements with nums, or the most frequent one has been already known and assigned as k?
        # nums = [1,2,2,3,3,3] k = 2, i want to return 2 most frequent elements.

        # Hashmap O(n*logn)

        # freq = {}

        # for i in nums:
        #     if i in freq:
        #         freq[i] += 1
        #     else:
        #         freq[i] = 1
        # a = sorted(freq, key = freq.get, reverse=True)
        # return a[:k]

        #how can i access the value of the freq dictionary so that i can sort that and get the biggest one or len(k) one to return as a result.



        

