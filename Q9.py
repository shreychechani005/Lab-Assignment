basic_salary = int(input("Enter the basic salary: "))

hra = 0.20 * basic_salary  
ta = 0.05 * basic_salary   
da = 0.10 * basic_salary   

gross_salary = basic_salary + hra + ta + da

print("Gross salary is : ",gross_salary)

l=100000
if gross_salary<3*l:
    print("0%")
elif gross_salary>=3*l and gross_salary<10*l:
    print("10%")
elif gross_salary>=10*l and gross_salary<25*l:
    print("20%")
else:
    print("30%")