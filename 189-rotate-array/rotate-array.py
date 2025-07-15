from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        notes:
        - k always gonna be positive since u cant rotate something negatively
        - shift everything to the right, the very last elem moves to the front
        """

        while k > 0:
            h = nums.pop()
            nums.insert(0, h)
            k -= 1