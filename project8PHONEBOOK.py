contact = {}
def display():
    print("Your contact list: ")
    for name , number in contact.items():
        print(f"{name} : {number}")
while True:
    choice = int(input("1. Add new Contact \n" "2. Search Contact \n" "3. Display Contact \n" "4. Edit Contact \n" "5. Delete Contact \n" "6. Exit \n" "Enter your choice:"))
    if choice == 1:
        name = input("Enter your contact name: ")
        num = input("Enter your contact number: ")
        contact[name] = num
    elif choice == 2:
        search = input("Enter your contact name: ")
        if search in contact:
            print(f"Your contact name is {search} and number is {contact[search]}")
        else:
            print("Contact not found!")
    elif choice == 3:
        if not contact:
            print("Your contact list is empty!")
        else:
            display()
    elif choice == 4:
        oldcontact = input("Enter contact name: ")
        if oldcontact in contact:
            newnum = input("Enter new number: ")
            contact[oldcontact] = newnum
            print(f"Your new contact number updated succesfully and new number is {contact[oldcontact]}")
            display()
        else:
            print("Name is not found!")
    elif choice == 5:
        del_contact = input("Enter contact name that you wanna delete: ")
        if del_contact in contact:
            confirmation = input(f"Do you want to delete this{del_contact} contact? [y/n]")
            if confirmation == "y":
                print("Succesfully deleted")
                contact.pop(del_contact)
            display()
        else:
            print("Conatact not found!")
    else:
        break