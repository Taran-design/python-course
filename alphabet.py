def is_alphabet(char):
    return char.isalpha()

def main():
    try:
        user_input = input("Enter a single character: ").strip()

        if len(user_input) != 1:
            print("Error: Please enter exactly one character.")
            return

        if is_alphabet(user_input):
            print(f"'{user_input}' is an alphabet letter.")
        else:
            print(f"'{user_input}' is NOT an alphabet letter.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()




