# CS 5120 Project 1A submission


## Name: **Akoh Atadoga**


I used python to implement insertion sort

The implementation of insertion sort is in `main.py` file and sample input data is in the `input_data` directory <br> <br>

To run insertion sort on the `input_data` directory, enter the following in the command line
```
python main.py
```

To run insertion sort on custom input data, enter the following into the command line:
```
python main.py -fp path/to/input_data --no-default
```
or 
```
python main.py --file-path path/to/input_data --no-default
```

To run insertion sort a list of values e.g 8 1 4, enter the following in the command line. The list of values have to separated by a space
```
python main.py --no-default -cv 8 1 4
```
or 
To run insertion sort a list of values e.g 8 1 4, enter the following in the command line. The list of values have to separated by a space
```
python main.py --no-default --custom-values 8 1 4
```

For more information you can the following in the command line
```
python main.py -h
```

### Note:
After insertion sort has been run on an input data, the size of input, number of comparisons made and execution time in milliseconds is recorded in output_data.txt file


For more information on how to generate the input data, you can view the custom implementation in `gen_input_data.py` or online: [here](https://repl.it/@AkohAtadoga/generatedataset)