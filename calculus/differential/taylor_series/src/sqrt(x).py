

"""

Let's approximate sqrt function (sqrt(x)) via a finite taylor series (taylor's polynimal. We wont 
use the Maclaurin series here.

"""

from math import factorial
import pandas as pd
import matplotlib.pyplot as plt



class SqrtApprox:
      def __init__(self) -> None:
            pass
      def _approximate(self, high):

            """ 

            Parameters:
                  - high: nº of inputs to approximate
            
            Note: Approximated at 81 (a = 81) and expanded at range(high) (x = range(high))
            Taylor polynomials had to be unfurtonately hardcoded because of non-cyclical derivative :( That means these slopes are hardcoded for original 'a'
            """
            
            # P = taylor polynomial of 1st order 
            p_1 = lambda x: 9 + (1/18 * (x-81)) 

            # P = taylor polynomial of 2nd order 
            p_2 = lambda x: 9 + (1/18 * (x-81)) + ((1/-2916) * ((x-81)**2)/factorial(2)) 

            # P = taylor polynomial of 3rd order 
            p_3 = lambda x:  9 + (1/18 * (x-81)) + ((1/-2916) * ((x-81)**2)/factorial(2)) + ((1/157464) * (((x-81)**3)/factorial(3)))

            # P = taylor polynomial of 4th order 
            p_4 = lambda x: 9 + (1/18 * (x-81)) + ((1/-2916) * ((x-81)**2)/factorial(2)) + ((1/157464) * (((x-81)**3)/factorial(3))) + ((-5/25509168) * (((x-81)**4)/factorial(4)))

            talyor_polynomials = [p_1, p_2, p_3, p_4]

            # f(x):
            f = lambda x: x **0.5

            actual_results = {}
            approx_results = [dict() for i in range(4)]

            for x in range(high):
                  actual_results[x] = f(x)

                  for taylor_order in range(4):
                        approx_results[taylor_order][x] = talyor_polynomials[taylor_order](x)

            plt.plot(actual_results.keys(), actual_results.values(), label = f"sqrt(x)")

            for taylor_order in range(4):
                  plt.plot(approx_results[taylor_order].keys(), approx_results[taylor_order].values(), label = f"Talyor polynomial '{taylor_order+1}' order")

            plt.grid()
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Approximating sqrt(x) via Taylor's Theorem")
            plt.legend()

            return plt.show()


                  
temp = SqrtApprox()

print(temp._approximate(192)) # 192 to see how well it approximates twice in each direction

"""
The power of derivatives is trule undervalued... lol
"""




