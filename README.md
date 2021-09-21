# Word-counter #
_________________
This program counts the number of lines, words and characters in given file(s) and outputs do the terminal. More directions of how to run is given below.

## Scripts: ##
- wc.py
- Array.py

## Tests: ##
- test_Array.py

## Requirements: ##
To run the scripts you need to have python3 installed on your PC.
This can be downloaded from the python website.

To run the tests you need to have pytest installed.
If you dont alredy have this, it can be installed with the command:

```bash
pip3 install pytest
```

## How to run: ##
### wc.py ###
This is a simple word counter.
To use you simply run the script with

```bash
python3 wc.py <argument>
```

with the argument  * , *.py or with a filename.

With * as the argument the word counter will count the number of lines, words and characters in every file in the current folder, and output this nicely to the terminal. The script will also count as one of the files in the folder.

With *.py the script will do the same as with the previous argument, however it will only count .py files.

With a filename as the argument the script will look for the file and count the lines, words and characters in the file. If a file with the given filename dont exist, the script will print an error message.

### Array.py ###
This is a python file containg a class Array implemented as an array with the opportunity to do several mathematical operations. The operations can be done on one array, two arrays or with an array and an integer or float. This is given that the data types in the array are all the same.

The operations to be done on the Array are: convert to string, add, subtract, multiply, comparison, find mean, variance or min number.

### testArray.py ###
This is the test file for the Array described. This is implemented for use of pytest, and to run the test you only need to run pytest in your terminal.

```bash
pytest
```

The test program will then run tests on several cases of each of the mathematical operations to be done on the Array and output the result to your terminal. All the tests in the program should pass.
