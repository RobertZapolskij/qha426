salary = float(input("Enter salary: "))
years = int(input("Enter number of years(whole years): "))

if years > 2 :
    if salary < 25000:
        salary = salary * 1.1           #salary *= 1.1
    else:
        salary += 500
elif years == 1:
    salary += 200
else:
    if salary <= 18000:
        print("oopsie, thats an Error! Your salary is 18000")
        salary = 18000
print(f"your salary from now on will be £{salary:.2f}. Keep up good work")

