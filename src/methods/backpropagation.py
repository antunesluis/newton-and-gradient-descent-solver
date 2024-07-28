import numpy as np
import sympy as sp


def CalculateBackpropagation(
    equation, x0, y0, learning_rate=0.001, tolerance=1e-6, max_iterations=10000
):
    x_sym, y_sym = sp.symbols("x y")
    eq_sym = sp.sympify(equation.replace("^", "**"))

    f = sp.lambdify((x_sym, y_sym), eq_sym, "numpy")
    gradient = sp.Matrix([eq_sym]).jacobian([x_sym, y_sym])
    gradient_func = sp.lambdify((x_sym, y_sym), gradient, "numpy")

    x, y = x0, y0
    points = [(x, y)]

    for i in range(max_iterations):
        grad = np.array(gradient_func(x, y)).astype(float).flatten()
        print(f"Iteration {i}, x: {x}, y: {y}, grad: {grad}")
        x_new = x - learning_rate * grad[0]
        y_new = y - learning_rate * grad[1]
        points.append((x_new, y_new))

        if np.linalg.norm([x_new - x, y_new - y]) < tolerance:
            break

        x, y = x_new, y_new

    return x, y, points
