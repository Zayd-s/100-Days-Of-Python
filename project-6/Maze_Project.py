def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_back():
    turn_left()
    turn_left()


while at_goal() != True:
    if wall_on_right() == True:
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
    else:
        turn_right()
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
