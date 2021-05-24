def max3_v1(a, b, c):
  if (a >= b) and (a >= c):
    largest = a
  elif (b >= a) and (b >= c):
    largest = b
  else:
    largest = c     
  return largest

def max3_v2(a, b, c):
  if (a >= b) and (a >= c):
    return a
  elif (b >= a) and (b >= c):
    return b
  else:
    return c

def max3_v3(a, b, c):
  if (a>=b):
    if (a>=c):
      largest=a
    else:
      largest=c
  else:
    if (b>=c):
      largest=b
    else:
      largest=c
  return largest

def max3_v4(a, b, c):
  if (a>=b):
    if (a>=c):
      return a
    else:
      return c
  else:
    if (b>=c):
      return b
    else:
      return c

def max3_v5(a,b,c):
  arr = []
  arr.append(a)
  arr.append(b)
  arr.append(c)
  max = arr[0]
  for i in arr:
    if (i>max):
      max=i
  return max

x = int(input())
y = int(input())
z = int(input())

print(max3_v1(x,y,z))

