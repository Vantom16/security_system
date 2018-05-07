#Creating our Age Identification System for our Movies.
# Code output is displayed in command line

# Our Movie dictionary
films = {
   "Finding Dory":[3,6],
   "Bourne": [18,6],
   "Tarzan": [15,6],
   "Ghost Busters":[12,6],
   "Avengers Inifinity":[15,6]
}

while True:
  choice = input("What film would you like to watch?: ").strip().title()
  if choice in films:
#Convert age into integer
    age = int(input("How old are you?: ").strip())
# First element in dictionary values corresponds to age.
# Check user age
    if age >= films[choice][0]:
# Check available seats
# Second element in our dictionary values correspondsto available seats.
      if films[choice][1]>0:
         num_seats = films[choice][1]
# Subtracting seats taken from total seats
      if num_seats > 0:
         print("Enjoy the film!")
         films[choice][1] = films[choice][1] -1
      else:
         print("Sorry, we are sold out!")
    else:
        print("You are too young to see that film!")
  else:
      print("We don't have that film ...")
