string-calculator part 1 (266)
For raw project instructions see: http://syllabus.africacode.net/projects/tdd/string-calculator-part-1/

# String_calculator part 1

## How to install string_calculator.

### 1. Start by cloning the repo:

- run ```git clone git@github.com:Umuzi-org/Nhlakanipho-Ngubo-266-string-calculator-python.git``` 
 
    in your linux terminal / git bash for Windows.

### 2. Navigate to the project directory:

- Open a code editor and navigate to `Nhlakanipho-Ngubo-266-string-calculator-python`.

### 3. Set up a virtual environment:

- Create a virtual environment by running ```python -m venv <env>``` in the terminal.
- Activate the virtual environment:
    - On Windows, run ```<env>\Scripts\activate``` in the terminal.
    - On macOS/Linux, run ```source <env>/bin/activate``` in the terminal.

### 4. Install simple_calculator and requirements:

- Run ```pip install .``` in the terminal.

- To verify that string_calculator is installed properly, run:

     ```pip show string_calculator```

    this should show detailed information about string_calculator in the terminal.

- Then run ```pip install -r requirements.txt``` to install all the dependencies listed in requirements.txt.

- To verify that all the dependencies are installed properly, run ```pip list```

## How to run tests

### To run all tests:

- Run ```pytest``` in your terminal to run all tests.

### To run a specific test:

- Run ```pytest tests/test_string_calculator.py::test_function_name``` in the terminal.

    - Replace ***"`test_function_name`"*** with a specific test function found in `test_string_calculator.py`

## How to deactivate the virtual environment:

- Run ```deactivate``` in the terminal, once you are finished testing.

