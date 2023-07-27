# Interpreter---Python

Creation of the procedural programming language LPP. 

This project implements a procedural programming language interpreter written in Python. It allows you to execute code written in the procedural language.

## Installation

1. Clone the repository:

~~~
git clone https://github.com/Johan-FF/Interpreter---Python.git
cd Interpreter---Python
~~~

2. Create a virtual environment (optional but recommended):

~~~
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
~~~

3. Install the required dependencies:

~~~
pip install -r requirements.txt
~~~

## Usage

1. To execute the procedural interpreter and run your procedural code, use the main.py file:

~~~
python main.py
~~~

2. Running Tests

We use nose2 for running tests and mypy for type checking. To ensure everything is working correctly run:

~~~
mypy . && nose2
~~~

## Contributing

Contributions are welcome! If you find any bugs or want to add new features, feel free to open an issue or submit a pull request.

Before submitting a pull request, please ensure that the tests pass and the code complies with the project's coding standards.
