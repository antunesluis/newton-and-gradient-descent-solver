import sympy as sp


class EquationManager:
    def __init__(self):
        self.equation1 = ""
        self.equation2 = ""
        self.f1 = None
        self.f2 = None

    def setEquation1(self, equation):
        if equation != self.equation1:
            self.equation1 = equation
            self.f1 = None  # Invalida a função lambdificada

    def setEquation2(self, equation):
        if equation != self.equation2:
            self.equation2 = equation
            self.f2 = None  # Invalida a função lambdificada

    def getLambdifiedFunction(self):
        if not self.f1 and self.equation1:
            try:
                xSym, ySym = sp.symbols("x y")
                eq1Sym = sp.sympify(self.equation1.replace("^", "**"))
                self.f1 = sp.lambdify((xSym, ySym), eq1Sym, "numpy")
            except Exception as e:
                print(f"Erro ao avaliar equação 1: {e}")
                self.f1 = None

        return self.f1

    def getLambdifiedFunctions(self):
        if not self.f1 and self.equation1:
            try:
                xSym, ySym = sp.symbols("x y")
                eq1Sym = sp.sympify(self.equation1.replace("^", "**"))
                self.f1 = sp.lambdify((xSym, ySym), eq1Sym, "numpy")
            except Exception as e:
                print(f"Erro ao avaliar equação 1: {e}")
                self.f1 = None

        if not self.f2 and self.equation2:
            try:
                xSym, ySym = sp.symbols("x y")
                eq2Sym = sp.sympify(self.equation2.replace("^", "**"))
                self.f2 = sp.lambdify((xSym, ySym), eq2Sym, "numpy")
            except Exception as e:
                print(f"Erro ao avaliar equação 2: {e}")
                self.f2 = None

        return self.f1, self.f2

