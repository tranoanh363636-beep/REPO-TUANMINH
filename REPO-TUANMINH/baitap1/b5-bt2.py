a=int(input())
b=int(input())
c=int(input())
if a==0 and b==0 or b**2-4*a*c<0:
    print("pt vo ngo")
elif a==0:
    print("pt co 1 ngo la:",-c/b)
elif b**2-4*a*c==0:
    print("pt co 1 ngo la:",-b/(2*a))
else:
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    print(f"pt co 2 ngo la:{x1} va {x2}")