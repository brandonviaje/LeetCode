class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, 0, [], result)
        return result

    def backtrack(self, decisions, index, path, result):
        
        # Base Case: if our index reaches the length of decisions we have reached a subset
        if index >= len(decisions):
            result.append(path[:]) #add shallow copy to result list
            return

        # Choose to add an element
        path.append(decisions[index])
        self.backtrack(decisions, index + 1, path, result)# Recurse
        path.pop() # Backtrack 

        # Don't choose an element
        self.backtrack(decisions, index + 1, path, result)