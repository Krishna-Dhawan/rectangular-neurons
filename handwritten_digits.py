from __future__ import division
import openpyxl as opx
import cv2
from matrix_multiply import MatrixProduct
import time
import os
import json
from funcns import *
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

os.chdir("E:/Documents/GitHub/rectangular-neurons")
tme = time.time()
img = cv2.imread("Untitled1.png", 1)
res = (27, 27)

weights = opx.load_workbook("digits.xlsx")
bias = 0
weights1 = opx.load_workbook("digits1.xlsx")
sheet1 = weights1["Sheet1"]

with open("weights.json") as fil:
    data = json.load(fil)

M1 = []
M2 = []
response = []
for i in range(10):
    """
        Matrix M1 is a 10x(27*27) matrix with all weights of each
        digit stored in each row. M2 is a column matrix (27*27)x1 
        with px. value / 255 is stored in each row. Output is a 
        10x1 matrix (response1) with activation of each output neuron. 
        The matrix is multiplied with another weight matrix to get  
        final output
    """
    # i = digit, j = row, k = column
    sheet = weights["Sheet" + str(i + 1)]
    L1 = []
    for j in range(res[0]):
        for k in range(res[1]):
            L1.append(sheet.cell(row=(j + 1), column=(k + 1)).value)
            # the weights are stored in a json file to make a cost function
            data["1"][str((res[0] * res[1]) * i + res[0] * j + k)] = sheet.cell(row=(j + 1), column=(k + 1)).value
            R, G, B = img[j, k]
            M2.append([G / 255])
    M1.append(L1)
response1 = MatrixProduct(M1, M2, 10, (res[0] * res[1]))

for i in range(len(response1)):
    """
        The activations are turned into a number between 0 
        and 1 using the sigmoid function
    """
    response1[i][0] = sigmoid(response1[i][0])

for a in range(10):
    """
        sheet1 contains 10 rows representing 10 weights of
        each of 10 neurons in 10 columns. a is the number
        of digits, w_list is a 1x10 matrix containing weights
        and is multiplied with the 10x1 matrix to give a 1x1 
        matrix representing activation of the digit 'a'
    """
    w_list = [[]]
    for j in range(10):
        w_list[0].append(sheet1.cell(row=(a + 1), column=(j + 1)).value)
        data["2"][str(10 * a + j)] = sheet1.cell(row=(a + 1), column=(j + 1)).value
    response.append(MatrixProduct(w_list, response1, 1, 10)[0])

with open("weights.json", "r+") as fil:
    json.dump(data, fil)

print(response1)
print(response)
out = {}
mx = 0
for i in range(len(response)):
    out[i] = response[i][0]
    if out[i] > out[mx]:
        mx = i
print(out)
print(f"I think the digit you drew is {mx}")
print("time:", time.time() - tme)

feedback = input("am i correct? ")
if feedback == 'no':
    ans = int(input("Correct digit: "))

    cost = find_cost(out, ans)
    print(cost)
    for i in range(1, 3):
        for j in range(27 * 27 * 10):
            # diff()
            pass

    out_sheet = weights["Sheet" + str(mx + 1)]
    r_sheet = weights["Sheet" + str(ans + 1)]
    for i in range(res[0]):
        for j in range(res[1]):
            R, G, B = img[i, j]
            out_sheet.cell(row=(i + 1), column=(j + 1)).value -= G / 255
            r_sheet.cell(row=(i + 1), column=(j + 1)).value += G / 255

# weights.save("digits.xlsx")
# weights1.save("digits1.xlsx")
