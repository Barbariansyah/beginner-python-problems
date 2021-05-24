size = int(input())

outline = input()[0]
fill = input()[0]

def square_v1(x):
  # assumes x>1
  for i in range(x):
    print(outline, end='')
  print()
  for i in range(x-2):
    print(outline, end='')
    for i in range(x-2):
      print(fill, end='')
    print(outline)
  for i in range(x):
    print(outline, end='')
  print()

def square_v2(x):
  for i in range(x):
    print(outline, end='')
  print()
  for i in range(x-2):
    print(outline, end='')
    for i in range(x-2):
      print(fill, end='')
    print(outline)
  if (i>1):
    for i in range(x):
      print(outline, end='')
    print()

def square_v3(x):
  print(outline*x)
  for i in range(x-2):
    print(outline+fill*(x-2)+outline)
  if (x>1):
    print(outline*x)

square_v3(size)

