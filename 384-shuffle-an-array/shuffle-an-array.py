class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.og = list(nums)

    def reset(self) -> List[int]:
        self.nums = self.og
        self.og = list(self.og)
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            idx = random.randrange(i, len(self.nums))
            self.nums[i],self.nums[idx] = self.nums[idx], self.nums[i]

        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

"""
brute force:
one way to shuffle the array is generate all permutations of the given array, and then add them to a list
and randomly pick out of that array. requires backtracking O(2^n) complexity


"""