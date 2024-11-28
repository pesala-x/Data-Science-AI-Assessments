def add_numbers(a, b):
    result = a+b
    return result

def substract(x,y):
    result = x-y
    return result

if __name__  == "__main__" : # this section make for test perposes 
    print("this will execute if this file run dirrectly..")
    print(add_numbers(4,9))
    print(substract(4,9))