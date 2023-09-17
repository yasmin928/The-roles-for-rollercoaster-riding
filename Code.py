print("Welcome to the rollercoaster!")

#Ask user to input his height and converting the number into int
height = int(input("What is your height in cm? "))

#The value of the bill
bill = 0

#checking the hight
if height >= 120:
  print("You can ride the rollercoaster! ")
  #Nested if statements and elif statements
  #check the age
  age = int(input("What is your age? "))
  if age < 12 :
    print("Pleas pay $5.")
    bill = 5
  #too add many conditions just use elif  
  elif age <= 18 :
    print("Pleas pay $7.")  
    bill = 7
  #Using Logical operators
  #give the Midifile crisis a free ride
   elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")  
  else:
    print("Pleas pay $12.")
    bill = 12
 wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")
   
else:
  print("Sorry, You have to groe taller brfore you can ride.")
