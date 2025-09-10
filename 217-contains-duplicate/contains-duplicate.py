class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Create a visited set to keep track of membership
        visited = set()

        for num in nums:
            
            # if u encounter the number again, theres a duplicate
            if num in visited:
                return True

            # add all the first time seen numbers
            visited.add(num)

        return False
        

        # T O(N) S O(M), where N is the number of elements in the array and M is the distinct numbers