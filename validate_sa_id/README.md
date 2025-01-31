Validate a South African ID number (625)
For raw project instructions see: http://syllabus.africacode.net/language-agnostic/validate-id-number/

# Validate South African ID number

## How to install validate_sa_id


### 1. Start by cloning my repo:

- run ```git clone git@github.com:Umuzi-org/Nhlakanipho-Ngubo-625-validate-a-south-african-id-number-python.git``` 
 
    in your linux terminal / git bash for Windows.

### 2. Navigate to the project directory:

- Navigate to "Nhlakanipho-Ngubo-625-validate-a-south-african-id-number-python" repo:

    run ```cd Nhlakanipho-Ngubo-625-validate-a-south-african-id-number-python```

### 3. Set up a virtual environment:

- Create a virtual environment by running ```python -m venv env``` in your terminal.
- Activate the virtual environment:
    - On Windows, run ```env\Scripts\activate``` in the terminal.
    - On macOS/Linux, run ```source env/bin/activate``` in the terminal.

### 4. Install simple_calculator and requirements:

- Run ```pip install .``` in the terminal.

- To verify that validate_sa_id is installed properly on your local computer, run:

     ```pip show validate_sa_id```

    this should show detailed information about simple_calculator in your terminal.

- Then run ```pip install -r requirements.txt``` to install all the dependencies listed in requirements.txt.

- To verify that all the dependencies are installed properly, run ```pip list```

## How to run tests

### To run all tests:

- Run ```pytest``` in your terminal to run all tests.

### To run a specific test:

- Before you run tests, create a ```__init__.py``` file inside the validate_sa_id and tests directories.

- Run ```pytest tests/test_validate_sa_id.py::test_function_name``` in the terminal.

    Replace ***"test_function_name"*** with a specific test function found in test_validate_sa_id.py
    - Example: run ```pytest tests/test_validate_sa_id.py::test_inputs_of_is_id_number_valid```
    - This runs the ***"test_inputs_of_is_id_number_valid"*** function only.

## How to deactivate the virtual environment:

- Run ```deactivate``` in the terminal, once you are finished testing.

