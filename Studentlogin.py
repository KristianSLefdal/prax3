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

        choice = input("Please insert where you wanna navigate:")
        if (choice == "Moodle"):
            print("Welcome to NIS 2022/2023 page")
        elif (choice == "Linkdinlearning"):
            print("Welcome to Linkdinlearning")
        elif (choice == "Openathens/openathens"):
            print("Welcome to Openathens")
        else:
            print("Invalid selection")
    else:
        print("MFA Incorrect")
else:
    print("Username/password incorrect")