import random
a=(random.randint(1,100))
b=0
while b<=7:
    c=int(input())
    b+=1
    if c==a:
        print("chuc mung")#
    else:
        print("rat tiec bn da thua.So dung la:", a)