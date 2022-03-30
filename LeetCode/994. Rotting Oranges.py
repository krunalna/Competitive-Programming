#994. Rotting Oranges

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows , cols = len(grid), len(grid[0])
        fresh_oranges = 0
        queue = []
        visited = set()
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] ==1:
                    fresh_oranges +=1
                    
        
        minutes = -1
        neighbours = [(1,0), (0,1),(-1,0),(0,-1)]
        queue.append((-1,-1))
        while queue:
            
            for _ in range(len(queue)):
                i,j = queue.pop(0)
                
                if i == -1:
                    if queue:
                        queue.append((-1,-1))
                    break
                
                for di, dj in neighbours:
                    ni = i+di
                    nj = j + dj
                    
                    if 0<=ni<rows and 0<=nj<cols and grid[ni][nj] == 1 and (ni,nj) not in visited:
                        grid[ni][nj] = 2
                        fresh_oranges -=1
                        queue.append((ni,nj))
                        visited.add((ni,nj))
                        
                        
            minutes +=1
            
        
        if fresh_oranges == 0:
            return minutes
        else:
            return -1
                
            
        