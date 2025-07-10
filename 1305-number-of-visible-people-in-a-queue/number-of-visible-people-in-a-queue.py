class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result = [0] * len(heights)

        """
        [10 6 8 5 11 9]
          ^
                     ^
            ^
        [1]

        while there is someone on the stack and their height is less than or equal to the current person's height
        this means the person at stack[-1] can see the current person but their view is now blocked by the current taller or equal person, so they are popped
        """

        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                result[stack.pop()] += 1

            # if there's still someone on the stack, they're taller than the current person
            if stack:
                result[stack[-1]] += 1

            # push current person's index to be considered for the next ones
            stack.append(i)
        
        return result