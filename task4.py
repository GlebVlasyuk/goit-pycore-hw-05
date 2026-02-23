def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."

    return inner


def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].lower()  # перше слово - команда
    args = parts[1:]  # все інше - аргументи
    return command, args


@input_error
def say_hello(_args, _contacts):
    return "How can I help you?"


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact changed."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(_args, contacts):
    if not contacts:
        return "No contacts yet."

    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            print("Please enter a command.")
            continue

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print(say_hello(args, contacts))
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
