n = int(input())

count = [[[0 for i in range(10)] for j in range (3)] for k in range(4)] #count初期化

for l in range(n):
  b,f,r,v = map(int,input().split())
  count[b-1][f-1][r-1] += v  #count記録

for i in range(4):
  for j in range(3):
    print('', *count[i][j])
  if i != 3:
    print('#' *20) #count出力
