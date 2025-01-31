Bank accounts - part 1 (959)
For raw project instructions see: http://syllabus.africacode.net/projects/oop/bank-accounts/part-1/


# How to setup the project:

### 1. Start by cloning the repo:

- Run `git clone git@github.com:Umuzi-org/Nhlakanipho-Ngubo-959-contentitem-python.git` in a linux terminal (git bash for Windows).

### 2. Navigate to the project directory:

- On the local computer, using a code editor, navigate to the cloned repository folder and open it in the code editor. The folder should appear as follows: `Nhlakanipho-Ngubo-959-contentitem-python`

### 3. Set up a virtual environment:

- In the terminal (Command Prompt for Windows), navigate to the project directory and create a virtual environment by running:

  `python -m venv <virtual_environment>`

- Activate the virtual environment:
  - On Windows, run `<virtual_environment>\Scripts\activate` in the terminal.
  - On macOS/Linux, run `source <virtual_environment>/bin/activate` in the terminal.

### 4. Install banking:

- Run `pip install .` in the terminal.

- To verify that `banking` is installed properly, run:

  `pip show banking`

- This should show details of this package in the terminal that correspond to the contents of the setup.py file.

## How to run tests

### To run all tests:

- Before you run tests, create a `__init__.py` file inside the `banking` and `tests` directories.

- Run `pytest` in your terminal to run all tests.

### To run a specific test:

- Run `pytest tests/test_bank_account.py::test_function_name` in the terminal.
- Or `pytest tests/test_bank.py::test_function_name`

Replace **_"test_function_name"_** with a specific test function found in `test_bank_account.py` or `test_bank.py` depending on which test script one wishes to run.

# How to deactivate the virtual environment:

- Run `deactivate` in the terminal (Command Prompt for Windows).
