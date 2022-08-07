a,b,c = map(int, input().split())
i = 0
for k in range(a, b+1):
  if c % k == 0:
    i += 1
print(i)
