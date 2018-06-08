import sys

sys.setrecursionlimit(2010)

n = int(sys.stdin.readline())
a = []
for i in range(n):
    x, y, t = sys.stdin.readline().split()
    a.append((int(x), int(y), int(t)))

a = sorted(a, key=lambda e: e[2])
tr = [(6, 6, 0)]
tr.extend(a)

p = [None]*n


def man_dist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)


def pega(i):
    if i == n:
        return 1
    if p[i] is None:
        xc, yc, tc = tr[i]
        here = 1 if i > 0 else 0
        maxi = here
        for j in range(i+1, n+1):
            xn, yn, tn = tr[j]
            if man_dist(xc, yc, xn, yn) <= (tn - tc):
                maxi = max(maxi, here + pega(j))
        p[i] = maxi
    return p[i]


print(pega(0))