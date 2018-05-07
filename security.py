#Creating our Security System
# Code output is displayed in command line
#First we create a list of known users

known_users = ["Alice", "Jane", "David", "Paul", "Eli", "Isme"]

while True:
    print("Hi! My name is Joe")
    name =input("What is your name?: ").strip().capitalize()
#Computer will compare name given and ones in our database.
    if name in known_users:
        print("Hello {}".format(name))
# If our users wants to be removed from the system
        remove = input("Would you like to be removed from the system (y/n)?").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem. I didn't want you to leave anyway! ")


    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_me =input("Would you like to be added to our system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries. See you around!")
