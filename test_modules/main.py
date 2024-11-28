import my_module;
# import math; # derrectly import math inbuilt function  
import math as m; # give short name tho the function name 

print(my_module.add_numbers(4,9))

# print("\npi value",math.pi) # use math function's pi module
print("\npi value",m.pi) # use math function's pi module 
print("\ncos(pi)",m.cos(m.pi))
print("\nsin(pi)",m.sin(m.pi))
print("\ntan(pi)",m.tan(m.pi))


