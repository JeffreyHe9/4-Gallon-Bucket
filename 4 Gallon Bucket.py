
from collections import deque
from typing import List, Tuple, Optional

# Creates a class that takes three parameters: capacities of two buckets and the target volume
class WaterBucketSolver:
    def __init__(self, bucket1_capacity: int, bucket2_capacity: int, target: int):
        self.bucket1_capacity = bucket1_capacity
        self.bucket2_capacity = bucket2_capacity
        self.target = target

# Takes two states (current and next) and determines what action was taken
# Uses pattern matching to identify actions
    def get_action_description(self, current: Tuple[int, int], next_state: Tuple[int, int]) -> str:
        """Generate a description of the action taken between states."""
        curr_3, curr_5 = current
        next_3, next_5 = next_state

        if curr_3 == 0 and next_3 == self.bucket1_capacity:
            return f"Fill the 3-gallon"
        elif curr_5 == 0 and next_5 == self.bucket2_capacity:
            return f"Fill the 5-gallon"
        elif curr_3 > 0 and next_3 == 0 and curr_5 == next_5:
            return f"Empty the 3-gallon"
        elif curr_5 > 0 and next_5 == 0 and curr_3 == next_3:
            return f"Empty the 5-gallon"
        elif curr_3 > next_3 and next_5 > curr_5:
            return f"Pour from 3-gallon to 5-gallon"
        elif curr_5 > next_5 and next_3 > curr_3:
            return f"Pour from 5-gallon to 3-gallon"
        return "Unknown action"

# Uses Breadth-First Search (BFS) to find the shortest solution
    def solve(self) -> Optional[List[Tuple[Tuple[int, int], str]]]:
        start_state = (0, 0)
        visited = {start_state}
        queue = deque([(start_state, [])])

        while queue:
            current_state, path = queue.popleft()
            bucket3, bucket5 = current_state

            if bucket3 + bucket5 == self.target:
                return path

            # Generate all possible next states
            next_states = []
            # Fill 3-gallon
            next_states.append((self.bucket1_capacity, bucket5))
            # Fill 5-gallon
            next_states.append((bucket3, self.bucket2_capacity))
            # Empty 3-gallon
            next_states.append((0, bucket5))
            # Empty 5-gallon
            next_states.append((bucket3, 0))
            # Pour from 3 to 5
            amount = min(bucket3, self.bucket2_capacity - bucket5)
            next_states.append((bucket3 - amount, bucket5 + amount))
            # Pour from 5 to 3
            amount = min(bucket5, self.bucket1_capacity - bucket3)
            next_states.append((bucket3 + amount, bucket5 - amount))

            for next_state in next_states:
                if next_state not in visited:
                    visited.add(next_state)
                    action = self.get_action_description(current_state, next_state)
                    queue.append((next_state, path + [(next_state, action)]))

        return None

# Print solution with step numbers, actions, and states
def print_solution(solution):
    for i, (state, action) in enumerate(solution, 1):
        print(f"{i}. {action:<30} {state}")


# Solve the problem
solver = WaterBucketSolver(3, 5, 4)
solution = solver.solve()

if solution:
    print_solution(solution)
else:
    print("No solution found!")