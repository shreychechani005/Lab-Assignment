basic_salary = int(input("Enter the basic salary: "))

hra = 0.20 * basic_salary  
ta = 0.05 * basic_salary   
da = 0.10 * basic_salary   

gross_salary = basic_salary + hra + ta + da

print("Gross salary is : ",gross_salary)
