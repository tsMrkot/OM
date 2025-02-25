from sympy import *
import math
import numpy as np

eps = 10 ** - 6

x = Symbol('x')
val = x*x - sin(x)
func = lambdify(x, val, modules=['numpy'])


def diff_func(diff_level):
    return diff(x*x - sin(x), x, diff_level)

def golden_ratio_method ():
    i = 0
    a = 0
    b = math.pi / 2
    sqrt_five = 5 ** (1/2)
    while abs(b - a) >= eps:
        x_left = a + (3 - sqrt_five)/2 * (b - a)
        x_right = a + (sqrt_five - 1)/2 * (b - a)
        func_left = func(x_left)
        func_right = func(x_right)
        if func_left > func_right: a = x_left 
        else: b = x_right
        i += 1
        print (i)


    print("Точка минимума: " + str(float((a + b) / 2)) + "\n Количество итераций: " + str(i))


def tangent_method ():
    i = 0
    a = 0
    b = math.pi / 2
    fun = 0
    tang = 0
    dif = lambdify(x, diff_func(1), modules=['numpy'])

    xm = (func(b) - func(a) + dif(a)*a - dif(b)*b)/(dif(a)) - dif(b)
    print (xm)
    while abs(fun - tang) >= eps:
        xm = (func(b) - func(a) + dif(a)*a - dif(b)*b)/(dif(a)) - dif(b)
        print (xm)


tangent_method()
#golden_ratio_method()
#print(diff_func(1))
#dif = lambdify(x, diff_func(1))
#print (dif(0))