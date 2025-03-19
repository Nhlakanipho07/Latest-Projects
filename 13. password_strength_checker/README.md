Password strength checker (269)
For raw project instructions see: http://syllabus.africacode.net/projects/tdd/password-checker/part1/

# Password strength checker

## How to install password_checker

### 1. Start by cloning this repo:

- Open a code editor and run `git clone git@github.com:Umuzi-org/Nhlakanipho-Ngubo-269-password-checker-python.git`

  in your linux terminal / git bash for Windows.

### 2. Navigate to the project directory through the code editor

### 3. Set up a virtual environment:

- Create a virtual environment by running `python -m venv <env>` in the terminal, replace `<env>` with a preferred name.
- Activate the virtual environment:
  - On Windows, run `<env>\Scripts\activate` in the terminal.
  - On macOS/Linux, run `source <env>/bin/activate` in the terminal.

### 4. Install password_checker and requirements:

- Run `pip install .` in the terminal.

- To verify that password_checker is installed properly on your local computer, run:

  `pip show password_checker`

  this should show detailed information about password_checker in your terminal.

- Then run `pip install -r requirements.txt` to install all the dependencies listed in requirements.txt.

- To verify that all the dependencies are installed properly, run `pip list`

## How to run tests

### To run all tests:

- Before you run tests, create a `__init__.py` file inside the password_checker and tests directories.

- Run `pytest` in your terminal to run all tests.

### To run a specific test:

- Run `pytest tests/test_password_checker.py::test_function_name` in the terminal.

  Replace **_"test_function_name"_** with a specific test function found in test_password_checker.py

## How to deactivate the virtual environment:

- Run `deactivate` in the terminal, once you are finished testing.
