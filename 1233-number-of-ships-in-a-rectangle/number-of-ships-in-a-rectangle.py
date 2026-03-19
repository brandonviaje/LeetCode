# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y


"""
constraint: you can't have more than 400 calls of hasShips(),
will have to prune the search space in order to reduce the number of calls
with a divide and conquer approach, we recursively divide an area into four quadrants
we can then add up all quadrants found together to get how many ships there are while also reducing the number of API calls.
"""
class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # base cases: empty, invalid and single point
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1

        # divide area into 4 quadrants
        midX = (bottomLeft.x + topRight.x) // 2
        midY = (bottomLeft.y + topRight.y) // 2

        # recursively explore each quadrant for ships
        return (self.countShips(sea, Point(midX, midY), bottomLeft) + 
                self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1)) + 
                self.countShips(sea, Point(topRight.x, midY), Point(midX + 1, bottomLeft.y)) +
                self.countShips(sea, topRight, Point(midX + 1, midY + 1))               
                )