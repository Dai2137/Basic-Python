n = int(input())
cards = [[False for j in range(13)] for i in range(4)] #所有カード配列を初期化
pattern = ["S","H","C","D"]
for k in range(n):
  ch,rank = input().split()
  rank = int(rank)
  cards[pattern.index(ch)][rank-1] = True #cards[i][j]を記録
for i, row in enumerate(cards):
  for j, elem in enumerate(row):
    if cards[i][j] == False:
      print(pattern[i], j+1)