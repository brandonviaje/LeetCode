class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        """
        notes:
        - we are basically showing what the box looks like after rotating it 90 degrees and capturing what the stones look like when it falls from being rotated
        - if we have n rows and m cols, then when we tilt it 90 we will have m rows and n cols this time
        - simulate the stones falling once flipping the rows and cols, transpose matrix
        - after transposing the matrix, simulate the stones falling

        falling logic:
        - if theres a stone, and you look down and its empty, swap values. 
        - if theres a stone there or stationary obstacle then it cant go fall down further

        steps:
        - transpose original matrix
        - simulate the falling
        """

        ROWS,COLS = len(boxGrid),len(boxGrid[0])
        transpose = [[] for i in range(COLS)]

        # Rotate matrix 90 degrees CW
        for i in range(COLS):
            for j in range(ROWS):
                transpose[i].insert(0,boxGrid[j][i])

        print(transpose)

        # Simulate the falling 
        
        # start from bottom up to simualte the falling
        for row in range(len(transpose)-1,-1,-1):
            for col in range(len(transpose[0])):
                # check if something is a stone
                if transpose[row][col] == "#":
                    # check below it is an empty cell
                    length = 1
                    while row + length < len(transpose) and transpose[row+length][col] == ".":
                        length += 1
                    # swap values, to simulate it falling
                    transpose[row][col],transpose[row+length-1][col] = transpose[row+length-1][col],transpose[row][col]

        return transpose

        # O(m*n) S O(m*n)
