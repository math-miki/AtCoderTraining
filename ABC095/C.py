A, B, C, X, Y = map(int, input().split())
 
min_cost = A*X + B*Y
for i in range(1, 1+max(X,Y)):
  cost = i*C*2 + max(0,X-i)*A + max(0,Y-i)*B
  min_cost = min(min_cost, cost)
 
print(min_cost)

