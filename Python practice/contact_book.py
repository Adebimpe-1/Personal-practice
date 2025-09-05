# Basic program to create a contact list
contacts = {}

def load_contacts():
    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                name, phone = line.strip().split(',')
                contacts[name] = phone
    except FileNotFoundError:
        pass

def save_contacts():
    with open('contacts.txt', 'w') as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

def add_contact(name, phone):
    contacts[name] = phone

def search_contact(name):
    return contacts.get(name, "Contact not found.")

def main():
    load_contacts()
    while True:
        choice = input("Choose: 1.Add 2.Search 3.Exit: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
            save_contacts()
        elif choice == '2':
            name = input("Enter name to search: ")
            print(search_contact(name))
        elif choice == '3':
            break
        else:
            print("Invalid choice")

main()
