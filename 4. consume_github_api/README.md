Consume Github API (186)
For raw project instructions see: http://syllabus.africacode.net/projects/github-api-consume/part1/

# Consume Github API

## How to setup Consume Github API.

### 1. Start by cloning the repo:

- run ```git clone git@github.com:Umuzi-org/Nhlakanipho-Ngubo-186-consume-github-api-python.git``` 
 
    in your linux terminal / git bash for Windows.

### 2. Navigate to the project directory:

- Open a code editor and navigate to `Nhlakanipho-Ngubo-186-consume-github-api-python`.

### 3. Set up a virtual environment:

- Create a virtual environment by running ```python -m venv <env>``` in the terminal.
- Activate the virtual environment:
    - On Windows, run ```<env>\Scripts\activate``` in the terminal.
    - On macOS/Linux, run ```source <env>/bin/activate``` in the terminal.

### 4. Install consume_github_api:

- Run ```pip install .``` to install the package.

- Run ```pip install -r requirements.txt``` to install all the dependencies listed in ```requirements.txt```.

- To verify that all the dependencies are installed properly, run ```pip freeze```

### 5. How to set the environment variable:

- Create a `.env` file in the root directory of this repository.
- Inside this file, fill it in with your token i.e `GITHUB_TOKEN=your_github_token_here`
- Close the file.
- Now `consume_github_api.py` should run as expected.

# How to run consume_github_api:

- In the terminal:
    - On Windows, run `python consume_github_api/consume_github_api.py`
    - On Linux, run `python3 consume_github_api/consume_github_api.py`

# How to run tests:

- In the terminal:
    - To run all tests:
        - On Windows: `python -m unittest tests/test_consume_github_api.py`
        - On Linux: `python3 -m unittest tests/test_consume_github_api.py`

    - To run a specific test:
        - On Windows: `python -m unittest tests.test_consume_github_api.TestConsumeGithubAPI.<test_method_name>`
        - On Linux: `python3 -m unittest tests.test_consume_github_api.TestConsumeGithubAPI.<test_method_name>`
    
    *Note: replace `<test_method_name>` with a test method name of the specific test method found in `test_consume_github_api.py`*

### 6. Deactivate virtual environment:

- Run ```deactivate``` in the terminal.

