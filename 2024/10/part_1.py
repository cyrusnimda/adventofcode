from collections import deque


def neightbors(node):
    row, col = node
    return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]


def is_valid_node(grid, node):
    row, col = node
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


grid = [[int(char) for char in line.strip()] for line in open("live.txt")]
rows, cols = len(grid), len(grid[0])

trails = []
trail_scores = {}

def get_trail_score(trail_node_head):
    score = 0
    seen = set()
    seen.add(trail_node_head)

    q = deque([trail_node_head])
    while q:
        node = q.popleft()
        node_value = grid[node[0]][node[1]]
        for neighbor in neightbors(node):
            if not is_valid_node(grid, neighbor): continue
            neighbor_value = grid[neighbor[0]][neighbor[1]]
            if neighbor_value != node_value +1: continue
            if neighbor in seen: continue
            seen.add(neighbor)
            if neighbor_value == 9:
                score += 1
                print("Found a path to 9:", neighbor)
            else:
                q.append(neighbor)
    return score



for r in range(rows):
    for c in range(cols):
        current_node = (r,c)
        if grid[r][c] == 0:
            # it is a trail
            trails.append(current_node)
            score = get_trail_score(current_node)
            trail_scores[current_node] = score

total_score = sum(trail_scores.values())
print(trail_scores)
print("Total trail score:", total_score)



