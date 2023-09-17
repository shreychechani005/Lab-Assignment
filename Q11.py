a=input()
b=input()
c=input()
p=int(a)
q=int(b)
r=int(c)
z=int(a+b+c)
if (p*p*p+q*q*q+r*r*r)==z:
    print("yes, it's an armstrong number")
else:
    print("No it is not an armstrong number")