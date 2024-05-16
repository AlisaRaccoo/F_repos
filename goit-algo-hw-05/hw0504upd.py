def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter valid user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Incomplete command. Please provide necessary arguments."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated: {} - {}".format(name, phone)
    else:
        return "Contact not found: {}".format(name)

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return "{}'s phone number: {}".format(name, contacts[name])
    else:
        return "Contact not found: {}".format(name)

@input_error
def show_all(args, contacts):
    if contacts:
        return "\n".join(["{} - {}".format(name, phone) for name, phone in contacts.items()])
    else:
        return "No contacts found"

def parse_input(user_input):
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]
    return command, args

def main():
    contacts = {}
    print("How can I help you?")

    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        elif command == "close" or command == "exit":
            print("Good bye!")
            break
        else:
            print("Unknown command: {}".format(command))

if __name__ == "__main__":
    main()
