counter = [0 for i in range(ord('z') - ord('a') + 1)]
while True:
  try:
    texts = input()
    texts = texts.lower()
    for d in texts:
      if ord('a') <= ord(d) <= ord('z'):
        counter[ord(d) - ord('a')] += 1
  except EOFError:
    break   #文字列の読み込みと記録

for j in range(ord('z') - ord('a') + 1):
  print(chr(j+ord('a')) + " : " + str(counter[j])) #出力
