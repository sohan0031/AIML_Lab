from collections import deque

def water_jug_problem(jug1_cap, jug2_cap, target):
    # Start with both jugs empty
    queue = deque([(0, 0, [])])
    visited = set([(0, 0)])

    while queue:
        jug1, jug2, path = queue.popleft()
        path = path + [(jug1, jug2)]

        # Check if target is reached
        if jug1 == target or jug2 == target:
            return path

        # Possible next states
        next_moves = []

        # Fill Jug 1
        next_moves.append((jug1_cap, jug2))
        # Fill Jug 2
        next_moves.append((jug1, jug2_cap))
        # Empty Jug 1
        next_moves.append((0, jug2))
        # Empty Jug 2
        next_moves.append((jug1, 0))
        # Pour Jug1 → Jug2
        pour = min(jug1, jug2_cap - jug2)
        next_moves.append((jug1 - pour, jug2 + pour))
        # Pour Jug2 → Jug1
        pour = min(jug2, jug1_cap - jug1)
        next_moves.append((jug1 + pour, jug2 - pour))

        # Add valid next moves
        for next_jug1, next_jug2 in next_moves:
            if (next_jug1, next_jug2) not in visited:
                visited.add((next_jug1, next_jug2))
                queue.append((next_jug1, next_jug2, path))

    return None


# --- Input ---
jug1_cap = int(input("Enter capacity of Jug 1: "))
jug2_cap = int(input("Enter capacity of Jug 2: "))
target_amount = int(input("Enter target amount: "))

# --- Solve ---
solution_path = water_jug_problem(jug1_cap, jug2_cap, target_amount)

# --- Output ---
if solution_path:
    print(f"\n✅ Path to measure {target_amount} liters:\n")
    for i, (j1, j2) in enumerate(solution_path):
        print(f"Step {i}: (Jug1 = {j1}, Jug2 = {j2})")
    print(f"\nTotal steps: {len(solution_path) - 1}")
else:
    print(f"\n❌ No solution found for target {target_amount}.")
