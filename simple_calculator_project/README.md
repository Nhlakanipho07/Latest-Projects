# Simple-calculator part 1

## How to install simple_calculator.

### 1. Start by cloning my repo:

- run ```git clone git@github.com:Umuzi-org/Nhlakanipho-Ngubo-273-simple-calculator-part-1-python.git``` 
 
    in your linux terminal / git bash for Windows.

### 2. Navigate to the project directory:

- Navigate to "Nhlakanipho-Ngubo-273-simple-calculator-part-1-python" repo:

    run ```cd Nhlakanipho-Ngubo-273-simple-calculator-part-1-python```

### 3. Set up a virtual environment:

- Create a virtual environment by running ```python -m venv my_virtual_env``` in your terminal.
- Activate the virtual environment:
    - On Windows, run ```my_virtual_env\Scripts\activate``` in the terminal.
    - On macOS/Linux, run ```source my_virtual_env/bin/activate``` in the terminal.

### 4. Install simple_calculator and requirements:

- Run ```pip install .``` in the terminal.

- To verify that simple_calculator is installed properly on your local computer, run:

     ```pip show simple_calculator```

    this should show detailed information about simple_calculator in your terminal.

- Then run ```pip install -r requirements.txt``` to install all the dependencies listed in requirements.txt.

- To verify that all the dependencies are installed properly, run ```pip list```

## How to run tests

### To run all tests:

- Run ```pytest``` in your terminal to run all tests.

### To run a specific test:

- Run ```pytest tests/test_calculator.py::test_function_name``` in the terminal.

    Replace ***"test_function_name"*** with a specific test function found in test_calculator.py
    - Example: run ```pytest tests/test_calculator.py::test_add_two_positive_numbers```
    - This runs the ***"test_add_two_positive_numbers"*** function only.

## How to deactivate the virtual environment:

- Run ```deactivate``` in the terminal, once you are finished testing.

