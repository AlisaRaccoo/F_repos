import re
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number format.")
        super().__init__(value)

    def validate_phone(self, phone_number):
        return bool(re.match(r'^\d{10}$', phone_number))

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

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





    

    
