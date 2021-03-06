import math
import os
import json

os.chdir("E:/Documents/GitHub/rectangular-neurons")
with open("Activations.json") as fil:
    data = json.load(fil)


def sigmoid(x):
    try:
        return 1 / (1 + math.exp(-x))
    except OverflowError:
        if x > 0:
            q = float("inf")
        else:
            q = -float("inf")
        return 1 / (1 + math.exp(-q))


def sigmderiv(x):
    """I couldn't get sympy to get the derivative of
    a function at a point so had to calculate myself.
    Thanks for nothing, sympy"""
    try:
        return math.exp(-x) / ((1 + math.exp(-x)) ** 2)
    except OverflowError:
        return 0


def find_cost(out, ans):
    cost = 0
    for i in range(10):
        if i == ans:
            cost += (sigmoid(out[i]) - 1) ** 2
        else:
            cost += sigmoid(out[i]) ** 2
    return cost
