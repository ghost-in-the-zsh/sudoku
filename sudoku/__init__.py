'''A program to solve sudokus

This program loads sudoku grids from text files and solves the puzzles,
if they happen to have a solution. A grid is represented in a text file
by following these rules:

  * The text file must be created using a text editor (e.g. Notepad)
    and not a word processor (e.g. MS Word, LibreOffice Writer, etc).
  * Only one (1) grid may be specified per file.
  * Grid dimensions must be 9x9, i.e. 9 rows with 9 columns each.
  * Each grid entry must be one of the following:
        - a valid entry value in the [1,9] range;
        - an empty entry value denoted by any one of the
          characters in the following set: {0, ., -}
  * All pre-populated entries must follow the rules by not repeating
    entry values in rows, columns, or regions.

The following example shows a sudoku grid specification:

    --8-1---9
    6-1-9-32-
    -4--37--5
    -35--82--
    --265-8--
    --4--175-
    5--34--8-
    -97-8-5-6
    1---6-9--

In this example, the '-' character is used to denote empty entries
while pre-propulated entries are in the valid [1,9] range and follow
the rules. This specification can be pasted into a text file and,
without extra spaces or indentation, and used.

If the grid above were stored in a file called "example.txt" in the
current directory, then it can be used as follows:

    $ sudoku-solver -g example.txt      # In GNU+Linux

or

    > sudoku-solver.exe -g example.txt  # In Windows [1]

To show additional program options and features, request help:

    $ sudoku-solver -h

The program's approach for finding a solution boils down to smart
trial and error by systematically trying out all of the (promising)
alternatives to move forward and backtracking when it determines
that there are no more promising alternatives left in the current
"path".

The basic steps are summarized below:

    1. Identify empty entries and their positions on the board.
    2. Generate a set of potential candidates that can be used
       as entries without violating the rules.
    3. Fill a position with an available candidate and recursively
       move one level deeper along this "path" to work on the next
       position, from step 2.
    4. When there are no more candidates for a given position,
       back up one level along the current "path", continuing
       where step 3 had left off.

The program has a solution when it is able to apply step 3 until all
empty entries have been filled [2].

Normally, the program only shows the board in its final solved
state [2]. This is boring. If you want to see the program at work,
step-by-step, then there are program options you can use to do this.

Examples:

Use the '-b' option to benchmark the program and show how long it
took to find the solution:

    $ sudoku-solver -b -g example.txt

Use the '-i' option to visualize the program as it runs. It causes
the program to re-draw the board after each step, forwards or backwards,
including information about the current level (or depth) being worked
on as well as the number of options that have been evaluated so far. For
example:

    $ sudoku-solver -i -g example.txt

Do note that a visualized run will be significantly slower than a normal
run; repeatedly drawing the board is very time consuming, so make sure
your puzzle is not too complicated for this. (Consider using the example
grid above.)

For a simple board, you might even want the run to be slower to see it
better. In this case, you can use the '-d' option to tweak how long the
delay between steps should be.


[1] You may need to add your Python interpreter and its Scripts
directory to your %PATH% variable manually for this to work. Otherwise,
the program executable will not be found.

[2] If it fails to fill the board completely, and all valid candidates
have been exhausted for all positions, then the given board has no
solution. All valid boards must have at least one solution and boards
following official rules have only one solution.
'''
