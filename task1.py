def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    full_name = f"{first_name} {last_name}"
    print(f"Full name: {full_name}")

    alternative_str = full_name[::2]
    print(f"String with every other character: {alternative_str}")

if __name__ == "__main__":
    main()
