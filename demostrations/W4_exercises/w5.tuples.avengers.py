def adding(lista = []):
    new_member = input("enter name of new avenger:  ")
    lista.append(new_member)

def remove(lista = []):
    name = input("enter name of avenger to be removed: ")
    if name in lista:
        lista.remove(name)

# #avengers = ["hulk", "thor", "ironman"]
# #print(avengers)
# adding(avengers)     (comment: highlight all + ctrl+/)
# print(avengers)
# adding(avengers)
# print(avengers)
# remove(avengers)
# print(avengers)

def printing (lista = []):
    for thing in lista:
        print(f"the mighty {thing} is part of avengers!")
def run():
        avengers = []
        while True:
            opt = int(input(
            '''Avengers, Assemble!
             1-Add an Avenger
             2-Remove Avenger
             3-check the team
             4-Exit
                       ''' ))
            if opt ==1:
                adding(avengers)
            elif opt==2:
                remove(avengers)
            elif opt ==3:
                printing(avengers)
            elif opt ==4:
                break
            else:
                print("no such option. Go specsavers")

run()