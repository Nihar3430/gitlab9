def encode(password):
    new_password = ""
    for char in password:
        char = int(char) + 3
        new_password += str(char)
    return new_password

def decode(password):
    decoded_password = ""
    for char in password:
        char = int(char) - 3
        decoded_password += str(char)
    return decoded_password

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("\nPlease enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            new_pass = encode(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            decoded_password = decode(new_pass)
            print(f"The encoded password is {new_pass}, and the original password is {decoded_password}.")
        if option == 3:
            break

if __name__ == "__main__":
    main()