
"""

Computing the area of infinitesimally small rectangles for all x that belong to the domain of 
f is a great idea to approximate the area under its curve (and the many applications that arise
thereafter)

Archive code from 21/2/2024

"""

class Integral:
      """ Function to approximate will be sqrt(x) """

      def __init__(self) -> None:
          pass
      
      def approximate(self, a, b, width = 0.0001):
            
            f = lambda x: x**0.5
            auc = 0

            current_rect = a
            while current_rect <= b:
                  auc += f(current_rect) * width
                  current_rect += width

            return auc

            
                  
temp = Integral()

print(temp.approximate(0,100))