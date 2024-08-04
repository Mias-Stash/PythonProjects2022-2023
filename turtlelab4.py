# Group 1
# 12/7/23
# Turtle Lab 4
# Turtle TicTacToe

###Previous classmates names have been changed for sake of privacy###

###This was an assignment for my first Python class! The goal was to make a functional Tic Tac Toe
###game using the turtle module and terminal.

#importing turtle
import turtle
#making the window 500x500
turtle.setup(500, 500)



### Student 1

def Student1Art():
    #pen setup
    turtle.speed(10)
    turtle.setheading(0)
    turtle.penup()
    turtle.bgcolor("cyan")
    turtle.goto(-250,-180)
    turtle.pencolor("green")
    turtle.fillcolor("green")

    #draws grassy ground
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()

    #pen setup
    turtle.penup()
    turtle.pencolor("grey")
    turtle.fillcolor("grey")

    #draw 2 small mountains
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.end_fill()

    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(80)
    turtle.left(120)
    turtle.forward(80)
    turtle.end_fill()

    #set pen
    turtle.penup()
    turtle.pencolor("white")
    turtle.fillcolor("white")

    #mountain ice caps
    turtle.begin_fill()
    turtle.right(180)
    turtle.forward(50)
    turtle.pendown()
    turtle.right(60)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(30)
    turtle.end_fill()

    #ice caps 2
    turtle.penup()
    turtle.right(60)
    turtle.forward(20)
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(20)
    turtle.pendown()
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(30)
    turtle.end_fill()

    #set pen
    turtle.penup()
    turtle.pencolor("yellow")
    turtle.fillcolor("yellow")

    #draw sun in top right corner
    turtle.goto(230,200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()



### Mia

#draw X function! it will accept a list object, which is associated with
#a pair of coordinates (the start of the turtle's path!)
def drawX(ListCoordinateX, ListCoordinateY):
    X= int(ListCoordinateX)
    Y= int(ListCoordinateY)
    turtle.setheading(0)
    turtle.penup()
    turtle.pensize(3)
    turtle.color("red")
    #This turtle will start in the top right of its box
    turtle.goto(X, Y)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(100)
    turtle.penup()
    turtle.left(135)
    turtle.forward(75)
    turtle.left(135)
    turtle.pendown()
    turtle.forward(100)

#draw O function! it will accept a list object, which is associated with
#a pair of coordinates (the start of the turtle's path!)
def drawO(CIRCLEListCoordinateX, CIRCLEListCoordinateY):
    X= int(CIRCLEListCoordinateX)
    Y= int(CIRCLEListCoordinateY)
    turtle.setheading(0)
    turtle.penup()
    turtle.pensize(3)
    turtle.color("blue")
    radius = int()
    radius = 50
    #This turtle will start in the top right of its box
    turtle.goto(X, Y)
    turtle.pendown()
    turtle.circle(radius)

#draw the grid!
def drawGrid():
    turtle.setheading(0)
    turtle.pensize(3)
    turtle.color("black")
    #horizontal lines
    turtle.penup()
    turtle.goto(-250,80)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-250,-80)
    turtle.pendown()
    turtle.forward(500)
    #vertical lines
    turtle.penup()
    turtle.goto(-85,250)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(85,250)
    turtle.pendown()
    turtle.forward(500)
    

def main():
    #declare variables
    ListX = []
    ListY = []
    CIRCLEListX = []
    CIRCLEListY = []
    ListCoordinateX = int()
    ListCoordinateY = int()
    CIRCLEListCoordinateX = int()
    CIRCLEListCoordinateY = int()
    current_board = [""]
    comp_list = [""]
    comp_list_count = int()
    choice = str()
    space = str()

    #making the lists. numbers will be matched Vertically
    ListX = [-200,-30,150,-200,-30,150,-200,-30,150]
    ListY = [200,200,200,30,30,30,-130,-130,-130]
    CIRCLEListX = [-170,0,170,-170,0,170,-170,0,170]
    CIRCLEListY = [120,120,120,-50,-50,-50,-210,-210,-210]

    #create empty board list 
    current_board = ["","","","","","","","",""]
    #single loop - create list of available spaces, letters A - I
    comp_list = ["","","","","","","","",""]
    for ascii in range (65,74):
        comp_list[comp_list_count] = chr(ascii)
        comp_list_count = comp_list_count + 1

    #call function to draw background
    Student1Art()

    #call function to draw tictactoe grid
    drawGrid()
    #print the tictactoe space guide
    print(" A | B | C ")
    print(" - + - + - ")
    print(" D | E | F ")
    print(" - + - + - ")
    print(" G | H | I ")

    #for loop
    for count in range (0, 9):
        #input of X or O
        choice = input("Please choose either X or O: ")
        #elif statements assign each space to a pair of coordinates
        #and add the player's symbol to the current_board list
        if (choice == "X") or (choice == "x"):
            # Call Lani's Function
            space = humaninput(comp_list)
            if space == "A":
                ListCoordinateX = ListX[0]
                ListCoordinateY = ListY[0]
                current_board[0] = "X"
            elif space == "B":
                ListCoordinateX = ListX[1]
                ListCoordinateY = ListY[1]
                current_board[1] = "X"
            elif space == "C":
                ListCoordinateX = ListX[2]
                ListCoordinateY = ListY[2]
                current_board[2] = "X"
            elif space == "D":
                ListCoordinateX = ListX[3]
                ListCoordinateY = ListY[3]
                current_board[3] = "X"
            elif space == "E":
                ListCoordinateX = ListX[4]
                ListCoordinateY = ListY[4]
                current_board[4] = "X"
            elif space == "F":
                ListCoordinateX = ListX[5]
                ListCoordinateY = ListY[5]
                current_board[5] = "X"
            elif space == "G":
                ListCoordinateX = ListX[6]
                ListCoordinateY = ListY[6]
                current_board[6] = "X"
            elif space == "H":
                ListCoordinateX = ListX[7]
                ListCoordinateY = ListY[7]
                current_board[7] = "X"
            elif space == "I":
                ListCoordinateX = ListX[8]
                ListCoordinateY = ListY[8]
                current_board[8] = "X"
            else:
                print("Invalid space!")
                continue
            drawX(ListCoordinateX, ListCoordinateY)

        elif choice == "O" or (choice == "o"):
            # Call Student 2's Function
            space = computer(comp_list)
            if space == "A":
                CIRCLEListCoordinateX = CIRCLEListX[0]
                CIRCLEListCoordinateY = CIRCLEListY[0]
                current_board[0] = "O"
            elif space == "B":
                CIRCLEListCoordinateX = CIRCLEListX[1]
                CIRCLEListCoordinateY = CIRCLEListY[1]
                current_board[1] = "O"
            elif space == "C":
                CIRCLEListCoordinateX = CIRCLEListX[2]
                CIRCLEListCoordinateY = CIRCLEListY[2]
                current_board[2] = "O"
            elif space == "D":
                CIRCLEListCoordinateX = CIRCLEListX[3]
                CIRCLEListCoordinateY = CIRCLEListY[3]
                current_board[3] = "O"
            elif space == "E":
                CIRCLEListCoordinateX = CIRCLEListX[4]
                CIRCLEListCoordinateY = CIRCLEListY[4]
                current_board[4] = "O"
            elif space == "F":
                CIRCLEListCoordinateX = CIRCLEListX[5]
                CIRCLEListCoordinateY = CIRCLEListY[5]
                current_board[5] = "O"
            elif space == "G":
                CIRCLEListCoordinateX = CIRCLEListX[6]
                CIRCLEListCoordinateY = CIRCLEListY[6]
                current_board[6] = "O"
            elif space == "H":
                CIRCLEListCoordinateX = CIRCLEListX[7]
                CIRCLEListCoordinateY = CIRCLEListY[7]
                current_board[7] = "O"
            elif space == "I":
                CIRCLEListCoordinateX = CIRCLEListX[8]
                CIRCLEListCoordinateY = CIRCLEListY[8]
                current_board[8] = "O"
            else:
                print(space)
                print("Invalid space!")
                continue
            drawO(CIRCLEListCoordinateX, CIRCLEListCoordinateY)
        
        else:
            print("Invalid choice!")
            continue
        #remove chosen space from list of available spaces in comp_list
        comp_list.remove(str(space)) 
        # Call Student3's Function
        CheckWinner(current_board)
        count = count + 1


### Mia & Student 2

def humaninput(comp_list):
    #declare variable
    human_move = str()
    #condition for nested loop
    while True:
        #generate computers move for the game
        human_move = input("Please select a space to fill in this grid (A - I) ")
        if human_move in comp_list:
            return human_move
        else:
            # this will continue the loop and should
            # generate another move for the computer
            pass



### student 2

def computer(comp_list):
    #declare variable
    comp_move = str()
    import random
    #condition for nested loop
    while True:
        #generate computers move for the game
        comp_move = comp_list[random.randint(0,(len(comp_list) - 1))]
        if comp_move in comp_list:
            return comp_move
        else:
            # this will continue the loop and should
            # generate another move for the computer
            pass



### Student 3
        
# Call CheckWinner() after every turn (checks every combo of 3 in a row)
def CheckWinner(current_board):
    #declare variable
    winner = str()
    #check for 3 X's in a row
    if ((current_board[0] == "X" and current_board[3] == "X" and current_board[6] == "X")
            or (current_board[1] == "X" and current_board[4] == "X" and current_board[7] == "X")
            or (current_board[2] == "X" and current_board[5] == "X" and current_board[8] == "X")
            or (current_board[0] == "X" and current_board[1] == "X" and current_board[2] == "X")
            or (current_board[3] == "X" and current_board[4] == "X" and current_board[5] == "X")
            or (current_board[6] == "X" and current_board[7] == "X" and current_board[8] == "X")
            or (current_board[0] == "X" and current_board[4] == "X" and current_board[8] == "X")
            or (current_board[2] == "X" and current_board[4] == "X" and current_board[6] == "X")):
        winner = "X"
    #check for 3 O's in a row
    elif ((current_board[0] == "O" and current_board[3] == "O" and current_board[6] == "O")
            or (current_board[1] == "O" and current_board[4] == "O" and current_board[7] == "O")
            or (current_board[2] == "O" and current_board[5] == "O" and current_board[8] == "O")
            or (current_board[0] == "O" and current_board[1] == "O" and current_board[2] == "O")
            or (current_board[3] == "O" and current_board[4] == "O" and current_board[5] == "O")
            or (current_board[6] == "O" and current_board[7] == "O" and current_board[8] == "O")
            or (current_board[0] == "O" and current_board[4] == "O" and current_board[8] == "O")
            or (current_board[2] == "O" and current_board[4] == "O" and current_board[6] == "O")):
        winner = "O"
    else:
        winner = "None"
    #if winner is found, print winner and end game
    if winner != "None":
        PrintWinner(winner)

# Print winner
def PrintWinner(winner):
    #declare variable
    play_again = str()
    #print results
    print(winner, " Wins")
    turtle.penup() 
    turtle.goto(0,0) 
    turtle.pendown() 
    turtle.color('green')
    turtle.write(str(winner)+" Wins!",align='center', font=("Arial", 36, "normal"))
    # Ask user if they want to play again or end the game
    while True:
        play_again = input("Enter Q to quit. Enter P to play again. ")
        if play_again == "Q":
            quit()
        elif play_again == "P":
            turtle.clear()
            main()



main()




