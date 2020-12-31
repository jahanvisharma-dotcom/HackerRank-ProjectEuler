#!/bin/python3
import sys

g = []
for _ in range(20):
    grid_t = [0,0,0]
    grid_t.extend([int(x) for x in input().split()])
    grid_t.extend([0,0,0])
    g.append(grid_t)
pad = [0]*26
for _ in range(3):
    g.append(pad)
m = []
for r in range(20):
    for c in range(3,23):
        m1 = g[r][c]*g[r][c+1]*g[r][c+2]*g[r][c+3]
        m2 = g[r][c]*g[r+1][c]*g[r+2][c]*g[r+3][c]
        m3 = g[r][c]*g[r+1][c+1]*g[r+2][c+2]*g[r+3][c+3]
        m4 = g[r][c]*g[r+1][c-1]*g[r+2][c-2]*g[r+3][c-3]
        m.append(max(m1,m2,m3,m4))
print(max(m))
