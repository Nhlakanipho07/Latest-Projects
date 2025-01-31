Animals Part 1. OOP basics (224)
For raw project instructions see: http://syllabus.africacode.net/projects/oop/animals/part1/

# Animals Part 1 Brief Overview:

This project aims to approximate a pet and owner scenario. For context: dogs and cats are animals that can be in a home, so, likewise the Dog and Cat classes inherit from the Animal class and the Home class uses some functionalities from both the Cat and Dog class, through the Animal class, by means of a object orientated programming concept called "Composition".

# How to setup the project:

### 1. Start by cloning the repo:

- Run `git clone git@github.com:Umuzi-org/Nhlakanipho-Ngubo-224-animals-part-1-oop-basics-python.git` in a linux terminal (git bash for Windows).

### 2. Navigate to the project directory:

- On the local computer, using a code editor, navigate to the cloned repository folder and open it in the code editor. The folder should appear as follows: `Nhlakanipho-Ngubo-224-animals-part-1-oop-basics-python`

### 3. Set up a virtual environment:

- In the terminal (Command Prompt for Windows), navigate to the project directory and create a virtual environment by running:

  `python -m venv <virtual_environment>`

- Activate the virtual environment:
  - On Windows, run `<virtual_environment>\Scripts\activate` in the terminal.
  - On macOS/Linux, run `source <virtual_environment>/bin/activate` in the terminal.

### 4. Install animals_part_1:

- Run `pip install .` in the terminal.

- To verify that animals_part_1 is installed properly, run:

  `pip show animals_part_1`

- This should show details of this package in the terminal that correspond to the contents of the setup.py file.

## How to run tests

### To run all tests:

- Before you run tests, create a `__init__.py` file inside the `animals` and `tests` directories.

- Run `pytest` in your terminal to run all tests.

### To run a specific test:

- Run `pytest tests/test_animals.py::test_function_name` in the terminal.

Replace **_"test_function_name"_** with a specific test function found in `test_animals.py`

# How to deactivate the virtual environment:

- Run `deactivate` in the terminal (Command Prompt for Windows).
