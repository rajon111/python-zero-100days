myName = input("What's you name?: ")
print(myName)

myAge = input("How old are you? :")
if myAge <= "17":
  print("You are a teenager")
if myAge >= "18":
  print("You are an adult")
if myAge >= "50":
  print("You are old")
  
replit = input("Do you like Replit?")
if replit.lower() == "yes" :
  print("OF COURSE YOU DO!")
else:
  print("opps! No")