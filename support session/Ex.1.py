f_n = input("Enter first name:  ")
s_n = input("Enter second name:  ")
age = int(input("Enter age:  "))
h = float(input("Enter heigh:  "))
w = float(input("Enter weight:  "))

bmi = w/(h*h)

print(f"{f_n} {s_n} - your age next year will be {age+1} and your bmi is {bmi:.2f}")
