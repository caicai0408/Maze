# Maze
Solve the maze problem and output the longest path 

[Please click to refer the detail of Maze](https://github.com/caicai0408/Maze/blob/main/Maze_Game.pdf)

This repository contains the solution code and 10 testcase(t0~t9).

Requires: Python 3

To use the code:

1. Clone the repository.
2. Try solution on each test case by commands in local:

```
$ cat ./testcases/t1 | python3 ./solution.py
$ cat ./testcases/t2 | python3 ./solution.py
...
$ cat ./testcases/t10 | python3 ./solution.py
```
3. Automatically check the solution on a Linux terminal using the following command:

```
$ { cat ./testcases/t1 ; cat ./testcases/t1 | python3 ./solution.py ; } | ./maze_checker
```


**If the output shows "pass xxx"(xxx is length of the longest path), that mean the solution is correct**
