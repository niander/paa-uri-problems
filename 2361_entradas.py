import sys


while True:
    N, K = sys.stdin.readline().split()
    N = int(N)
    K = int(K)

    if N == 0 and K == 0:
        break

    j = N
    for i in range(1, N+1):
        if i < K:
            sys.stdout.write(str(i) + " ")
        else:
            sys.stdout.write(str(j) + " ")
            j -= 1

    sys.stdout.write("\n")
