from operator import add, truediv, mul, sub
def basic_op(operator, value1, value2):
    return {'+':add , '-':sub, '*': mul, '/':truediv}[operator](value1,value2)
