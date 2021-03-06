#cs221_project

Objective:

For a given chess puzzle, can we develop an engine that would find the optimal solution. We are going to develop a chess engine that would solve puzzles optimally with the FEN string as
input and output being the subset of moves.

Solution:
By leveraging the python-chess library, we used FENs as inputs to our agent the agent uses the min-max algorithm to determine the best optimal moves.

Tech/framework used:
We have used python-chess as our frameworkpython-chess is a pure Python chess library with move generation, move validation and support for common formats.

Input:

Input: A string (FEN), list of moves by Oracle, the color to move next.
We also developed a PGN reader which reads a PGN puzzle file, which reads the file, performs the data cleanup and returns a lot of puzzles which is used by the engine to solve it.

We also separated the set of puzzles as use cases which have mate in two, three or four steps to evaluate how many of these use cases our engine solves and this forms one of our evaluation metrics.

Sample Input PGN:
Following is an example of the puzzle:
[White "Mate in three"]
[Black "White to move"]
[FEN "4r3/5R2/p5pp/6k1/8/1B4KP/P1P1r3/8 w - - 0 1"]
Output: The list of moves to mate.
1.Rh8+ Kxh8 2.Rf8+ Rxf8+ 3.exf8=Q# *

Example test case:
board       color       number_of_moves_to_mate move_sequence
r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R w KQkq - 1 0   white       2   1. Nf6+ gxf6 2. Bxf7#
r5rk/2p1Nppp/3p3P/pp2p1P1/4P3/2qnPQK1/8/R6R w - - 1 0           white       4   1. hxg7+ Rxg7 2. Rxh7+ Rxh7 3. Qf6+ Rg7 4. Rh1#
r1b1kb1r/pppp1ppp/5q2/4n3/3KP3/2N3PN/PPP4P/R1BQ1B1R b kq - 0 1  black       3   1... Bc5+ 2. Kxc5 Qb6+ 3. Kd5 Qd6#


Algorithm Information:

? State:
? Chess Position (using python-chess)
? Evaluation Function Result
? Evaluation Functions:

Basic: Each chess piece has a value assigned to it. We will sum the total
value of all the pieces for the agent and subtract the sum of all the pieces
for the opponent.

Basic 2: Same as above but take into consideration checkmates; we can
add say if agent checkmates; then the value will be 1000. And if the
opponent can checkmate then -1000 as the value.

Advance: Same as above but take into consideration checks. Checks
can have a value of 100.

Advance 2.0: Same as above but take into consideration forced moves.
Basically, if the opponent can only move a subset of pieces because of
check or discovery check.

Advance 3.0: Same as above but take into consideration the position of
the game. Position here refers to the chess board and who has control of
important positions in the game. This evaluation function will be a strict
goal and might not be implemented within the time window of this project.

Model:
- While this is not a model in the traditional sense; what we call a model will be a method
of determining the accuracy of the chess agent output based on the algorithm.
- The input will provide us with the number of moves to mate and our chess engine will
output the list of moves and we will determine the difference.
- The equation for determining it; let s be the number of moves in the solution, and c be
the number of moves determined by our chess engine.
- f(s, c) = (|s - c|) if c results in checkmate
- f(s, c) = (|s - c|)*100 if c doesn’t results in checkmate
- The goal is to get a small value of f across all the runs. The ideal value will be 0 which
means that it found the checkmate in the same number of moves as expected for all the
game positions as input.

Evaluation Metric: For each puzzle, we will know the number of moves to mate. And our
engine will output the number of moves to mate. Using these two data points, we can leverage
the following metrics in order to evaluate the accuracy of our engine.
1) Correct / Incorrect Metric: calculate the number of puzzles our engine accurately solves.
2) The Difference Metric: calculate the absolute difference between our guess and optimal
solution across all puzzles.
3) Percentage Difference: calculate the percentage difference between our guess and optimal solution across all puzzles.


Implementation:

1) Clean up the input data and put it in our desire format:
the input data was taken from internet and had many inconsistencies in the PGN. some times, the header didn't have information about FEN String and otehr times it was having missing information about number of steps or list of moves from oracle. we cleaned up such games from our list of input data points to our solution.

2) Created a model script that will read the data and run the engine and determine the value of f. The script works in two modes.
1. read the list of puzzles and select a puzzle randomely to pass it to our chess engine. it then prints the list of steps generated by the engine and oracle to show the comparision between the two.
2. read the list of  puzzles and generate evaluation metrics described above.

3)Created the chess engine with the minimax algorithm to return a list of moves based on the starting position.

Oracle: Our input data has the optimal number of moves to mate; which is provided by chess engines. We have used this oracle value to evaluate how successful our engine is at solving chess puzzles.

Results:
for puzzles with mate in one or two moves, we get 100% accuracy and average 0 deviation from the oracle.


Challenges and future improvements:

The main challanges we faced was getting the input data in the right format and making sure that we have large amounts of data in order to successfully test our chess engine. one of our puzzle files had ~5400 chess puzzles out of which ~4400 puzzles remained after cleaning. 
we also had three other set of puzzles of 222,490,463 puzzles of mate in 2,3 and 4 steps.

Since we constrained our engine to look at moves that will result in checkmate, this challenge becomes a little more
difficult because we had to find positions that resulted in mate. However as a side effect this challenge also minimize the workload on the algorithm because we already knew the optimal solution will be a mate.

as the number of moves to win increases ( at level 3 or 4, number of moves increases so drammatically that it takes too long to solve a puzzle. for reference expected number of moves for a given FEN is depth 1: ~20, depth 2: ~400, depth 3: ~9,000, depth 4:~200,000 depth 5: ~5,000,000 depth 6:~120,000,000, depth 7: ~3,000,000,000 and depth 8: ~85,000,000,000 and we need to compute these after  every legal move. (ref. https://www.chessprogramming.org/Perft_Results)
consequently when we have puzzles where we need 3 or more moves for each color to mate which is effectively(2n-1) actual game levels, means at least 5 million board positions at tree depth of 5 per move, our limited capacity of laptops couldn't compute it in reasonable time. 

The possible improvement could be to use multithreaded search which would speed it up by a factor of number of processors present. also given sufficient memory, we could store evaluation of subtrees which would speedup computation at the cost of memory. pre-computed endgame tables would also help avoid exhaustive search. 

Another corner case was when last step was a promotion of a pawn which resulted in mate for the opposite color. given more time, we could adjust our evaluation function to take care of such scenarios where 

scenarios. A complex game like chess has so many variations and covering all such corner cases would require a lot more use cases and time than we could devote to this project however we were happy to implement what we learnt in the class of CS221.