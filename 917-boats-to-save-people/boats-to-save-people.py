class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        - given an arr where arr[i] is the weight of each person
        - each boat can carry a max weight of limit
        - each boat carries <= 2 people at the same time if sum of weight is <= limit
        - find min number of boats to carry every person
        - the weight of a person is at most the limit

        limit: 5
        [3,3,4,5]
         ^
           ^
        boats:4

        intuition: you wanna fit 2 ppl on a boat as much as you can in order to reduce the amount of boats needed
        - sorting might help here, as when you start you will get the smaller magnitude first
        - start off with 1 person, if they can fit

        pattern:
        - i think this is a greedy problem because we want as much ppl on the boat as possible (in this case 2)
        - in addition, two pointers because we are working with an array, and also its in the problem list
        - i think its two pointers because we are dealing with max 2 ppl at the same time, so it would be appropriate to use this for best space

        procedure:
        - sort the array first, set boats to len(arr)
        - left pointer and right will converge
        - if sum of left and right is > limit, decrease the right pointer
        - if sum of left and right is < limit, increase left to explore more

        [1,2]
         ^
           ^

        weight = 3
        boats = 1
        """

        people.sort()
        l, r = 0, len(people)-1
        boats = len(people)

        while l<r:
            weight = people[l] + people[r]
            if weight <= limit:
                boats -= 1
                # update pointer
                l += 1
                r -= 1
            elif weight > limit:
                r -= 1
            else:
                l += 1
            
        return boats

        # T O(n) S O(1)
