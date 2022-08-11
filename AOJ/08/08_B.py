while True:
  x = input()
  if x == '0':
    break
  print(sum([int(val) for val in x]))
