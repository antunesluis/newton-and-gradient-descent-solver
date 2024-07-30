import sympy as sp
import numpy as np
from typing import List, Tuple

from utils.exceptions import CalculationError


def calculateNewtonMethod(
    equation1: str,
    equation2: str,
    x0: float,
    y0: float,
    tolerance: float = 0.000001,
    max_iterations: int = 100,
) -> Tuple[float, float, List[Tuple[float, float]]]:
    """
    Resolve um sistema de equações não lineares usando o método de Newton.

    Args:
        equation1 (str): A primeira equação na forma de string.
        equation2 (str): A segunda equação na forma de string.
        x0 (float): Valor inicial para x.
        y0 (float): Valor inicial para y.
        tolerance (float): Tolerância para a convergência do método.
        max_iterations (int): Número máximo de iterações permitidas.

    Returns:
        Tuple[float, float, List[Tuple[float, float]]]: Contém os valores finais (x, y) e a lista de pontos iterados.
    """
    try:
        # Definindo os símbolos x e y
        x_sym, y_sym = sp.symbols("x y")

        # Convertendo as equações de string para expressões simbólicas
        eq1_sym = sp.sympify(equation1.replace("^", "**"))
        eq2_sym = sp.sympify(equation2.replace("^", "**"))

        # Calculando a matriz Jacobiana das equações
        jacobian = sp.Matrix(
            [
                [eq1_sym.diff(x_sym), eq1_sym.diff(y_sym)],
                [eq2_sym.diff(x_sym), eq2_sym.diff(y_sym)],
            ]
        )

        # Lambdificando as equações e a matriz Jacobiana para avaliação numérica
        f1 = sp.lambdify((x_sym, y_sym), eq1_sym, "numpy")
        f2 = sp.lambdify((x_sym, y_sym), eq2_sym, "numpy")
        jacobian_func = sp.lambdify((x_sym, y_sym), jacobian, "numpy")

    except Exception as e:
        raise CalculationError(
            f"Erro ao preparar as equações/matriz Jacobiana: {str(e)}"
        )

    def newton_step(x: float, y: float) -> Tuple[float, float]:
        """
        Executa um passo do método de Newton.

        Args:
            x (float): Valor atual de x.
            y (float): Valor atual de y.

        Returns:
            Tuple[float, float]: Novos valores de (x, y) após o passo de Newton.
        """
        try:
            F = np.array([f1(x, y), f2(x, y)])  # Calcula F(x, y)
            J = np.array(jacobian_func(x, y))  # Calcula a matriz Jacobiana J(x, y)
            delta = np.linalg.solve(J, F)  # Resolve J * delta = F para delta
            return x - delta[0], y - delta[1]  # Atualiza x e y
        except np.linalg.LinAlgError as e:
            raise CalculationError(f"Erro ao resolver o sistema linear: {str(e)}")
        except Exception as e:
            raise CalculationError(f"Erro ao executar o passo de Newton: {str(e)}")

    x, y = x0, y0  # Inicializa os valores de x e y
    points: List[Tuple[float, float]] = [
        (x, y)
    ]  # Lista para armazenar os pontos iterados

    # Itera até o número máximo de iterações ou até a convergência
    for _ in range(max_iterations):
        try:
            x_new, y_new = newton_step(x, y)  # Executa um passo do método de Newton
            points.append((x_new, y_new))  # Armazena o novo ponto
            # Verifica a convergência
            if abs(x_new - x) < tolerance and abs(y_new - y) < tolerance:
                return (
                    x_new,
                    y_new,
                    points,
                )  # Retorna o resultado final e os pontos iterados
            x, y = x_new, y_new  # Atualiza os valores de x e y para a próxima iteração
        except CalculationError as e:
            raise e

    # Caso o método não converja, levanta uma exceção
    raise CalculationError(
        "O método de Newton não convergiu após o número máximo de iterações."
    )

