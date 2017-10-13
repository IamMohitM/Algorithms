import time

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# l = [i for i in range(1, 11, 1)]


# print(i)


def cut_rod(p, n):
    if n == 0:
        return 0

    q = float("-inf")
    for j in range(1, n + 1, 1):
        # print(j, n - j)
        q = max(q, p[j] + cut_rod(p, n - j))
        # print(q)
    return q


t = time.time()
print(cut_rod(p, 10))
print(time.time() - t)


# print("total calls

def Bottom_Up_Cut_Rod(p, n):
    r = [0]
    for j in range(1, n + 1, 1):
        # print("j=", j)
        q = float("-inf")
        for i in range(1, j + 1, 1):
            # print("i=", i)
            q = max(q, p[i] + r[j - i])
        # print("q=", q)
        r.append(q)
    return r[n]


t = time.time()
print(Bottom_Up_Cut_Rod(p, 10))
print(time.time() - t)
