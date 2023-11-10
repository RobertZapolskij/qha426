def dimentions():
    w = float(input("Enter the width of the room: "))
    l = float(input("Enter the lenght of the room: "))
    return l*w

#print(dimentions())
#print(f" The room has area {dimentions()}m^2")

def r_name():
    return input("Enter room name:  ")
#print(r_name())


def price(name ="", area = 1):
    if name.lower() == "bathroom":
        return 15*area
    elif name.lower() == "bedroom":
        return 10*area
    else:
        return 5*area

def run():
    t_price = 0
    num = int(input("How many rooms to clean? "))
    for i in range(num):
        room = r_name()
        area = dimentions()
        p = price(room, area)
        t_price += p
        print(f"The total price is £{t_price}")
run()


#print(price("bedroom", 20))
#print(price("attic", 10))
#print(price("bathroom", 50))
