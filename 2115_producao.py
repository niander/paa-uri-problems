import sys


while True:
    maybe_new = sys.stdin.readline()
    if maybe_new == "":
        break
    n = int(maybe_new)
    tasks = []
    for i in range(n):
        d, p = sys.stdin.readline().split()
        tasks.append((int(d), int(p)))
    tasks = sorted(tasks, key=lambda e: e[0])
    time = 1
    for i in range(n):
        if time < tasks[i][0]:
            time = tasks[i][0]
        time += tasks[i][1]
    print(time)
