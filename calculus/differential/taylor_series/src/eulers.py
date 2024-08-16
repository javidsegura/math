
import sys

"""

Let's approximate eulers function (e^x) via a finite taylor series (taylor's polynimal) (more precisely,
we will use the special case of the Maclaurin series (taylor series when x = a))

"""

from math import factorial,e
import pandas as pd
import matplotlib.pyplot as plt



class EulerNumberApprox:
      def __init__(self) -> None:
            """
            Params:
                  - high = nº of iterations toward approximation
            
            """
      def _approximate(self, x, high):

            """
            
            I 'land' at a = 0 (Maclaurin) conquer rates of changes around (approximating very well the shape) and 
            then attempt to extend the approximation to further away values
            
            """

            euler_value = 0

            for deriv in range(high):
                  euler_value += 1 * (((x)**deriv) / factorial(deriv))

            return euler_value
      
      def compare_results(self, iters):

                  results = {}
                  aprox_results = [dict() for i in range(iters)]

                  euler = e
                  aprox_eulers = [self._approximate(1,i) for i in range(iters)]
                  

                  for i in range(20):
                        results[i] = euler ** i
                        for idx in range(iters):
                              aprox_results[idx][i] = aprox_eulers[idx] ** i

                  plt.plot(results.keys(), results.values(), label = f"e: 2.7182")
                  for i in range(iters):
                        plt.plot(aprox_results[i].keys(), aprox_results[i].values(), label = f"(iters: {i})approx e: {round(aprox_eulers[i],4)}")


                  plt.title("Approximated euler's number via Taylor's Theorem")
                  plt.xlabel("x")
                  plt.ylabel("e(x)")
                  plt.legend()
                  plt.grid()
                  return plt.show()


                  



temp = EulerNumberApprox()

temp.compare_results(8)

"""
Truly amazed by the power of derivatives...
"""




