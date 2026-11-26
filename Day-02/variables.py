num1,num2,num3 = 10,20,30
print(num1,num2,num3)
print("variable references are:", id(num1), id(num2), id(num3))

print("assign single value to multiple variables")
num1=num2=num3= 350
print(num1, num2, num3)
print("variable references are:", id(num1), id(num2), id(num3))

print("approach 2")
num1,num2,num3 = 256, 256, 256
print(num1,num2,num3)
print("variable references are:", id(num1), id(num2), id(num3))
