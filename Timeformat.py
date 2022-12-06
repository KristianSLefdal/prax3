intime = int(input("Enter time format hours: "))
#time can be between 0-23
if 0 <= intime <= 23:

    if 8 <= intime <17:
        print("Its working hour still")
    else:
        print(" do not work anymore you earned yourself some hours off  ")
else:
    print("wrong input")