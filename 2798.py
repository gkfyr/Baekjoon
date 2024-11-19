import sys

input = sys.stdin.readline

# n = int(input())
# r = list(map(int, input().split()))


n, m = map(int, input().split())
r = list(map(int, input().split()))


def solve():
    le = len(r)
    ss = []
    for i in range(n):
        for j in range(i + 1, le):
            for k in range(j + 1, le):
                t = r[i] + r[j] + r[k]
                ss.append(t)

    best_op = 0

    for i in ss:
        if i > m:
            continue
        elif i == m:
            return i
        else:
            if best_op < i:
                best_op = i
    return best_op


print(solve())
