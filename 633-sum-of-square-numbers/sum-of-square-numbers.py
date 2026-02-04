class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        [1,2,3,4]
         ^
               ^
        let l = 0 and r = sqrt(c)
        any number bigger than sqrt(c) is automatically bigger than c
        this reduces the search space

        sum_square = l**2 + r**2

        if sum_square == c: return True
        if sum_square > c: r-= 1
        elif sum_square < c: l += 1
        """ 
        
        l,r = 0, int(sqrt(c))

        while l<=r:
            curr_sum = l*l + r*r
            if curr_sum == c:
                return True 
            elif curr_sum < c:
                l += 1
            else:
                r -= 1

        return False

        # O(n)