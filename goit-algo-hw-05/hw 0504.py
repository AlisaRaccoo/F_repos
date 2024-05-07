def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            error_message = str(e)
            if 'user name' in error_message.lower():
                return "Enter user name."
            elif 'name and phone' in error_message.lower():
                return "Give me name and phone please."
            else:
                return "Invalid input. Please try again."
    return wrapper

class BotHelper:
    def __init__(self):
        self.contacts = {}

    def parse_input(self, user_input):
        parts = user_input.strip().split(' ', 1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ''
        return command, args

    @input_error
    def add_contact(self, args):
        parts = args.split(',')
        if len(parts) != 2:
            raise ValueError("Invalid arguments. Please provide name and phone number separated by comma.")
        name, phone = parts
        self.contacts[name.strip()] = phone.strip()
        return f"Contact '{name}' added successfully."

    @input_error
    def change_contact(self, args):
        parts = args.split(',')
        if len(parts) != 2:
            raise ValueError("Invalid arguments. Please provide name and new phone number separated by comma.")
        name, new_phone = parts
        if name.strip() not in self.contacts:
            raise KeyError(f"Contact '{name}' not found.")
        self.contacts[name.strip()] = new_phone.strip()
        return f"Phone number for contact '{name}' changed successfully."

    @input_error
    def show_phone(self, args):
        if args.strip() not in self.contacts:
            raise KeyError(f"Contact '{args}' not found.")
        return f"Phone number for contact '{args}' is {self.contacts[args]}"

    def main(self):
        print("Welcome to Bot Helper!")
        while True:
            user_input = input("Enter command: ")
            command, args = self.parse_input(user_input)
            if command == 'exit' or command == 'close':
                print("Exiting Bot Helper. Goodbye!")
                break
            elif command == 'add':
                print(self.add_contact(args))
            elif command == 'change':
                print(self.change_contact(args))
            elif command == 'show':
                print(self.show_phone(args))
            else:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    bot = BotHelper()
    bot.main()
