from collections import deque

def is_valid(state):
    m_left, c_left, _ = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or m_left > 3 or c_left < 0 or c_left > 3:
        return False
    if m_right < 0 or m_right > 3 or c_right < 0 or c_right > 3:
        return False
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    return True

def get_successors(state):
    successors = []
    m, c, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for dm, dc in moves:
        if boat == 0:
            new_state = (m - dm, c - dc, 1)
        else:
            new_state = (m + dm, c + dc, 0)
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [successor]))
    return None

start_state = (3, 3, 0)
goal_state = (0, 0, 1)

solution = bfs(start_state, goal_state)

if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")