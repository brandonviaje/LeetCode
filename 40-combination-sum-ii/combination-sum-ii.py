class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(index,path,total):
            # base case
            if total == target:
                result.append([elem for elem in path])
                return
            if total > target:
                return

            for i in range(index,len(candidates)):
                # check for dupes
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                # add
                path.append(candidates[i])
                backtrack(i+1,path,total+candidates[i]) # recurse down 
                path.pop() # backtrack

        
        backtrack(0,[],0)
        return result