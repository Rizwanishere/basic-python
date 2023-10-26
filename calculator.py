
'''a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
multiplication=(a)*(b)
division=(a)/(b)
sum=(a)+(b)
subtraction=(a)-(b)
print("The multiplicaton of two numbers: ",multiplication)
print("The division of two numbers: ",division)
print("The addition of two numbers is: ",sum)
print("The subtraction of two numbers is: ",subtraction)

print(eval(input("Enter an equation:")))


x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python programming is " + x) 
myfunc()
print("ICT Facility in LORDS are " + x)


def reverse_number(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev
# Test the function
num = 12345
print("Original number:", num)
print("Reversed number:", reverse_number(num))




def myfunc():
    for i in range(6):
        for j in range(6-i):
            print(" ",end="")
        for k in range(i):
            print("*",end=" ")
        print("\n")
myfunc()



dictlang = { 'c#': 6, 'GO': 89, 'Python': 4, 'Rust':10 }
for _ in sorted(dictlang):
    print (dictlang[_])


set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Using the union() method
result = set1.union(set2)
print(result)


class Operations:
    a = 10
    b = 20
    def addition(self):
        addition = self.a + self.b
        print("Sum of a and b is:", addition)
class MyClass(Operations):
    c = 50
    d = 10
    def subtraction(self):
        subtraction = self.c - self.d
        print("Subtraction of c and d is:", subtraction)
obj = MyClass()
obj.addition()
obj.subtraction()



class Addition:
    a = 10
    b = 20
    def add(self):
        sum = self.a + self.b
        print("Sum of a and b is:", sum)
class Subtraction(Addition): 
    def sub(self):
        sub = self.b - self.a 
        print("Subtraction of a and b is:", sub)
class Multiplication(Subtraction): 
    def mul(self):
        multi = self.a * self.b
        print("Multiplication of a and b is:" , multi)
ob = Multiplication () 
ob.add()
ob.sub()
ob.mul()



class Employee:
    id = 2786
    name = "Abdul Rais" 
    def display(self):
        print("Name of the Employee: ",self.name) 
        print("ID of the Employee:",self.id)
# Creating a emp instance of Employee class 
obj = Employee()
obj.display()



lower = 0
upper = 10
print("Prime number between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)


print("hello world")
print("welcome to programming")

print("input format")
k=float(input())
print("output format:")
print("%f" %k)
print("%.3f" %k)
print("%.2f" %k)
print("%.1f" %k)


y=input("enter a value")
x=ord(y)
print(x)'''


l=int(input("enter a number:"))
b=int(input("enter second number"))
print(2*(l+b))
print(l*b)



