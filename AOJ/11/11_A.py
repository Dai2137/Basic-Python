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

dice = Dice(list(map(int,input().split())))
order = input()
for d in order:
  dice.one_order(d)
print(dice.top)
