import numpy as np
import sympy as sp
from typing import List, Tuple

from utils.exceptions import CalculationError


def calculateBackpropagation(
    equation: str,
    x0: float,
    y0: float,
    learningRate: float = 0.001,
    tolerance: float = 0.000001,
    maxIterations: int = 10000,
) -> Tuple[float, float, List[Tuple[float, float]]]:
    """
    Realiza o cálculo do backpropagation para encontrar o mínimo de uma função.

    Args:
        equation (str): A equação na forma de string.
        x0 (float): Valor inicial para x.
        y0 (float): Valor inicial para y.
        learningRate (float): Taxa de aprendizado para a atualização dos parâmetros.
        tolerance (float): Tolerância para a convergência do método.
        maxIterations (int): Número máximo de iterações permitidas.

    Returns:
        Tuple[float, float, List[Tuple[float, float]]]: Contém os valores finais (x, y) e a lista de pontos iterados.

    Raises:
        CalculationError: Se ocorrer um erro durante o cálculo.
    """
    try:
        # Definindo os símbolos x e y
        xSym, ySym = sp.symbols("x y")

        # Convertendo a equação de string para expressão simbólica
        eqSym = sp.sympify(equation.replace("^", "**"))

        # Lambdificando a função e calculando o gradiente
        sp.lambdify((xSym, ySym), eqSym, "numpy")
        gradient = sp.Matrix([eqSym]).jacobian([xSym, ySym])
        gradientFunc = sp.lambdify((xSym, ySym), gradient, "numpy")

        x, y = x0, y0  # Inicializa os valores de x e y
        points = [(x, y)]  # Lista para armazenar os pontos iterados

        for i in range(maxIterations):
            # Calcula o gradiente
            grad = np.array(gradientFunc(x, y)).astype(float).flatten()

            print(f"Iteration {i}, x: {x}, y: {y}, grad: {grad}")
            xNew = x - learningRate * grad[0]  # Atualiza x
            yNew = y - learningRate * grad[1]  # Atualiza y
            points.append((xNew, yNew))

            # Verifica a convergência
            if np.linalg.norm([xNew - x, yNew - y]) < tolerance:
                break

            # Atualiza os valores de x e y para a próxima iteração
            x, y = (xNew, yNew)
        return x, y, points

    except Exception as e:
        raise CalculationError(f"Erro no cálculo do backpropagation: {str(e)}")

