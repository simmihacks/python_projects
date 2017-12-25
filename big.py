#this code get 3 numbers and see's which one is bigger
#made by @simmihacks 12/24/17: Merry Christmas!!!!

a = int(input("please enter a num: "))
b = int(input("please enter another num: "))
c = int(input("please enter a num: "))

if a>b and b>c:
    print("larger num is " + str(a))
else:
    if b>a and a>c:
        print("larger num is " + str(b))
if c>b and b>a:
    print("larger num is " + str(c))
if c==b and a==b and a==c:
    print("Three numbers are same")
if c==b or a==b or a==c:
    print("Two numbers are the same")
