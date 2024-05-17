from collections import deque

def water_jug_problem(Jug1_capacity, Jug2_capacity, target_amount):
    # BFS to find the solution
    def bfs():
        # To keep track of visited states
        visited = set()
        # Queue for BFS: (jug1, jug2, steps)
        queue = deque([(0, 0, 0)])  # Start with both jugs empty
        
        while queue:
            jug1, jug2, steps = queue.popleft()
            
            # If we reach the target amount in either jug, return the number of steps
            if jug1 == target_amount or jug2 == target_amount:
                return steps
            
            # If this state is already visited, skip it
            if (jug1, jug2) in visited:
                continue
            
            # Mark this state as visited
            visited.add((jug1, jug2))
            
            # Possible states from the current state
            next_states = [
                (Jug1_capacity, jug2),  # Fill Jug1
                (jug1, Jug2_capacity),  # Fill Jug2
                (0, jug2),              # Empty Jug1
                (jug1, 0),              # Empty Jug2
                (min(Jug1_capacity, jug1 + jug2), jug1 + jug2 - min(Jug1_capacity, jug1 + jug2)),  # Pour Jug2 into Jug1
                (jug1 + jug2 - min(Jug2_capacity, jug1 + jug2), min(Jug2_capacity, jug1 + jug2))   # Pour Jug1 into Jug2
            ]
            
            # Add the next states to the queue
            for state in next_states:
                if state not in visited:
                    queue.append((*state, steps + 1))
        
        # If no solution found
        return -1
    
    # Start BFS
    return bfs()

# Example usage
Jug1_capacity = 4
Jug2_capacity = 3
target_amount = 2

result = water_jug_problem(Jug1_capacity, Jug2_capacity, target_amount)
if result != -1:
    print(f"Minimum steps to get {target_amount} liters: {result}")
else:
    print("No solution found.")
