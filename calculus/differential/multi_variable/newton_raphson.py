""" Findin the roots of a function with Newton-Raphson method. """

import sympy as sym
import math

class NetwoRaphson:
    def __init__(self, max_iters:int = 50, boundary:float = 0.01):
        self.max_iters = max_iters
        self.boundary = boundary
        self.x = sym.symbols("x")
        self.func = str(input("F(x) = "))

    def f(self, x):
        return eval(self.func, {"x":x, "math":math})
    
    def fprime(self, x):
        return sym.diff(self.f(self.x), self.x)
    
    def differentiate(self, x):
        return self.fprime(self.x).evalf(subs={self.x: x})
    
    def get_root(self, init_val):
        iter_val = init_val
        counter = 0
        while (self.f(iter_val) - 0) > self.boundary and counter < self.max_iters:
            iter_val -= (self.f(iter_val) / self.differentiate(iter_val))
            counter += 1
        return iter_val, self.f(iter_val)


       
       
temp = NetwoRaphson()
root, f_val = temp.get_root(400000)

print(root,f_val)