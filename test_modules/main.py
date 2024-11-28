import my_module;
from my_module import * ; # import all functions from another module 
# from my_module import  add_numbers,substract; # import one by one functions from another module 
# import math; # derrectly import math inbuilt function  
import math as m; # give short name tho the function name 

print(my_module.add_numbers(4,9))

# print("\npi value",math.pi) # use math function's pi module
print("\npi value",m.pi) # use math function's pi module 
print("cos(pi)",m.cos(m.pi))
print("nsin(pi)",m.sin(m.pi))
print("tan(pi)",m.tan(m.pi))


