# CS 5120 Project 2 submission


## Name: **Akoh Atadoga**

Note: This program requires an installation of Python 3.7 or higher

I used python to implement a solution to the Change-Making problem using:
1) Greedy algorithm
2) Straight forward Recursive algorithm
3) Bottom-up dynamic algorithm

On unix system run all the algorithms on the test cases given in the assignment and randomly generated test cases, as shown in `input_data.txt` file, enter the following in the command line
```
$ bash run.sh
```

To run all the algorithms on custom input, enter the following into the command line:
```
$ python main.py [amount] [number_of_coins] [coins_as_space_seperated_values]
```
**Note**: 
1) The order must be maintained for the algorithms to work.
2) If all the data is not supplied, the default data in `input_data.txt` is used.


To run all the algorithms on amount of 63 with a US coin system of 4 values which are 1 5 10 25, enter the following in the command line. The values have to separated by a space
```
$ python main.py 63 4 1 5 10 25
```

### Note:
After running all the algorithms on the input: the amount used, the coin system, number of coins used and execution time in milliseconds is recorded in `name_of_the_algorithm_solution_output.txt` file.
For example, the output of the recursive algorithm is in `recursive_solution_output.txt`.  

A line of output in `greedy_solution_output.txt` and `bottom_up_dynamic_solution_output.txt` would look like
<br>`1 5 10 25`<br>
`0.00044585`<br>
. <br>
. <br>
.<br>
<br>
where the values on the top are coins used while
the value below it is the time taken to execute the algorithm on a given set of data.<br>


A line of output in `recursive_solution_output.txt` would look like
<br>`4` <br> 
`0.012159347534179688` <br>
. <br>
. <br>
.<br>
<br>
 where the values on the top is the coin count
the value below it is the time taken to execute the recursive algorithm on a given set of data<br>