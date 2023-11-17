def generate():
    name = input("enter a name:  ")
    mrk = float(input("enter the mark: "))
    return name, mrk


def list_of_std(n):
    stud_list = []
    for i in range(n):
        stud_list.append(generate())
    return stud_list
def average(lista=[]):
    total = 0
    for item in lista:
        total += item[1]
    avg = total/len(lista)
    return avg

def run():
    s_list = []
    while True:
     opt = int(input("Meniu:\n\n1-populate Students\n2-Calculate Avg mark\n3-change mark of one\n4-Exit\n"))
     if opt ==4:
            break
     elif opt ==1:
        num = int(input("How many students to add? "))
        s_list.extend(list_of_std(num))
     elif opt == 2:
        print(f"The average mark is {average(s_list):.2f}")
     elif opt == 3:
        name = input("Whose marks shall we change? ")
        for tup in s_list:
            if tup[0] == name:
                n_mrk = float(input("Enter new mark:  "))
                s_list.remove(tup)
                #s_list.append((name, n_mrk))
                s_list.insert(0, (name, n_mrk))
     else:
        print("no such option, try again. fool!")

run()

# print(list_of_std(4))
#
# x = generate()
# print (x)
# print(type(x))
