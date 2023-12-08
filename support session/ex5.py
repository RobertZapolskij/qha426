import math
from random import randint as ran
def menu()
     print("Menu: \n1-message\n2-triarea\n3-triprism\n4-circarea\n5-lotto")
      opt = int(input())
        if opt ==3:
            break

def message():
    print("kurwa mac!!")

def triarea(b=2,h=2):
    area = 0.5*b*h
    return area
def triprism(b, h, l):
    v = triaera(b,h)*l
    return v

def circarea(r):
    area = math.pi * r**2
    return area

def lotto():
    for i in range(6):
        print(ran (1, 59), end="\t")

def main():
    while True:
        x = menu()
        if == 6:
            break
        elif x == 1:
            b = float(input("Enter base: "))
            h = float(input("Enter height:  "))
            t_a = triarea (b, h)
            print(f"Area of this triangle is {t_a}")
        elif x == 2:
            base = float(input("Enter base: "))
            height = float(input("Enter height:  "))
            lenght = float(input("Enter lenght of prism:"))
            print(f"Volume of the prism")
        elif x == 3:
            radius = float(input("Enter the radius: "))
            print(f"")





#x = triarea(1,2) + triarea(10,5) + triarea()
#print(f"total area is {x}cm^2")

