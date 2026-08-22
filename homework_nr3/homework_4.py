def parse_input(user_input):
    command, *args = user_input.strip().split()
    return command.lower(), args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Введіть ім'я та номер телефону."

    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Введіть ім'я та новий номер телефону."

    name, phone = args
    name = name.lower()

    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact changed."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Введіть ім'я контакту."

    name = args[0].lower()

    if name not in contacts:
        return "Contact not found."

    return f"{name}: {contacts[name]}"


def show_all(contacts):
    if not contacts:
        return "Немає збережених контактів."

    result = []

    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome!")

    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            print("Invalid command.")
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()