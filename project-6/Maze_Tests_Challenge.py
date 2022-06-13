def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
    # if wall_on_right() != True and front_is_clear() != True:
    # turn_right()
turn_left() #commented code also works - replacing turn_left()

while at_goal() != True:
    if wall_on_right() == True:
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
    else:
        turn_right()
        move()