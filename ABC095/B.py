import math
N, X = map(int, input().split())
M = [int(input()) for i in range(N)]
print(N + math.floor((X - sum(M))/min(M)))

