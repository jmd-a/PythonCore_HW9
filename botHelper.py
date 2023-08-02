def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid input."
    return wrapper

contacts = {}

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."

@input_error
def change_contact(name, phone):
    contacts[name] = phone
    return f"Phone number for {name} updated to {phone}."

@input_error
def get_phone(name):
    return f"The phone number for {name} is {contacts[name]}."

def show_all_contacts():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def main():
    while True:
        user_input = input("Enter a command: ").lower().split(" ", 2)
        command = user_input[0]

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            try:
                name = user_input[1]
                phone = user_input[2]
                response = add_contact(name, phone)
                print(response)
            except IndexError:
                print("Give me name and phone please.")
        elif command == "change":
            try:
                name = user_input[1]
                phone = user_input[2]
                response = change_contact(name, phone)
                print(response)
            except IndexError:
                print("Give me name and phone please.")
        elif command == "phone":
            try:
                name = user_input[1]
                response = get_phone(name)
                print(response)
            except IndexError:
                print("Enter user name.")
        elif command == "show":
            if user_input[1] == "all":
                print(show_all_contacts())
        elif command in ["good", "bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()