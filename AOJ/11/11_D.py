class Dice:
  def __init__(self,pips):
    self.top = pips[0]
    self.s = pips[1]
    self.e = pips[2]
    self.w = pips[3]
    self.n = pips[4]
    self.bot = pips[5]
    
  def one_order(self,d):
    if d == 'E':
      self.top,self.e,self.w,self.bot = self.w,self.top,self.bot,self.e
    elif d == 'N':
      self.top,self.s,self.n,self.bot = self.s,self.bot,self.top,self.n
    elif d == 'S':
      self.top,self.s,self.n,self.bot = self.n,self.top,self.bot,self.s
    elif d == 'W':
      self.top,self.e,self.w,self.bot = self.e,self.bot,self.top,self.w
  #1回回した時の操作

n =int(input())
dice = [[]*6]*n
for s in range(n):
  dice[s] = Dice(list(map(int,input().split())))

judge = 0
for k in range(n-1):
  for m in range(k+1,n):
    for l in 'NWWNWW': #上面が1,2,3,5,6,4,1の順になるように
      for i in range(4): #側面を1周
        if dice[k].top == dice[m].top and dice[k].s == dice[m].s and dice[k].e == dice[m].e and dice[k].w == dice[m].w and dice[k].n == dice[m].n and dice[k].bot == dice[m].bot:
          judge += 1
          break
        for d in 'SEN':
          dice[m].one_order(d) #側面を90度回転
      if judge > 0:
        break
      dice[m].one_order(l)
    if judge > 0:
      break
  if judge > 0:
    break

if judge == 0:
  print('Yes')
else:
  print('No')
