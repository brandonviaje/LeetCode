class Solution:
    

            
    def letterCombinations(self, digits: str) -> List[str]:
        """
        generate all possible = backtracking
        if u want to explore all possible combos = backtrack
        base case
        
        """
        # if digits is empty return nothing
        if len(digits) == 0:
            return []
            
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y","z"]
        }
        def backtrack(index, path):
            #base case
            if index == len(digits):
                result.append(path[:])
                return
                
            # loop through each string backtrack after
            for l in phone[digits[index]]:
                backtrack(index + 1, path + l)
            
        result = []
        path = ""
        backtrack(0,path)
        return result