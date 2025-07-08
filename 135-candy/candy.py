class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        """
        [  4  9  8  7  6  ]
             ^
        
        [  4  7  8  9  6  11]
                 ^
                    ^
        
        [  1  1  2  3  1  1  ]
        
        [ 1 3 2 1]
        
        ratings:
        [7  3   2   1]
        
        candies:
        [5   4   3   1]
        
        note:
        - greedy
        - check if node has left or right neighbour
        - [1] * n , where n is length of ratings
        - right neighbour has a higher rating or vice versa 
        - one or two pass, two pass to check right neighb and then second pass is to check left neighb
        
        [1,0,2]
        
        [2 1 2]
        """
        candy = [1] * n
        
        #  update left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        
        print(candy)
        
        # update from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # make sure left candy has more candy than the right prev one
                candy[i] = max(candy[i], candy[i + 1] + 1)
                
        print(candy)
        
        return sum(candy)
        
        # T O(n) S O(n)