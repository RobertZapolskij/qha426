
print("program started")
number = abs(int(input("please enter ASCII code ")))

if number in range (32, 126):
    character = chr(number)
    print(f"the character represented by the ASCII code {number} is {character}")
else:
    print("chose number from the range of 32 126")
print("program ended")






