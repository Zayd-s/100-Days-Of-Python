def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    if front_is_clear():
        move()
    elif wall_in_front():    
        jump()

#The functions move() and turn_left().
#The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
#How to use a while loop and an if statement.
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
