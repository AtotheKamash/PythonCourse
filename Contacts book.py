# Define an empty dictionary to store the contacts
contacts = {}

# Function to create a new contact
def create_contact(name, phone_number):
    contacts[name] = phone_number
    print(f"Hi {name}, your contact was successfully created with phone number {phone_number}")

# Function to find a contact by name
def find_contact(name):
    if name in contacts:
        print(f"Hi {name}, we found your contact with phone number {contacts[name]}")
    else:
        print(f"Sorry {name}, we couldn't find a contact with that name")

# Function to update the phone number of a contact
def update_contact(name, phone_number):
    if name in contacts:
        contacts[name] = phone_number
        print(f"Hi {name}, your phone number was updated to {phone_number}")
    else:
        print(f"Sorry {name}, we couldn't find a contact with that name")

# Function to remove a contact by name
def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Hi {name}, your contact was successfully removed from the contact book")
    else:
        print(f"Sorry {name}, we couldn't find a contact with that name")

# Program loop to allow the user to interact with the contact book
while True:
    print("Hi there! Welcome to your Contact Book.")
    print("What would you like to do today?")
    print("1. Create a new contact")
    print("2. Find a contact by name")
    print("3. Update the phone number of a contact")
    print("4. Remove a contact by name")
    print("5. Exit the program")

    choice = input("> ")
1
    if choice == "1":
        name = input("Great! What's the name of your new contact? ")
        phone_number = input("What's their phone number? ")
        create_contact(name, phone_number)

    elif choice == "2":
        name = input("Sure thing! What's the name of the contact you're looking for? ")
        find_contact(name)

    elif choice == "3":
        name = input("Which contact would you like to update? Please enter their name. ")
        phone_number = input("What's their new phone number? ")
        update_contact(name, phone_number)

    elif choice == "4":
        name = input("Which contact would you like to remove? Please enter their name. ")
        remove_contact(name)

    elif choice == "5":
        print("Thank you for using your Contact Book. Goodbye!")
        break

    else:
        print("Sorry, I didn't understand that. Please choose a valid option.")
