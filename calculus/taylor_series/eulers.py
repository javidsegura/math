
"""

Let's approximate eulers function (e^x) via a finite taylor series (taylor's polynimal) (more precisely,
we will use the special case of the Maclaurin series (taylor series when x = a))

"""

from math import factorial

class EulerNumber:
      def __init__(self, high) -> None:
            """
            Params:
                  - high = nº of iterations toward approximation
            
            """
            self.high = high
      def approximate(self,x):

            """
            
            I 'land' at a = 0 (Maclaurin) conquer rates of changes around (approximating very well the shape) and 
            then attempt to extend the approximation to further away values
            
            """


            euler_value = 0

            for i in range(self.high):

                  euler_value += 1 * (((x)**i) / factorial(i))

            return euler_value
      

temp = EulerNumber(500)
print(temp.approximate(1)) #2.71821...

"""
Truly amazed by the power of derivatives...
"""




