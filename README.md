# Interpreter---Python

Creation of the procedural programming language LPP. 

This project implements a procedural programming language interpreter written in Python. It allows you to execute code written in the procedural language.

## Requirements

- Python 3.9+
- mypy
- nose2

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

1. To execute the procedural interpreter and run your procedural code (REPL), use the main.py file:

~~~
python39 main.py  # Or python3.9 main.py
~~~

### Commands to REPL

1. `salir()`: This it allow you exit of the REPL.

### Built-in of LPP

1. `longitud()`: Returns the length of a STRING in an INTEGER.

2. Running Tests

We use nose2 for running tests and mypy for type checking. To ensure everything is working correctly run:

~~~
mypy . && nose2
~~~

## Tutorial SigmaF

### Let Statements

For declaring a value, you must use `variable` and give it a value. For example:

~~~
variable numero = 1                        -- Interger
variable cadena_de_caracteres = "string"   -- String
~~~

SigmaF allows data type as Integer, Boolean and String.

### Operators

These are operators:

| Operator             | Symbol |
|----------------------|--------|
| Plus                 |    +   |
| Minus                |    -   |
| Multiplication       |    *   |
| Division             |    /   |
| Negation             |    !   |
| Equal                |   ==   |
| Not Equal            |   !=   |
| Less than            |    <   |
| Greater than         |    >   |
<br/>

### Functions

For declaring a function, you have to use the next syntax:

~~~
variable function_name = procedimiento ( param_1, param_2, ... ) {
    ...
    regresa param_1 + param_2 + ...;
}
~~~

For example:

~~~
variable obtener_suma = procedimiento ( x, y ) {
    regresa x + y;
}
obtener_suma(12, 4)  # Print 16
~~~

### Conditionals

Regarding the conditionals, the syntax structure is:

~~~
si ( condition ) {
    ...
}
si_no {
    ...
}
~~~

For example:

~~~
variable mayor_de_edad = procedimiento( x ) {
    si ( x < 18 ) {
        regresa falso;
    }
    si_no {
        regresa verdadero;
    }
}
mayor_de_edad(18)  # Print 'verdadero'
~~~

## Some Examples

~~~
    python39 main.py
LPP - v=0.1.1
Para salir ingresa salir().
>> variable factorial = procedimiento ( x ) { si ( x < 1 ) { regresa 1; } si_no { regresa x * factorial( x - 1 ); }; };
>> factorial(4)
24
>> variable factorial_4 = factorial(4)
>> si ( factorial_4 == 24 ) { variable resultado = "correcto"; } si_no { variable error = "incorrecto"; };
>> resultado
correcto
>> error
Error: Identificador no encontrado: error
>> longitud(resultado)
8
~~~

## Contributing

Contributions are welcome! If you find any bugs or want to add new features, feel free to open an issue or submit a pull request.

Before submitting a pull request, please ensure that the tests pass and the code complies with the project's coding standards.
