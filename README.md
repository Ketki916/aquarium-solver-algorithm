# aquarium-solver-algorithm

This algorithm solves the puzzle Aquarium (https://www.puzzle-aquarium.com/). The inputs are a rowMatrix (a list of lists containing each row of the puzzle, 
and each row contains the individual squares grouped into lists which represent their block), a columnMatrix (similar structure as the row matrix except it represents
each column of the puzzle), a rowSums matrix (contains a list of each row's total sum), and a columnSums matrix (contains a list of each column's total sum). Unfilled 
squares are represented by the string "unfilled", filled squares are represented by the string "filled", and squares that cannot be filled are labeled with "x" as
the algorithm is implemented.

The output is the finished rowMatrix which contains all the filled squares in the solution.
