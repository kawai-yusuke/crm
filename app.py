from db import find_all_users, add_user


def main():
    print("==== Welcome to CRM Application =====")
    print("[S]how all customers information")
    print("[A]dd new customer")
    print("[Q]uit")
    print("==============================")

    command = input("Your Command > ")

    while command != "q":
        if command == "s":
            print("顧客一覧を表示します")

            for user in find_all_users():
                name = user[0]
                age = user[1]

                print(f"Name: {name} Age: {age}")

        elif command == "a":
            print("新規の顧客情報を追加します")

            name = input("new customer's name ? > ")
            age = input("new customer's age ? > ")

            add_user(name, age)

            print(f"Add new customer {name}")
            
        else:
            print(f"{command}: command not found")

        command = input("Your Command > ")

    print("Bye")


if __name__ == '__main__':
    main()
