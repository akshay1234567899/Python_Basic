import calculation

# -------------------------------
import calculation as cal
# --------------------------------

# ----------------------------------
calculation.add(10,20)
calculation.mul(20,30)



# Approach-2
cal.add(10,20)
cal.mul(20,30)


# approach-3 : import for specific method
from calculation import add
from calculation import  mul

add(20,40)
mul(21,30)


# if you have more number of classes and you need to import method so use from calculation import *
