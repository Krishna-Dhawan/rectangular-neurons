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
    """
    :param M1: a 2-D list with order m x n
    :param M2: a 2-D list with order n x p
    :return: M3 (m x p) = M1*M2, calculated by making lists
            of the current row of M1, current column of M2
            and adding the products of corresponding elements
            of the lists.
    :param m: .
    :param n: .
    """
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
