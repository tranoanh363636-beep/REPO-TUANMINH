import random
a=random.randint(0,10)
for i in range(1,4):
    n=int(input())
    if n==a:
        print("chuc mung bn da doan dung")
        break
    else:
        print("sai roi")
        if n<a:
            print("so bi an lon hon",n)
        else:
            print("so bi an be hon",n)
else:
    print("Rất tiếc, bạn đã đoán sai 3 lần.")
    print("Số bí mật là:",a)         
            
    
