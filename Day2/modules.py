"""
import math
from math import sqrt
print(sqrt(16))
print(math.__name__)
print(math.__doc__)
"""


import TC_Modules
TC_Modules.welcome()
print(TC_Modules.data)
print(TC_Modules.add(500,600))
print(TC_Modules.sub(800,600))


from TC_Modules import student
TC_Modules.welcome()
print(TC_Modules.data)
print(TC_Modules.add(500,600))
print(TC_Modules.sub(800,600))
s=student("Ravi",25)
s.show()