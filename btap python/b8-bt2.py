a=int(input())
if a==2 or a==3:
    print("a la snt")
else:
    for i in range (3,a):
        if a%2==0 or a%3==0:
            print("a ko la snt")
        else:
            print("a la snt")
        break    