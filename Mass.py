talent_str = input("Enter mass in talent: ")
talent = float(talent_str)
pound_str = input("Enter mass in pound: ")
pound = float(pound_str)
lot_str = input("Enter mass in lot: ")
lot = float(lot_str)
grams = float(talent*20*32*13.3) + float(pound*32*13.3) + float(lot*13.3)
kilograms = int(grams/1000)
grams_str = float(grams)-kilograms*1000
rounded = round(grams_str, 2)
print("The weight in modern units is " +str(kilograms) + " kilograms and " + str(rounded) + " grams.")

