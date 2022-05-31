import openpyxl as opx
import cv2
from matrix_multiply import MatrixProduct
import time

t = time.time()
img = cv2.imread("ML_Data/Untitled1.png", 1)
res = (27, 27)

weights = opx.load_workbook("ML_Data/digits.xlsx")
bias = 0

M1 = []
M2 = []
for i in range(10):
    sheet = weights["Sheet" + str(i+1)]
    L1 = []
    for j in range(res[0]):
        for k in range(res[1]):
            L1.append(sheet.cell(row=(j+1), column=(k+1)).value)
            R, G, B = img[j, k]
            M2.append([G/255])
    M1.append(L1)

response = MatrixProduct(M1, M2, 10, 729)
out = {}
mx = 0
for i in range(len(response)):
    out[i] = response[i][0]
    if out[i] > out[mx]:
        mx = i
print(out)
print(f"I think the digit you drew is {mx}")
print(time.time()-t)

feedback = input("am i correct? ")
if feedback == 'no':
    ans = int(input("Correct digit: "))
    out_sheet = weights["Sheet" + str(mx+1)]
    r_sheet = weights["Sheet" + str(ans+1)]
    for i in range(res[0]):
        for j in range(res[1]):
            R, G, B = img[i, j]
            out_sheet.cell(row=(i+1), column=(j+1)).value -= G/255
            r_sheet.cell(row=(i+1), column=(j+1)).value += G/255

weights.save("ML_Data/digits.xlsx")
