N, C = map(int, input().split())
X, V = [], []

cw1 = [0]
cw2 = [0]
ccw1 = [0]
ccw2 = [0]

s = 0
for _ in range(N):
  x, v = map(int, input().split())
  X.append(x)
  V.append(v)
  s += v
  cw1.append(max(cw1[-1], s-x))
  cw2.append(max(cw2[-1], s-2*x))

s = 0

for x,v in zip(X[::-1], V[::-1]):
  s += v
  ccw1.append(max(ccw1[-1], s-(C-x)))
  ccw2.append(max(ccw2[-1], s-(C-x)*2))

ans = 0

for a,b,c,d in zip(cw1, ccw2[::-1], cw2, ccw1[::-1]):
  ans = max(ans, a+b, c+d)

print(ans)

