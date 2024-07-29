import sympy as sp

from utils.exceptions import InitialValuesError, InvalidEquationError


class EquationManager:
    def __init__(self):
        self.xInitial = None
        self.yInitial = None
        self.strEquation1 = ""
        self.strEquation2 = ""
        self.lambdifiedEquation1 = None
        self.lambdifiedEquation2 = None

    def setXInitial(self, val):
        try:
            self.xInitial = float(val)
        except ValueError:
            raise InitialValuesError("O x inicial precisa ser um número válido")

    def setYInitial(self, val):
        try:
            self.yInitial = float(val)
        except ValueError:
            raise InitialValuesError("O y inicial precisa ser um número válido")

    def setStrEquation1(self, equation):
        if equation != self.strEquation1:
            self.strEquation1 = equation

    def setStrEquation2(self, equation):
        if equation != self.strEquation2:
            self.strEquation2 = equation

    def setLambdifiedEquation1(self, equation):
        try:
            xSym, ySym = sp.symbols("x y")
            eq1Sym = sp.sympify(equation.replace("^", "**"))
            self.lambdifiedEquation1 = sp.lambdify((xSym, ySym), eq1Sym, "numpy")
        except Exception:
            self.lambdifiedEquation1 = None
            raise InvalidEquationError(
                "Equação f(x, y) inválida, erro ao avaliar equação."
            )

    def setLambdifiedEquation2(self, equation):
        try:
            xSym, ySym = sp.symbols("x y")
            eq2Sym = sp.sympify(equation.replace("^", "**"))
            self.lambdifiedEquation2 = sp.lambdify((xSym, ySym), eq2Sym, "numpy")
        except Exception:
            self.lambdifiedEquation2 = None
            raise InvalidEquationError(
                "Equação g(x, y) inválida, erro ao avaliar equação."
            )

