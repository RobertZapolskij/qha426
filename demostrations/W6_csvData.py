import csv
import matplotlib.pyplot as plt
def gather_data(n=1):
    with open("oct_data.csv", "w") as f:
        csv_writer = csv.writer(f)
        for i in range(n):
            h = float(input("enter height: "))
            w = float(input("Enter weight: "))
            csv_writer.writerow([h,w])

def retrieve_data():
    with open("oct_data.csv") as f:
        csv_reader = csv.reader(f)
        hs =[]
        ws = list()
        for row in csv_reader:
            if len(row) !=0:
                hs.append(float(row[0]))
                ws.append(float(row[1]))
        return hs, ws


#print(retrieve_data())
def graph():
    x,y = retrieve_data()
    plt.plot(x,y, "b^--")
    plt.show()
graph()
