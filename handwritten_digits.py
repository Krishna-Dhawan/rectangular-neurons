import openpyxl as opx
import cv2
from matrix_multiply import MatrixProduct
import time
import os

os.chdir("E:/Documents/GitHub/rectangular-neurons")
t = time.time()
img = cv2.imread("Untitled1.png", 1)
res = (27, 27)

weights = opx.load_workbook("digits.xlsx")
bias = 0
weights1 = opx.load_workbook("digits1.xlsx")
sheet1 = weights1["Sheet1"]

M1 = []
M2 = []
response = []
for i in range(10):
    """
        Matrix M1 is a 10x(27*27) matrix with all weights of each
        digit stored in each row. M2 is a column matrix (27*27)x1 
        with px. value / 255 is stored in each row. Output is a 
        10x1 matrix with activation of each output neuron. The
        matrix is multiplied with another weight matrix to get  
        final output
    """
    sheet = weights["Sheet" + str(i + 1)]
    L1 = []
    for j in range(res[0]):
        for k in range(res[1]):
            L1.append(sheet.cell(row=(j + 1), column=(k + 1)).value)
            R, G, B = img[j, k]
            M2.append([G / 255])
    M1.append(L1)
response1 = MatrixProduct(M1, M2, 10, (res[0] * res[1]))

for a in range(10):
    for i in range(10):
        w_list = [[]]
        for j in range(1, 11):
            w_list[0].append(sheet1.cell(row=(i + 1), column=j).value)
        response.append(MatrixProduct(w_list, response1, 1, 10)[0])

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
print(time.time() - t)

feedback = input("am i correct? ")
if feedback == 'no':
    ans = int(input("Correct digit: "))

    cost = 0
    for i in range(1, 11):
        if i == ans:
            cost += (out[i] - 1) ** 2
        else:
            cost += out[i] ** 2

    out_sheet = weights["Sheet" + str(mx + 1)]
    r_sheet = weights["Sheet" + str(ans + 1)]
    for i in range(res[0]):
        for j in range(res[1]):
            R, G, B = img[i, j]
            out_sheet.cell(row=(i + 1), column=(j + 1)).value -= G / 255
            r_sheet.cell(row=(i + 1), column=(j + 1)).value += G / 255

# weights.save("digits.xlsx")
