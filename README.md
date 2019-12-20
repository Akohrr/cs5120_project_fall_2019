# CS 5120 Project 2C submission


## Name: **Akoh Atadoga**

Note: This program requires an installation of Python 3.7 or higher

I used python to implement a Breadth First Search (BFS) algorithm to
find the minimum hop length between 2 nodes in a graph.

On unix system, to run the BFS algorithms on randomly generated `directed graph`.<br>
 Enter the following in the command line
```
$ bash run.sh
```


### Note:
After running all the BFS algorithms on the randomly generate graph, <br>
The path from the start node to end node and the execution time in milliseconds is recorded in `output_data_{random_number}.csv` file. 
 Where {random_number} is a random number from 0 to 100. For example `output_data_87.csv`<br> 
<br>
For example, running the program on a random graph below:<br>
Edges of 1 is {'3', '2'}<br>
Edges of 2 is {'3', '4'}<br>
Edges of 3 is {'3', '4'}<br>
Edges of 4 is {'1', '4'}<br>
Graph is {'1': {'3', '2'}, '2': {'3', '4'}, '3': {'3', '4'}, '4': {'1', '4'}} <br>
Number of nodes is 4 edges is 8 <br>
Path from 1 to 4  is ['1', '3', '4'] <br>

A line of output in `output_data_{random_number}.csv` using the example above would look like
<br>`['1', '3', '4'], 0.0023598484`<br>
<br>

Note: The graphs are randomly generated so you would get different outputs each time you run the program.

To graph used to generate the `output_data_{random_number}.csv` is stored in `graph_data_{random_number}.txt`. For example, `graph_data_87.txt`
 would generate `output_data_87.csv` <br>
The graph is stored to view the randomness of the graph generator and to verify the results.

The graph for generating the project report is in `graph_data_99.txt`
The output of the graph used for generating the project report is in `output_data_99.csv`