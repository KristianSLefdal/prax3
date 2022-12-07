total = 0
entered = 0
while entered != -1:

    # catch invalid data
    try:
        entered = int(input("enter a value (or -1 to quit): "))

        #adding only positive values to total
        if entered >= 0:
            total += entered
    except:
        print ("input need to be a numeric value")

print()
print("-" * 20)
print("total sum=", total, "\n")