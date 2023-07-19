#16026792
import turtle # Enable Turtle use for this code 
import time # Enable to use time.sleep
turtle.setup(500,500)#Setting the size of the game window
turtle.bgcolor("teal")#Turtle background colour
turtle.title("Guess the word game")#Turtle window title
t1 = turtle.Turtle() #Decleration of first Turtle (Global)
t2 = turtle.Turtle() #Decleration of second Turtle (Global)
t1.pensize(5) #Turtle pensizes
t2.pensize(5)
t1.penup()
t1.goto(-240, 210) # Coordinates for in game title
t1.pendown
t1.color("black") #Pen colour
t1.write("Guess the word:", font = ("Arial", 25, "italic")) # In game title itself
t1.hideturtle() # Global hide of the Turtle cursor's
t2.hideturtle()
def main(): # Main function

    guess_remaining = 8 #Wrong answers
    guesses = 0 #User input
    print ("-------------- PLAYER 1 --------------\n") # Start of player 1's turn
    print ("(Make sure PLAYER 2 is not peaking)") # Little hint to make sure chosen word is hidden during input
    time.sleep(3) # Little break to give player 1 time to think and make sure player 2 is not "Peaking"
    word = str(input("(Enter your word (if it has a space, use '-', e.g ice-cream or 'E' to end):")) # promt of Input of the word, saved as a string at first 
    list(word) #Turing the imputed word into a list to be stored
    word = (list(word))#makeing the input "word" to be represented by individual letters
    print ("\n" * 50) # Spaceing to hide player 1's inputted word

    print ("-------------- PLAYER 2 --------------\n") # Start of player 2's turn
    print ("Ready?") 
    time.sleep(3) #Again a little break to give player 2 some time to get set up.
    while guesses < 8: # While guesses are less than 8
        for char in word: # for character (Letter) in player 1's word
            print ("Time to guess the word")
            guess = input("Please enter a letter:") # Player 2's letter (Guess)
            if char in guess: # If letter from word is the same as guessed letter print "That is correct" 
                print ("That is correct\n")
                break # Break from loop
            else: # If guessed letter is not the same a letter in word, print error message.
                print ("You done goofed, guess again")
                guesses = guesses + 1 #To save the amount of guesses 
                guess_remaining = guess_remaining - 1 #After a wrong input, remaining guesses go down. (Used for counter and turtle) 
                print ("You have", guess_remaining, " guesses left \n")#Console based promt for remaining guesses.
                t2.clear()#Clearing 2nd turtle to reset guess remaining counter for in game promt every loop.
                t2.penup()
                t2.goto(-175,-240)
                t2.pendown
                t2.color("black")
                t2.write("You have " + str(guess_remaining) + " attempts left", font = ("Arial", 25, "italic"))# in game remaining wrong guesses promt, resets every loop.
                #Below is all the turtle code for the drawing of the Ambulance, non circles have loops in for efficiency 
                #Body
            if guess_remaining == 7:
                t1.penup()
                t1.goto(-100, 100)
                t1.pendown()
                t1.fillcolor("white")
                t1.begin_fill()
                for i in range(2):
                    t1.forward(175)
                    t1.right(90)
                    t1.forward(150)
                    t1.right(90)
                t1.end_fill()
                #Drivercompartment       
            if guess_remaining == 6:
                    t1.penup()
                    t1.goto(75,50)
                    t1.pendown()
                    t1.fillcolor("white")
                    t1.begin_fill()
                    for i in range(4):
                        t1.forward(100)
                        t1.right(90)
                    t1.end_fill()
                    #rearwheel  
            if guess_remaining == 5:
                t1.penup()
                t1.goto(-60,-80)
                t1.pendown()
                t1.fillcolor("black")
                t1.begin_fill()
                t1.circle(30)
                t1.end_fill()
                #forward wheel
            if guess_remaining == 4:
                t1.penup()
                t1.goto(120,-80)
                t1.pendown()
                t1.fillcolor("black")
                t1.begin_fill()
                t1.circle(30)
                t1.end_fill()
                 #windshield
            if guess_remaining == 3:
                t1.penup()
                t1.goto(75,50)
                t1.pendown()
                t1.fillcolor("blue")
                t1.begin_fill()
                for i in range(2):
                    t1.forward(85)
                    t1.right(90)
                    t1.forward(40)
                    t1.right(90)
                t1.end_fill()
                #Lights
            if guess_remaining == 2:
                t1.penup()
                t1.goto(-20,120)
                t1.pendown()
                t1.fillcolor("Red")
                t1.begin_fill()
                for i in range(2):
                     t1.forward(30)
                     t1.right(90)
                     t1.forward(20)
                     t1.right(90)
                t1.end_fill()
                #Firstcross
            if guess_remaining == 1:
                t1.penup()
                t1.goto(-20,70)
                t1.pendown()
                t1.fillcolor("Red")
                t1.begin_fill()
                for i in range(2):
                    t1.forward(20)
                    t1.right(90)
                    t1.forward(60)
                    t1.right(90)
                t1.end_fill()
                #Secondcross
            if guess_remaining == 0:
                t1.penup()
                t1.goto(-40,50)
                t1.pendown()
                t1.fillcolor("Red")
                t1.begin_fill()
                for i in range(2):
                    t1.forward(60)
                    t1.right(90)
                    t1.forward(20)
                    t1.right(90)
                t1.end_fill()
                t1.penup()
                t1.goto(-100,150)
                t1.pendown
                t1.color("black")
                t1.write("Game over", font = ("Arial", 25, "italic"))#Game over message
                print ("Out of attempts, Game over") # console Game over message
                
                break
        
          
main()

