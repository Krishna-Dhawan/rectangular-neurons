# m = int(input("rows in M1: "))
# m1 = []
# for i in range(m):
#     ri = list(map(int, input().split()))
#     m1.append(ri)
#
# n = int(input("rows in M2: "))
# m2 = []
# for i in range(n):
#     r1 = list(map(int, input().split()))
#     m2.append(r1)


def MatrixProduct(M1, M2, m, n):
    p = len(M2[0])

    M3 = []
    for a in range(m):
        t1 = M1[a]
        t = []
        for j in range(p):
            t2 = []
            s = []
            for k in range(n):
                t2.append(M2[k][j])
            for l in range(n):
                s.append(t1[l]*t2[l])
            t.append(sum(s))
        M3.append(t)
    return M3

#
# print("="*20 + "\n")
# for i in MatrixProduct(m1, m2):
#     print(i)
