import sys

input = sys.stdin.readline

# n = int(input())
# r = list(map(int, input().split()))


n = int(input())
l = []

for i in range(n):
    r = list(map(int, input().split()))
    l.append(r)

l.sort()

for i in range(len(l)):
    print(l[i][0], l[i][1])
