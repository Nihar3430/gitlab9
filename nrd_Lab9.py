def encode(password):
    new_password = ""
    for char in password:
        char = int(char) + 3
        new_password += str(char)
    return new_password

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("\nPlease enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            new_pass = encode(password)
            print("Your password has been encoded and stored!")

if __name__ == "__main__":
    main()