# CS 5120 Project 1 submission


## Name: **Akoh Atadoga**

Note: This program requires an installation of Python 3.7 or higher

I used python to implement heap sort, merge sort, 3-way merge sort and insertion sort

On unix system run all the algorithms on the `input_data` directory, enter the following in the command line
```
$ bash run.sh
```

To run all the algorithms on the `input_data` directory, enter the following in the command line
```
python main.py
```

To run all the algorithms on custom input data, enter the following into the command line:
```
python main.py path/to/input_data -fp --no-default
```
or 
```
python main.py path/to/input_data --file-path --no-default
```

To run all the algorithms on a list of values e.g 8 1 4, enter the following in the command line. The list of values have to separated by a space
```
python main.py --no-default -cv 8 1 4
```
or 
To run all the algorithms on a list of values e.g 8 1 4, enter the following in the command line. The list of values have to separated by a space
```
python main.py --no-default --custom-values 8 1 4
```

For more information you can the following in the command line
```
python main.py -h
```

### Note:
After running all the algorithms on the input data, the size of input, number of comparisons made and execution time in milliseconds is recorded in (name of the algorithm)_output_data.csv file.
For example output of merge sort would be `merge_sort_output_data.csv`.
The output data is in the order: 
1. identical data
2. random data
3. reverse sorted data
4. sorted data


For more information on how to generate the input data, you can view the custom implementation in `gen_input_data.py` file or online: [here](https://repl.it/@AkohAtadoga/generatedataset)