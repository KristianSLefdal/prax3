postcodes ={7013 : "Trondheim", 6415 : "Molde",637 : "Oslo",8450 : "Stokmarknes", 7340 : "Oppdal",
6783 : "Stryn", 4005 : "Stavanger", 5073 : "Bergen",  }

pcentered = int(input("enter a valid postcode: "))
if pcentered in postcodes.keys():
    print("postcode:",pcentered, "-",postcodes[pcentered], "\n")
else:
    print("invald postal number")