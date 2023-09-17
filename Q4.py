num = int(input())
A = num // 100
print(A)

c = num % 100

B = c // 10
print(B)

b = c%10

print(b)

print("Sum is " ,A + b + B)

sum = A + B + b
if sum % 3 == 0:
    print(num ,"is Divisible by 3")
else:
    print(num ," is not Divisible by 3")


