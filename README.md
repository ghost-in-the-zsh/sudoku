# sudoku

A program to solve sudokus.


## Features

The program has a few features that make the process more fun. These include:

* Solving valid sudoku puzzles (duh).
* Benchmark performance by measuring the time taken to solve a given puzzle.
* Visualizing a run by showing what the program is doing on a step-by-step basis.

The last one also makes it fun to look at, especially since it can be set to different speeds with the `--delay <seconds>` option. Note that the latter would be significantly slower by comparison, since re-drawing the board is a fairly expensive operation, relatively speaking.


## Requirements

* Python v3.6.5 or later
* A GNU+Linux shell or Windows command prompt


## Installation

You need to use the Python Package Installer. The command syntax may be different depending on your platform.


### GNU+Linux

To remove an older version, run this first from a terminal:
```bash
$ pip3 uninstall -y sudoku
```

Then, to install, you can run this, assuming Git is installed:
```bash
$ pip3 install git+https://gitlab.com/ghost-in-the-zsh/sudoku.git
```

If you do not have Git installed, then you should [download the `.tar.gz`](https://gitlab.com/ghost-in-the-zsh/sudoku) archive into a separate location, and then run this from within the same directory as the archive:

```bash
$ pip3 install .
```


### Windows

The syntax for Windows may vary and often depends on whether you have the Python interpreter in your `PATH` or not. Generally, the commands used in the GNU+Linux section are expected to work if you change `pip3 install` for `py -m pip install`.

The following should work:

```bash
> py -m pip install <URL or path>
```


## Usage Examples

The general structure is:
```bash
$ sudoku-solver [options]
```

More detailed help is available with the `--help` option:
```bash
$ sudoku-solver --help
usage: sudoku-solver [-h] [-g PATH] [-v] [-i] [-d SECS] [-b]

A program to solve sudokus

optional arguments:
  -h, --help            show this help message and exit
  -g PATH, --grid PATH  file system path to text file containing a 9x9 sudoku
                        grid, where empty entries are marked by any of the
                        following symbols: -.0 (default: None)
  -v, --version         show program's version number and exit
  -i, --visualize       shows a step-by-step run by re-drawing the board on
                        each step (default: False)
  -d SECS, --delay SECS
                        step delay, in seconds, when showing a step-by-step
                        run (default: 0.04)
  -b, --benchmark       measure the time taken to solve a sudoku, in seconds
                        (not recommended on step-by-step runs) (default:
                        False)

This program uses a backtracking algorithm. To learn more about backtracking
and how it works, you can look at the built-in pydoc3 documentation and
README.md file.
```


### Puzzles

#### Rules and Terminology

You can look at [this page](https://www.sudoku.name/rules/en) for an explanation of the rules and basic terminology.


#### Creating Puzzles

Sudoku boards must be stored in plain text files. The contents of the file must be arranged as a 9x9 grid, using one character per entry. For example:

```txt
--8-1---9
6-1-9-32-
-4--37--5
-35--82--
--265-8--
--4--175-
5--34--8-
-97-8-5-6
1---6-9--
```

The `-` characters denote empty entries. Other characters that can be used to mark empty entries include dots (`.`) and the number zero (`0`), which is considered an invalid entry value. (Valid entry values must be in the `[1,9]` range.)

While this would be a deviation from official rules, a board that's completely empty would be stored as follows:

```txt
---------
---------
---------
---------
---------
---------
---------
---------
---------
```

If your board is setup incorrectly (e.g. wrong number of rows, columns, entries, etc), the program will reject it.


#### Concrete Examples

Assuming the boards above are stored in the files `hard.txt` and `empty.txt` respectively, you can launch the solver as follows:

```bash
$ sudoku-solver --grid hard.txt --benchmark
+---+---+---+
|358|216|479|
|671|594|328|
|249|837|615|
+---+---+---+
|935|478|261|
|712|653|894|
|864|921|753|
+---+---+---+
|526|349|187|
|497|182|536|
|183|765|942|
+---+---+---+
Solved in 0.0057 secs

$ sudoku-solver --grid empty.txt --benchmark
+---+---+---+
|123|456|789|
|456|789|123|
|789|123|456|
+---+---+---+
|214|365|897|
|365|897|214|
|897|214|365|
+---+---+---+
|531|642|978|
|642|978|531|
|978|531|642|
+---+---+---+
Solved in 0.0185 secs
```

If we launch a visualized run with the `--visualize` option, then the board is presented to the user and begins solving on user command. As the run progresses, the board is re-drawn in its current state at the given step, including information about recursion depth and the number of attempts made so far.

A snapshot of a visualized run for the `hard.txt` board is below:

```bash
+---+---+---+
|278|516|4.9|
|6.1|.9.|32.|
|.4.|.37|..5|
+---+---+---+
|.35|..8|2..|
|..2|65.|8..|
|..4|..1|75.|
+---+---+---+
|5..|34.|.8.|
|.97|.8.|5.6|
|1..|.6.|9..|
+---+---+---+
depth=5, calls=14
```

When displayed, dots denote empty entries and the board is shown divided into 3x3 regions. [This YouTube video](https://youtu.be/kVewrrRwmwQ) shows a full visualized run of this problem.


#### World's Hardest Sudoku

According to this 2012 article[^1], the world's hardest sudoku was created by Finnish mathematician Arto Inkala. It's represented as:

```txt
8--------
--36-----
-7--9-2--
-5---7---
----457--
---1---3-
--1----68
--85---1-
-9----4--
```

This problem was solved by the program in 49,559 calls, taking an average of 1.88 seconds [^2].

[^1]: [World's hardest sudoku: can you crack it?](https://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html)
[^2]: Average of 3 runs.

### Batteries Included

Built-in documentation can be accessed as follows:

In GNU+Linux (and macOS?)
```bash
$ pydoc3 sudoku
```

In Windows
```
> py -m pydoc sudoku
```


## Licensing

This project is [Free Software](https://www.gnu.org/philosophy/free-sw.html) because it respects and protects your freedoms. For a quick summary of what your rights and responsibilities are, you should see [this article](https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)). For the full text, you can see the [license](LICENSE).
