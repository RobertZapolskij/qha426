def shop():
    items = {"wine": 9.99, "cheese": 2.99, "bacon": 1.99, "bread": 1.99, "croissant": 0.99}
    return items

def view_all(products={}):
    for x, y in products.items():
        print(f"{x}----------£{y}")

#view_all(shop())


def basket():
    b = []
    while True:
        p = input("Enter an item or \"stop\": ")
        if p.upper() == "STOP":
            break

        q = int(input(f"Enter the quantity of {p}: "))
        for i in range(q):
            b.append(p)
    return b


def till(basket={}):
    all_items = shop()
    total = 0
    for prod in basket:
        if prod.lower() in all_items:
            total += all_items[prod]
        else:
            print(f"No luck. The {prod} is not in stock. Go to LIDL ")
    return total
#print(f"{till(basket()):.2f}")
def run():
    print("Welcome to Robs shop. Please look around. we are watching")
    view_all(shop())
    b = basket()
    while True:
        response = input("Are you ready to pay? [y/n]: ")
        if "y" in response.lower():
            to_pay = till(b)
            print(f"pay £{to_pay} or I will come after you! ")
            break
        else:
            b2 = basket()
            b.extend(b2)

run()



