def parse_input(user_input):
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]
    return command, args

def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added: {} - {}".format(name, phone)

def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated: {} - {}".format(name, phone)
    else:
        return "Contact not found: {}".format(name)

def show_phone(contacts, name):
    if name in contacts:
        return "{}'s phone number: {}".format(name, contacts[name])
    else:
        return "Contact not found: {}".format(name)

def show_all(contacts):
    if contacts:
        return "\n".join(["{} - {}".format(name, phone) for name, phone in contacts.items()])
    else:
        return "No contacts found"

def main():
    contacts = {}
    print("How can I help you?")

    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Incorrect usage. Use 'add username phone'.")
            else:
                print(add_contact(contacts, args[0], args[1]))
        elif command == "change":
            if len(args) != 2:
                print("Incorrect usage. Use 'change username phone'.")
            else:
                print(change_contact(contacts, args[0], args[1]))
        elif command == "phone":
            if len(args) != 1:
                print("Incorrect usage. Use 'phone username'.")
            else:
                print(show_phone(contacts, args[0]))
        elif command == "all":
            print(show_all(contacts))
        elif command == "close" or command == "exit":
            print("Good bye!")
            break
        else:
            print("Unknown command: {}".format(command))

if __name__ == "__main__":
    main()
