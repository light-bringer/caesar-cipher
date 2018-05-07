def decrypt(text, key):
    return ''.join([chr(ord(char) - key) for char in text])


def encrypt(text, key):
    return ''.join([chr(ord(char) + key) for char in text])



def bruteforce(text):
    shiftrange = 95
    result = []
    for i in range(0, shiftrange):
        decrypted = decrypt(text=text, key=i)
        result.append(decrypted)
    return '\n'.join(result)

    


def menu():

    print("\n\n\nWelcome to the Caesar Shifter.")
    # Set the beginning choice and store the function objects.
    choice = -1
    choices = {'1': encrypt, '2': decrypt, '3': bruteforce}
    # Loop as long as the user doesn't choose `quit`.
    while choice != '4':
        print("\n\nWhat would you like to do?")
        print("Option 1: Encrypt Word")
        print("Option 2: Decrypt Word")
        print("Option 3: Brute Force")
        print("Option 4: Exit.")

        choice = input("Pick your selection: ")
        # Try and get the function. If this errors its because the the choice
        #  was not in our options.
        try:
            func = choices[choice]
        except KeyError:
            if choice != '4':
                print("Incorrect selection. Please choose either 1, 2, 3 or 4")
                continue
        if choice!='3' and choice!='4':
            text = input("Please give me a word:")
            shift = input("Please provide a shift amount:")
            print(func(text, int(shift)))
        elif choice == '3':
            text = input("Please give me a word:")
            print(func(text))
        print(choice)






menu()