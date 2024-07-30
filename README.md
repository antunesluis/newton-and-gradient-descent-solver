# Newton Method and Backpropagation Calculator

This project was developed as part of the Calculus B course during my undergraduate studies. It implements a graphical calculator to solve equations using the Newton Method and the Backpropagation algorithm.

## Newton Method Interface

![Newton Method Interface](https://github.com/antunesluis/newton-backprop-solver/blob/main/newton-method.png)

## Backpropagation Interface

![Backpropagation Interface](https://github.com/antunesluis/newton-backprop-solver/blob/main/backpropagation.png)

## Overview

This project consists of two main parts:

1. **Newton Method**: Implementation to find roots of a two-dimensional system of equations.
2. **Backpropagation**: Implementation to find the minimum of a function using gradient descent.

## Features

- Interactive graphical interface using PySide6.
- Input of mathematical equations in an understandable syntax.
- 2D plots of the provided equations.
- Tables to display calculation results.

## Requirements

- Python 3.8+
- PySide6
- SymPy
- Matplotlib

## Installation

1. Clone this repository:

```bash
git clone https://github.com/usuario/newton-method-and-backprop.git
```

2. Navigate to the project directory:

```bash
cd newton-method-and-backprop
```

3. Create a virtual environment and activate it:

```bash
python -m venv venv source venv/bin/activate # For Windows: venv\Scripts\activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
python src/main.py
```

2. Use the tabs to input the equations and initial values, and click on "Calculate" to see the results.

## Equation Syntax

The equations must be input in a syntax understandable by the SymPy library. Some examples:

- Trigonometric functions: `sin(x)`, `cos(y)`
- Exponentials and logarithms: `exp(x)`, `log(x)`
- Powers and roots: `x**2`, `sqrt(x)`
- Basic operations: `+`, `-`, `*`, `/`

## Equation Examples

### Newton Method

1. `f(x, y) = x**2 + y**2 - 1`

2. `g(x, y) = x**3 - y`

3. `f(x, y) = sin(x) + y`

4. `g(x, y) = cos(y) - x`

### Backpropagation

1. `f(x, y) = (x - 2)**2 + (y - 3)**2`

2. `f(x, y) = x**2 + y**2 + x*y - 10*x`
