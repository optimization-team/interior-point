# Programing task 2, "Introduction to optimization"

## How to test the program on your LPP
To test the program on your input, input the LPP into on of the files in [inputs](https://github.com/optimization-team/interior-point/tree/main/inputs) folder.
- Enter objective value coefficients, separated by space, in one line.
- Enter coefficients of constraints, line by line.
- Enter right-hand side values of constraints.
- Enter number of digits after decimal point (precision).
- Enter initial solution for interior point algorithm (**with slack variables!**) 

Specify the name of the file from [inputs](https://github.com/optimization-team/interior-point/tree/main/inputs) folder you want to use as an argument in parse_file() function in [main.py](https://github.com/optimization-team/interior-point/blob/main/main.py), line 20. Then, run the [main.py](https://github.com/optimization-team/interior-point/blob/main/main.py) file.

Check, if the results are what you expected.
## Structure of the project
### [inputs](https://github.com/optimization-team/interior-point/tree/main/inputs)
Folder, containing 7 different inputs, on which the program was tested.
### [Exceptions.py](https://github.com/optimization-team/interior-point/blob/main/Exceptions.py)
File containing Exceptions which Simplex and Interior Point classes can raise.
### [Function.py](https://github.com/optimization-team/interior-point/blob/main/Function.py)
File containing a Function class. This class is used to store the objective function for the LPP.
### [InteriorPoint.py](https://github.com/optimization-team/interior-point/blob/main/InteriorPoint.py)
File containing the Interior Point method. Contains the following classes:
- Solution - class, used to store the solution for the LPP.
- InteriorPoint - class, responsible for calculating the Interior Point method.
### [Simplex.py](https://github.com/optimization-team/interior-point/blob/main/Simplex.py)
File containing the Simplex method. Contains the following classes:
- SimplexSolution - class, used to store the solution for the LPP.
- Simplex - class, responsible for calculating the LPP using the Simplex method.
### [input_parser.py](https://github.com/optimization-team/interior-point/blob/main/input_parser.py)
File containing functions parsing input into format, needed for the Simplex class.
### [main.py](https://github.com/optimization-team/interior-point/blob/main/main.py)
File, from which the program can be tested on the input from certain file from [inputs](https://github.com/optimization-team/interior-point/tree/main/inputs) folder.
### [requirements.txt](https://github.com/optimization-team/interior-point/blob/main/requirements.txt)
Information about assets needed for the program to be executed correctly.
