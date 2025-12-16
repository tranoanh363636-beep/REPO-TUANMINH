a=int(input())
if a%15==0:
    print("Fizz-Buzz")
elif a%3==0:
    print("Buzz")
elif a%5==0:
    print("Fizz")
else:
    print(a)