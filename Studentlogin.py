username = input(" please enter username:")
password = input(" please enter password:")

if (username == "student") and (password == "noroff"):

    MFA = input("please enter code from device: ")
    if (MFA == "123456"):
        print("you succesfully have been logged")
        print ("Loading.")
        print ("Loading..")
        print ("Loading...")
        print("Welcome to student page.")

        choice = input("Please insert where you want to navigate: ")
        if (choice == "moodle"):
            print("Welcome to NIS 2022 & 2023 student page")
        if (choice == "Linkdinlearning"):
            print("Welcome to linkdinlearning!")
        if (choice == "openathens"):
            print("Welcome to openathens!")
        else:
            print("invalid selection")
    
    else:
        print("MFA incorrect")

else:
    print("username/ password incorrect")    
