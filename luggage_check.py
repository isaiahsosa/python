#luggage weight calculator for SkyFly Airlines for heavy luggage
#only measures above 25 pounds

weight = float(input("How many pounds does your suitcase weigh?: "))

if weight >= 50:
  print("There is a $25 charge for luggage that heavy.")
  print("Thank you for your business.")
  
if weight >= 150:
  print ("We do not allow luggage that heavy on the airline")
  print ("Thank you for your business")
  
if weight <= 49:
  print ("Luggage has to be over 50 pounds! Thank you for experiencing SkyFly Airlines!")

