import string

def decrypt(text, key):
    '''
    :param text: Text to decrypt
    :param key: shift key for the cipher
    :return: decrypted string
    '''
    returnval = ""
    try:
        ## If both the plain text character and
        # the keyword are spaces (ASCII 32) you end up with negative 1:
        # You'll have to consider how to handle this case in your cipher
        # or strip spaces altogether, which is what traditionally was done.
        returnval= ''.join([chr(ord(char) - key) for char in text])
    except ValueError:
        s1=set(x for x in string.printable)
        s2=set(chr(x) for x in range(32,127))
        returnval = ''.join(choice(s2) for i in range(len(text)))
    return returnval


def encrypt(text, key):
    '''
        :param text: Text to encrypt
        :param key: shift key for the cipher
        :return: encrypted string
        '''
    returnval = ""
    try:
        ## If both the plain text character and
        # the keyword are spaces (ASCII 32) you end up with negative 1:
        # You'll have to consider how to handle this case in your cipher
        # or strip spaces altogether, which is what traditionally was done.

        returnval = ''.join([chr(ord(char) + key) for char in text])
    except ValueError:
        pass
    return returnval



def bruteforce(text):
    # because 95 characters between 32 and 126
    shiftrange = 94
    # list to store the result
    result = []
    for i in range(0, shiftrange+1):
        # calling decrypt function for every key
        decrypted = decrypt(text=text, key=i)
        decrypted = "key " + str(i) + ": " + decrypted
        result.append(decrypted)
    return '\n'.join(result)

    


def menu():

    print("\n\n\nWelcome to the Caesar Shifter.")
    # Set the beginning choice and store the function objects.
    choice = -1
    choices = {'1': encrypt, '2': decrypt, '3': bruteforce}
    # Loop as long as the user doesn't choose `quit`.
    while choice != '4':
        print("\n\n **** MENU **** \n\n")
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
            print("In option - %s"%choice)
            text = input("Please give me a word:")
            shift = input("Please provide a shift amount. Range [1- 94]:")
            print(func(str(text), int(shift)))

        elif choice == '3':
            print("In option - %s" % choice)
            text = input("Please give me a word:")
            print(func(str(text)))







menu()
