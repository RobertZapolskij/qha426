print("program started")
char = input("please enter a letter: ")

if len(char) == 1:
     value = ord(char)
     print(f"the ASCII code for {char}, is {value}")
else:
    print("wrong input")

print("program ended")