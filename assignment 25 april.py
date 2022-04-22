# Q1. program to find average of three numbers entered by the user
n1 = int(input('enter first number :'))
n2 = int(input('enter second number :'))
n3 = int(input('enter third number :'))
avg = (n1 + n2 + n3)/3
print("average of the three numbers is :",avg)


# Q2. program to compute a person's income tax
income = float(input("enter your gross income (to the nearest penny): "))
no_of_dependents = int(input("enter the number of dependents: "))
taxable_income = income - 10000 - (3000*no_of_dependents)
tax = (taxable_income * 20)/100
print("your tax is :", tax)



# Q3. program to store different data type values into a list.
SID=int(input('Enter your SID : '))
Name= str(input('Enter your Name: '))
Gender=str(input('Enter your Gender(M/F/U): '))
Course_name=str(input('Enter your Course: '))
CGPA=float(input('Enter your CGPA: '))
Student=[SID,Name,Gender,Course_name,CGPA]
print(Student)

# Q4. To enter marks of 5 students into a list and display them in sorted manner.
m1 = int(input('enter the marks of first student: '))
m2 = int(input('enter the marks of second student: '))
m3 = int(input('enter the marks of third student: '))
m4 = int(input('enter the marks of fouth student: '))
m5 = int(input('enter the marks of fifth student: '))
list = [m1,m2,m3,m4,m5]
print(sorted(list))


# Q5.(a) and (b)
color = ['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print(color)
color[3] = 'Purple'
print(color)
