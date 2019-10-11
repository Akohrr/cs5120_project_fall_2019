# CS 5120 Project 1 submission


## Name: **Akoh Atadoga**

Note: This program requires an installation of Python 3.7 or higher

I used python to implement heap sort, merge sort, 3-way merge sort and insertion sort

The implementation of insertion sort is in `main.py` file and sample input data is in the `input_data` directory <br> <br>

On unix system run all the algorithms on the `input_data` directory, enter the following in the command line
```
bash run.sh
```

To run all the algorithms on the `input_data` directory, enter the following in the command line
```
python main.py
```

To run all the algorithms on custom input data, enter the following into the command line:
```
python main.py -fp path/to/input_data --no-default
```
or 
```
python main.py --file-path path/to/input_data --no-default
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
For example output of merge sort would be merge_sort_output_data.csv.
The output data is in the order: identical data, random data, reverse sorted data and sorted data


For more information on how to generate the input data, you can view the custom implementation in `gen_input_data.py` file or online: [here](https://repl.it/@AkohAtadoga/generatedataset)