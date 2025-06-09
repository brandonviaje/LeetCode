class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:



        for row in image:
  
            # reverse each row
            left = 0
            right = len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                #shift pointers
                left += 1
                right -= 1

            #invert each number with XOR operation
            i = 0
            while i < len(row):
                row[i] = row[i] ^ 1
                i += 1

        return image