#imports a library -> turtle libary is  a grpahics libary that shows a "turtle" in which you can move around with commands; essentially we can create shapes and it provides us with a virtual canvas
import turtle
#imports a random library -> random library randomly retrives an item from a list
import random 


#shapes option -> user can select different choices to show different shapes 
def ShapesOption():
  
  #picks a random color and stores that color into a variable
  randomColorOne = random.choice(["Red", "Yellow", "Blue", "green", "pink","purple", "yellow", "gray"])
  randomColorTwo = random.choice(["Orange", "Red", "Blue", "green", "pink","purple", "yellow", "gray"])

  #displays different options to the user 
  print ("-----------------------------------------------------")
  print("Welcome to Shapes!")
  print("#1 for crazy zigzag")
  print("#2 for pentagon")
  print("#3 for Rose")
  print ("-----------------------------------------------------")

  UserShapeInput = (int(input("Please select an interger option above: ")))
  print ("-----------------------------------------------------")

  #determines if the user chose option one from the list
  #creates a crazy zigzag 
  if UserShapeInput == 1:
    #resets the virtual canvas
    turtle.reset()
    #colors the virtual canvas with a random color from the list
    turtle.bgcolor(randomColorOne)
    #speeds up the movement of the turtle 
    turtle.speed(100000)
    #changes the size of the turtle's pen 
    turtle.pensize(5)
    
    
    countCount = 1
    while countCount < 8:
      #changes the color of the turtle 
      turtle.color(randomColorTwo)
      #changes the angle of the turtle 
      turtle.setheading(180)
      #moves the turtle forward 
      turtle.forward(190)
      turtle.setheading(270)
      turtle.forward(10)
      turtle.setheading(0)
      turtle.forward(190)
      turtle.setheading(270)
      turtle.forward(10)
      countCount = countCount + 1
    turtle.setheading(180)
    turtle.forward(190)

  #determines if the user chose option two from the list
  #creates a pentagon
  elif UserShapeInput == 2: 
    turtle.reset()
    turtle.bgcolor(randomColorOne)
    turtle.speed(10000)
    turtle.pensize(2)
    countCount = 1
    #moves until the pentagon is created
    for i in range(100):
      turtle.color(randomColorTwo)
      turtle.right(60)
      turtle.forward(1+countCount)       
      countCount = countCount + 1
        
  #determines if the user chose option three from the list
  #creates a rose 
  elif UserShapeInput == 3: 
    turtle.reset()
    turtle.bgcolor(randomColorOne)
    turtle.speed(10000)
    turtle.pensize(2)
    countCount = 1
    #moves until a rose is created
    for i in range(100):
      turtle.color(randomColorTwo)
      turtle.right(250)
      turtle.forward(100+countCount)
        

        
      countCount = countCount + 1

#game function -> lets the user play a game, trying to guess a random number 
def GuessingOption():
  print ("-----------------------------------------------------")
  print("Welcome to the guesssing game!")
  #ask for user input
  userAnswer = (int(input("Guess a number bewteen 1-10: ")))

  #this picks a random code from 1 -10 and stores that into a variable 
  correctAnswer = random.randint(1,10)

  #holds a count
  count = 0

  #This code will keep repeating until the user guesses the correct answer 
  while (userAnswer != correctAnswer):
      
      #checks if the user input is too low from correct answer
      #adds a count
      #ask the user to try again
      if (userAnswer < correctAnswer):
          count = count +1
          print("Too low!")
          userAnswer = (int(input("Try again: ")))


      #checks if the user input is too high from correct answer
      #adds a count
      #ask the user to try again
      elif (userAnswer > correctAnswer):
          count = count + 1
          print("Too High!")
          userAnswer = (int(input("Try again: ")))


  #checks if the user input is equal to the correct answer
  #adds a count
  #displays the amount of counts the user took and a congrats to the user 
  if (userAnswer == correctAnswer):
      count = count + 1
      print ("-----------------------------------------------------")
      print("You got it")
      print("It only took you", count , "tries")
      print ("-----------------------------------------------------")

 

  
    
#place holder 
menu = 1 

#this while loop makes the program loop as long as the user does not input 3
while (menu!=3):
    #displays options for the User
    #asks the user for an input 
    print ("-----------------------------------------------------")
    print ("#1 for shapes:")
    print ("#2 for Coinflip:")
    print ("#3 to exit:")
    print ("-----------------------------------------------------")
    menu = (int(input("Please select number #1-3:")))


    #the shapes Option function will run if user chose 1
    if menu == 1:
      ShapesOption()

    #the guessing Option function will run if user chose 2
    elif menu == 2:
      GuessingOption()

    #the program will exist if user chose 3 
    elif menu == 3:
      quit()