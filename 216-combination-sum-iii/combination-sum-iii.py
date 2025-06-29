class Solution:
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(index,path,total):

            # base case
            if total == n and len(path) == k and path not in result:
                result.append([elem for elem in path])
                return
            if total > n:
                return
            
            for i in range(index,9+1):
                if i in path:
                    continue 

                # add
                path.append(i)
                backtrack(i+1,path,total + i)
                path.pop()
                # dont add
                backtrack(i+1,path,total)

        backtrack(1,[],0)
        return result