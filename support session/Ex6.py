

#global stud_id
#stud_id = 1001    #global variable -> visible to all functions
def generate():
    name = input("Enter name: ")
    dob = input("Enter date of birth: ")
    age = int(input("Enter age"))
    return name, dob, age, id

def saving():
    with open("students.csv", "a") as f:
        csv_writer = csv.writer(f)
        for bob in students:
            csv_writer.writerow(bob)


def loading(path):
    stud_list = []
    with open(path) as f:
        csv_reader = csv_reader(f)
        for row in csv_reader:
            if len(row)> 0:
                tuple(row)
loading("students.csv")

#t = (generate(), generate(), generate())
#ss == saving(s)

