class Solution:
    
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(index,path):
            # base case
            if len(path) >= k:
                result.append([elem for elem in path])
                return

            for i in range(index,n+1):
                path.append(i) # add
                backtrack(i+1,path) # recurse
                path.pop() # backtrack
        
        backtrack(1,[])
        return result
        