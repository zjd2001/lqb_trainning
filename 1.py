import os
import sys

N = 1000 + 10
w = [[0] * N for _ in range(N)]
g = [[''] * N for _ in range(N)]
f = [[float('inf')] * N for _ in range(N)]

n, m, k, p = map(int, input().split())
for i in range(1, n + 1):
    w[i][1:m + 1] = map(int, input().split())

for _ in range(k):
    x, y, z = map(int, input().split())
    w[x][y] += z

for _ in range(p):
    x, y, c = input().split()
    x, y = int(x), int(y)
    g[x][y] = c

f[1][1] = w[1][1]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            continue
        v = min(f[i - 1][j], f[i][j - 1]) + w[i][j]
        if i - 2 > 0 and g[i - 2][j] == 'D':
            v = min(v, f[i - 2][j] + w[i - 1][j] + w[i][j])
        if j - 2 > 0 and g[i][j - 2] == 'R':
            v = min(v, f[i][j - 2] + w[i][j - 1] + w[i][j])
        f[i][j] = v

print(f[n][m])