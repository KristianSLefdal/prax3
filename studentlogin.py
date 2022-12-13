continueLogon = True
counter = 0

while continueLogon == True:

    username = input("please enter username: ")
    password = input("enter password: ")

    if (username == "student") and (password == "noroff"):

        MFA = input("please enter code from device:")
        
        if (MFA == "123456"):
            print("Hold on meanwhile we logging you in")
            print("LOADING.")
            print("LOADING..")
            print("LOADING...")
            print("Welcome to Noroff Student page.")

            while True:
                choice = input("Please insert where you wanna navigate:")
                if (choice == "Moodle"):
                    print("Welcome to NIS 2022/2023 page")
                    continueLogon = False
                    break

                elif (choice == "Linkdinlearning"):
                    print("Welcome to Linkdinlearning")
                    continueLogon = False
                    break

                elif (choice == "Openathens"):
                    print("Welcome to Openathens")
                    continueLogon = False                    
                    break

                else:
                    print("Invalid selection")
        else:
            print("MFA Incorrect")
    else:
        print("Username/password incorrect")
        counter += 1
        if counter > 2:
            print("Too many failed logon atempts\n")
            break

print("\nProgram ended\n")