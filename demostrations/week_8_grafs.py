import json
import matplotlib.pyplot as plt

def save(dictio = {}):
    with open("survey.json", "w") as f:
        json.dump(dictio, f)

def load ():
    with open("survey.json", "r") as f:
        d = json.load()
    return d

def survey(n=3):
    s={}
    for i in range(n):
        resp = ""
        while resp not in ("me", "partner", "pet", "child"):
            resp = input("Who is rules in yout house?(ME, partner, pet, child)   ").lower()
        s[resp] = s.get(resp, 0) +1
    return s

#print(survey(5))
def run():
    data = {}
    while True:
        opt = int(input("Menu:\n1-New Survey\n2-Load survey\n3-Save Data\n4-Visualise\n0-Exit\n    "))
        if opt == 1:
            n = int(input("number of respondents:  "))
            data = survey(n)
        elif opt == 2:
            data = load()
        elif opt == 3:
            save(data)
        elif opt == 4:
            opt2 = int(input("chose type:\n1-Point Graph\n2-Bar Chart\n3-Pie Chart  \n  "))
            if opt2 == 1:
                plt.plot(data.keys(), data.values(), "y^-")
                plt.xlabel("The king of the house")
                plt.ylabel("Freguency")
            elif opt2 == 2:
                plt.bar(data.keys(), data.values(), color = "#a512b1")1

                plt.ylabel("The king of the house")
                plt.ylabel("Frequency")
            elif opt2 == 3:
                plt.pie(data.values(), labels=data.keys(),autopct="%.0f")
            else:
                print("No graph option. Chose number 1 oor 3")
            plt.title("power struggle in students houses")
            plt.show()
        elif opt == 0:
            break
        else:
            print("No such menu option. Chose number 1 or 4")

run()