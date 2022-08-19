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

dice1 = Dice(list(map(int,input().split())))
dice2 = Dice(list(map(int,input().split())))

for l in 'NWWNWW': #上面が1,2,3,5,6,4,1の順になるように
  for i in range(4): #側面を1周
    if dice1.top == dice2.top and dice1.s == dice2.s and dice1.e == dice2.e and dice1.w == dice2.w and dice1.n == dice2.n and dice1.bot == dice2.bot:
      print('Yes')
      break
    for d in 'SEN':
      dice2.one_order(d) #側面を90度回転
  if dice1.top == dice2.top and dice1.s == dice2.s and dice1.e == dice2.e and dice1.w == dice2.w and dice1.n == dice2.n and dice1.bot == dice2.bot:
    break
  dice2.one_order(l)

if not (dice1.top == dice2.top and dice1.s == dice2.s and dice1.e == dice2.e and dice1.w == dice2.w and dice1.n == dice2.n and dice1.bot == dice2.bot):
  print('No')
