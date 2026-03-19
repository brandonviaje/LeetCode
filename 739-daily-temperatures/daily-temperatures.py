class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            # while stack isnt empty and temp is warmer than prev
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # pop prev warmest
                index = stack.pop()
                result[index] = i - index 

            stack.append(i)
        
        return result