from collections import deque

def water_jug_problem(capacity_a, capacity_b, target):
    """
    Solves the water jug problem using BFS.

    Args:
        capacity_a: Capacity of jug A.
        capacity_b: Capacity of jug B.
        target: Target amount of water to measure.

    Returns:
        A list of tuples representing the sequence of states to reach the target,
        or None if no solution is found.
    """

    queue = deque([(0, 0, [])])  # (amount in A, amount in B, path)
    visited = set()

    while queue:
        current_a, current_b, path = queue.popleft()

        if (current_a, current_b) in visited:
            continue
        visited.add((current_a, current_b))

        if current_a == target or current_b == target:
            return path + [(current_a, current_b)]

        # Possible actions:
        # 1. Fill jug A
        queue.append((capacity_a, current_b, path + [(current_a, current_b)]))
        # 2. Fill jug B
        queue.append((current_a, capacity_b, path + [(current_a, current_b)]))
        # 3. Empty jug A
        queue.append((0, current_b, path + [(current_a, current_b)]))
        # 4. Empty jug B
        queue.append((current_a, 0, path + [(current_a, current_b)]))
        # 5. Pour A into B
        pour_amount = min(current_a, capacity_b - current_b)
        queue.append((current_a - pour_amount, current_b + pour_amount, path + [(current_a, current_b)]))
        # 6. Pour B into A
        pour_amount = min(current_b, capacity_a - current_a)
        queue.append((current_a + pour_amount, current_b - pour_amount, path + [(current_a, current_b)]))

    return None

if __name__ == "__main__":
    capacity_a = 4
    capacity_b = 3
    target = 2

    solution = water_jug_problem(capacity_a, capacity_b, target)

    if solution:
        print("Solution found:")
        for state in solution:
            print(state)
    else:
        print("No solution found.")