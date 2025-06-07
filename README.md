N-Queens Solver Using Genetic Algorithm
This project implements a genetic algorithm to solve the N-Queens problem, arranging N queens on an NxN chessboard such that no queens threaten each other (no shared rows, columns, or diagonals).
Problem Description

Goal: Place N queens on an NxN chessboard with no conflicts.
Solution Representation: A list of integers where the index is the row and the value is the column, ensuring one queen per row and column.
Fitness Function: Counts conflicts (column and diagonal). Returns a negative value, with 0 indicating an optimal solution.

Algorithm Details

Population: Initialized with random permutations, each representing a board arrangement.
Selection: Tournament selection (size 3) picks the best individual from a random subset, balancing diversity and quality.
Crossover: Ordered Crossover (OX) creates a child by copying a segment from one parent and filling the rest from the other, preserving permutation integrity. Safety checks ensure no missing values.
Mutation: Swaps two positions with a dynamic probability (0.05 + N*0.01, capped at 0.15). Local search is limited to 2 positions with 2 new positions to reduce computation.
Elitism: Retains the best individual each generation.
Stopping Criteria:
Maximum 1000 generations.
Fitness reaches 0 (optimal solution).
No improvement for 200 generations.


Progress Tracking: Records improvements for monitoring and debugging.

Performance

N=8: Typically finds a solution in 50-300 generations (5-30 seconds).
N=10: Often achieves 200-600 generations, sometimes with 1-2 conflicts.
N=12: Usually results in 1-3 conflicts after 1000 generations (1-2 minutes).

Parameter Sensitivity

Population Size (50):
Low (30): Risks premature convergence.
High (100): Slows computation.


Mutation Rate (Dynamic):
High (>0.3): Disrupts convergence.
Low (<0.05): Inhibits exploration.


Tournament Size (3):
Large (5-10): Reduces diversity.


Local Search: Reduces sensitivity to parameter tuning.

Pros and Cons

Pros:
Fast and reliable for N=8-10.
Near-optimal for N=12.
Progress monitoring aids debugging.


Cons:
Perfect solutions unlikely for N > 10.
Stochastic nature requires configuration.
Some parameter tuning needed.



Complexity

Time: O(pop_size * N^2) per generation.
N=8: Seconds.
N=12: 1-2 minutes.


Space: O(pop_size * N).

Resource Usage

Low for N ≤ 10.
Moderate for N=12.

Optimizations

Dynamic mutation rate adapts to board size.
Local search limits computation for large N.
Elitism ensures retention of the best solution.
Early stopping after 200 stagnant generations.

