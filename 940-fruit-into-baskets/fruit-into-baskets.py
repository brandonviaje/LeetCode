class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        dynamic sliding window

        shrink: if there are more than two distinct types of fruit
        expcand: if the current fruit they're on is in basket already

        - capture max result after
        - they have to be the same type, can only hold a single type of fruit

        [3,3,3,1,2,1,1,2,3,3,4]
                             ^
                         ^
        basket = {'3':2, '4' : 1}
        result = 5
        """

        basket = defaultdict(int)
        result = 0
        l,r = 0,0

        while r < len(fruits):
            # incremenet to count
            basket[fruits[r]] += 1
            
            # shrink when there's more than two types of fruits, whatever fruit hits 0 first is not in the window anymore
            # u will now have 2 distinct fruits again
            while len(basket) > 2:
                # decrease count
                basket[fruits[l]] -= 1
                
                # delete from basket if it hits 0
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]

                l += 1

            result = max(result, r-l+1)
            r += 1

        return result