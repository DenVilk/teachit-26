def func(a, b):
    return a+b
  
def min(a,b):
    return a if a<b else b

a, b = input().split()
a, b = int(a), int(b)

print(func(a,b))
print(min(a,b))
