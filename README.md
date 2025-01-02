# 4-Gallon-Bucket

This Python program solves the classic water jug riddle using Breadth-First Search (BFS). Given two buckets of different capacities, it finds the shortest sequence of steps to measure a target amount of water.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)

## Description
This project implements a water bucket puzzle solver that:
- Finds the shortest solution using BFS algorithm
- Supports any two bucket capacities and target volume
- Generates clear step-by-step instructions
- Tracks visited states to avoid cycles
- Returns None if no solution exists

## Installation
1. Clone the repository:
```bash
git clone https://github.com/JeffreyHe9/4-Gallon-Bucket.git
```

2. No additional installation required - uses only Python standard library.

## Usage
```python
# Create solver instance (3-gallon bucket, 5-gallon bucket, target: 4 gallons)
solver = WaterBucketSolver(3, 5, 4)
solution = solver.solve()

# Print solution
if solution:
    print_solution(solution)
else:
    print("No solution found!")

Sample Output:
1. Fill the 5-gallon                   (0, 5)
2. Pour from 5-gallon to 3-gallon      (3, 2)
3. Empty the 3-gallon                  (0, 2)
4. Pour from 5-gallon to 3-gallon      (2, 0)
5. Fill the 5-gallon                   (2, 5)
6. Pour from 5-gallon to 3-gallon      (3, 4)
```

## How It Works

The program consists of three main components:

```python
class WaterBucketSolver:
    def __init__(self, bucket1_capacity, bucket2_capacity, target):
        # Initializes solver with bucket capacities and target

    def get_action_description(self, current, next_state):
        # Generates human-readable descriptions of actions

    def solve(self):
        # Implements BFS to find shortest solution path
```

The solver uses BFS to systematically explore possible states:
1. Fill either bucket
2. Empty either bucket
3. Pour from one bucket to another
4. Track visited states to avoid cycles
5. Return solution path when target is reached

## Contributing
You can contribute by:
1. Adding visualization features
2. Implementing multiple solution paths
3. Adding unit tests
4. Improving error handling
5. Enhancing documentation
