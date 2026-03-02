import collections

def count_thermal_zones(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    zone_count = 0

    def bfs(r, c):
        queue = collections.deque([(r,c)])
        grid[r][c] = 0

        directions = [(1,0), (0,1), (-1, 0), (0,-1)]

        while queue:
            current_r, current_c = queue.popleft()

            for dr, dc in directions:
                nr, nc = dr + current_r, dc + current_c

                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                    queue.append((nr,nc))
                    grid[nr][nc] = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                zone_count += 1
                # TODO : Trigger BFS Here
                bfs(r,c)
    
    return zone_count

grid = [ [1, 0, 0], [1, 0, 0], [0, 0, 1] ]
print(count_thermal_zones(grid))