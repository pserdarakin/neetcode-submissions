class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # String -> String
        # example: strs = ["abc", "bbb", "ccc", "aax", "xxa"] => 
        # [["aax","xxa"],["abc"],["bbb"],["ccc"]]
        # I need to put this strs[i] inside of array, if it has anagram, put in the same array else just put in an array.
        # I need to check if they are anagram for each item
        # How frequent are they? 
    

        # for i in len(26):
        #     if len(strs[i]) != len(strs[i+1]):
        #         return False
        #     if i in 
        
        # Second Try
        # Array String -> Array of Array String
        # Constraints: need to be same number of letter, that includes overall word, and for each letter
        # loop through strs and then loop through each index will give me brute force, i ll have two loops which will end up in O(n^2)
        # How to use the dictionaries? hash map? to just do in one scan?
        # If i would use ASCII codes for each letter inside of the array and value ASCII codes and key would be letter ??
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())










        
