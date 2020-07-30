import random
def get_code(xx):
   a='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   b=''
   for i in range(xx):
        c=random.randint(0,61)
        b+=a[c]
   return b
a=get_code(22)
print(a)
