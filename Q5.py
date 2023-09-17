num = int(input("Enter a 5 digit number : "))
A = num//10000
print(A)
B = num%10000
C = B//1000
print(C)
D = num%1000
E = D//100
print(E)
F = num%100
G = F//10
print(G)
H = num%10
print(H)
print(A,C,E,G,H)
print(H,G,E,C,A)