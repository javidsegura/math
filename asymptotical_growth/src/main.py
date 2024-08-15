"""

Motivation: asymptotical growth of functions suggest only the largest terms is relevant to
approximately determine its growth (meaning for any function f(x) only its largest 
polynomial term prevails (without any possible multiplactive constant) as n grows to infinity

"""

import pandas as pd 
import matplotlib.pyplot as plt

class FunctionGrwoth:
      def __init__(self, high) -> None:
            # Function is: 3*x^3 + x^2 + x + 1000
            self.high = high
            self.growth_rate = pd.DataFrame(columns=["cubic", "quadratic", "one", "constant"])
            pass

      def evaluate(self):  

            for x in range(self.high):
                  cubic = x**3 
                  quadratic = x**2
                  one = x
                  constant = 1000
                  total = cubic  +  quadratic + one + constant

                  print(total)
                  
                  new_row = {
                        "cubic": cubic / total,
                        "quadratic" : quadratic / total,
                        "one": one / total, 
                        "constant": constant / total  
                  }
                  
                  self.growth_rate = self.growth_rate._append(new_row, ignore_index = True)

      def plot_results(self):

            for col in self.growth_rate.columns:
                  plt.plot(range(self.high), self.growth_rate[col], label = col)

            plt.title("Growth Rate Components over Range")
            plt.xlabel("x")
            plt.ylabel("Proportion")
            plt.legend()
            plt.grid(True)
            plt.show()
            
      
evaluator = FunctionGrwoth(50)
evaluator.evaluate()


            
evaluator.plot_results()