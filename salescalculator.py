
totalsales = 0
salescounter = 0
counter = 0
valueentered = float(input("please enter your sales number: "))


if valueentered < 5000:
    #continue
    pass
if 5000 < valueentered < 10001:
    salescounter += 1
    totalsales += valueentered
    averagesales = totalsales / salescounter

    print("This sale was:\t\t", valueentered)
    print("number of sales this month: \t", salescounter)
    print("your total sale this month is: \t", totalsales)
    print("your average sale was: \t\t", averagesales)

else:
    print("a possible data entry error has occourred")