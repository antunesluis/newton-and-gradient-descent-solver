import numpy as np
import sympy as sp

from utils.exceptions import CalculationError


def CalculateBackpropagation(
    equation, x0, y0, learning_rate=0.001, tolerance=1e-6, max_iterations=10000
):
    """
    Realiza o cálculo do backpropagation para encontrar o mínimo de uma função.

    Args:
        equation (str): A equação na forma de string.
        x0 (float): Valor inicial para x.
        y0 (float): Valor inicial para y.
        learning_rate (float): Taxa de aprendizado para a atualização dos parâmetros.
        tolerance (float): Tolerância para a convergência do método.
        max_iterations (int): Número máximo de iterações permitidas.

    Returns:
        tuple: Contém os valores finais (x, y) e a lista de pontos iterados.

    Raises:
        CalculationError: Se ocorrer um erro durante o cálculo.
    """
    try:
        # Definindo os símbolos x e y
        x_sym, y_sym = sp.symbols("x y")

        # Convertendo a equação de string para expressão simbólica
        eq_sym = sp.sympify(equation.replace("^", "**"))

        # Lambdificando a função e calculando o gradiente
        sp.lambdify((x_sym, y_sym), eq_sym, "numpy")
        gradient = sp.Matrix([eq_sym]).jacobian([x_sym, y_sym])
        gradient_func = sp.lambdify((x_sym, y_sym), gradient, "numpy")

        x, y = x0, y0  # Inicializa os valores de x e y
        points = [(x, y)]  # Lista para armazenar os pontos iterados

        for i in range(max_iterations):
            # Calcula o gradiente
            grad = np.array(gradient_func(x, y)).astype(float).flatten()

            print(f"Iteration {i}, x: {x}, y: {y}, grad: {grad}")
            x_new = x - learning_rate * grad[0]  # Atualiza x
            y_new = y - learning_rate * grad[1]  # Atualiza y
            points.append((x_new, y_new))

            # Verifica a convergência
            if np.linalg.norm([x_new - x, y_new - y]) < tolerance:
                break

            # Atualiza os valores de x e y para a próxima iteração
            x, y = (x_new, y_new)
        return x, y, points

    except Exception as e:
        raise CalculationError(f"Erro no cálculo do backpropagation: {str(e)}")

