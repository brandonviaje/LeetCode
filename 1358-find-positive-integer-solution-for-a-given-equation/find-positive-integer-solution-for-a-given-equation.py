"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        """
        since we have to reverse engineer it, we can do this by using z
        since function is monotonically increasing, we can use binary search
        to help us eliminate values that wouldn't be possible

        integers are positive, so our startin val is 0, up to inf basically

        we can do an iterative approach where we test every val x,y 
        """
        result = []
        x,y = 1, z

        while x <= z and y > 0:
            
            # check if curr value equals z
            if customfunction.f(x,y) == z:
                result.append([x,y])
                x += 1
                y -= 1
            elif customfunction.f(x,y) > z: # if greater than, reduce y
                y -= 1
            else:                           # if less than, increase x
                x += 1

        return result