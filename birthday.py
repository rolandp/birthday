import sys

def birthday_wish(name):
  print(f"Gefeliciteerd {name}!")
  print("Fijne dag en tot zondag!")

# Check if a name is provided as a command line argument
if len(sys.argv) > 1:
  birthday_person = " ".join(sys.argv[1:])
else:
  birthday_person = input("Je bent je naam vergeten. Hoe heet je? ")

# Call the function to wish them a happy birthday
birthday_wish(birthday_person)
