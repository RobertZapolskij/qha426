import random #Taking definitions from package "random" into my scope
secret = random.randint(1,20)
print("welcome to my guess game. I am thinking of a number between 1 and 20")

for attempt in range(5):
    print(f"Attempt nr{attempt+1}")
    guess =int(input("take a guess : "))
    if guess == secret:
        print("condrats! you won")
        break
    elif guess> secret:
        print("to high")
    else:
        print("too low")

if guess != secret:
    Print(f"Game over! my number was {secret}")