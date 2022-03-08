#1232. Check If It Is a Straight Line  - Time complexity O(n)

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]

        x2 = coordinates[1][0]
        y2 = coordinates[1][1]

        dx = x2 - x1
        dy = y2 - y1

        for i in range(len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]

            if dx * (y - y1) != dy * (x - x1):
                return False
            
        return True
                

