# |s| <= 50 でAC. cppで書き換え中

s = input()
k = int(input())

def solve():
  memo = []
  sortedS = sorted(set(s))
  for letter in sortedS:
    for start in [i for i in range(len(s)) if s[i]==letter]:
      for end in range(start+1, len(s)+1):
        substr = s[start:end]
        i = 0
        if substr in memo: continue
        while i<len(memo) and is_X_larger_than_Y(substr,memo[i]):
          i+=1
        if(len(memo)==0): memo.append(substr)
        else: memo.insert(i, substr)
    if k<=len(memo): return memo[k-1]
  

def is_X_larger_than_Y(x, y): # true: 1, false:0, equal: 2
  for i in range(min( len(x), len(y) )):
    if x[i]==y[i]: continue
    elif x[i] < y[i]: return 0
    else: return 1
  if len(x) == len(y): return 2
  elif len(x) < len(y): return 0
  else: return 1

print(solve())

