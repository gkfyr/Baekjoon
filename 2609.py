import sys
import math

input = sys.stdin.readline

# n = int(input())
# r = list(map(int, input().split()))


n, m = map(int, input().split())

r = []
arr = list(range(10000))
cdg = 1
csg = 1

for i in arr:
    j = i
    if i != 0 and i != 1:
        r.append(i)
        while j < 10000:
            if arr[j] % i == 0:
                arr[j] = 0
            j += 1


while i < len(r):
    y = r[i]

    if n <= y or m <= y:
        if n % y == 0 and m % y == 0:
            n = n // y
            m = m // y
            cdg = y * cdg
        csg = n * m * cdg
        break

    if n % y == 0 and m % y == 0:
        n = n // y
        m = m // y
        cdg = y * cdg
    else:
        i += 1

if csg == 1:
    csg = n * m * cdg

# cdg = math.gcd(n, m)
# csg = (n * m) // cdg

print(cdg)
print(csg)


# 반례는 4 8 이였다...
