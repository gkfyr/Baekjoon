import sys
import math

input = sys.stdin.readline

# n = int(input())
# r = list(map(int, input().split()))


n, m = map(int, input().split())

# r = []
# arr = list(range(10000))
# cdg = 1
# csg = 1

# for i in arr:
#     j = i
#     if i != 0 and i != 1:
#         r.append(i)
#         while j < 10000:
#             if arr[j] % i == 0:
#                 arr[j] = 0
#             j += 1


# for i in range(len(r)):
#     if n <= r[i] or m <= r[i]:
#         csg = n * m * cdg
#         break

#     if n % r[i] == 0 and m % r[i] == 0:
#         n = n // r[i]
#         m = m // r[i]
#         cdg = r[i] * cdg

# if csg == 1:
#     csg = n * m * cdg

cdg = math.gcd(n, m)
csg = (n * m) // cdg

print(cdg)
print(csg)
