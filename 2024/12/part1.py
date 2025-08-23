from collections import deque



def bfs(grid, start):
    visitado = set()
    q = deque([start])
    visitado.add(start)

    while q:
        i, j = q.popleft()
        print(f"Visitando: ({i}, {j}) valor: {grid[i][j]}")

        # process neighbors
        for di, dj in neightbors(grid, i, j, grid[start[0]][start[1]]):
            if (di, dj) not in visitado:
                visitado.add((di, dj))
                q.append((di, dj))

    return visitado


def neightbors(node):
    row, col = node
    return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]


def is_valid_node(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


grid =  list(map(list,open("large.txt").read().split("\n")))
rows, cols = len(grid), len(grid[0])
regions = []
seen = set()

for r in range(rows):
    for c in range(cols):
        current_node = (r,c)
        if current_node not in seen:
            seen.add(current_node)
            region_actual = set()
            region_actual.add(current_node)

            #BFS
            q = deque([current_node])
            flower_type = grid[r][c]

            while q:
                node = q.popleft()
                for neighbor in neightbors(node):
                    if not is_valid_node(grid, neighbor[0], neighbor[1]): continue
                    if grid[neighbor[0]][neighbor[1]] != flower_type: continue
                    if neighbor not in region_actual:
                        seen.add(neighbor)
                        q.append(neighbor)
                        region_actual.add(neighbor)
            
            regions.append(region_actual)


def perimeter(region: set) -> int:
    total = 0
    for node in region:
        node_neightbors = neightbors(node)
        # check how many are in the region
        number_of_neighbors = 0
        for neighbor in node_neightbors:
            if neighbor in region:
                number_of_neighbors += 1
        total += (4 - number_of_neighbors)
    return total


print("Total regions:", len(regions))
print(sum(len(region) * perimeter(region) for region in regions))