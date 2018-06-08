import sys

sys.stdin.readline()
Qs = sorted([int(i) for i in sys.stdin.readline().split()])
Ns = sorted([int(i) for i in sys.stdin.readline().split()])

n = len(Qs)
c = 0

j = 0
for i in range(n):
    while j < n and Qs[i] >= Ns[j]:
        j += 1
    if j == n:
        break
    if Ns[j] > Qs[i]:
        c += 1
        j += 1

print(c)
