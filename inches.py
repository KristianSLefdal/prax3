def metric_converter(valueininches):
    centimeters = valueininches * 2.54
    print("your value is:", valueininches, "inches")
    print("thats similar to:", round(valueininches * 2.54, 2),"centimeters")

value = float(input("enter value be converted"))
metric_converter(value)
print("end of program")