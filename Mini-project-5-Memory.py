# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global state, turns, num, clicked, current
    current = []
    num = range(8) + range(8)
    clicked = [False] * 16
    random.shuffle(num)
    state = turns = 0
    label.set_text("Turns = " + str(turns))
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turns, current, label
    
    mypos = pos[0]//50
    
    if clicked[mypos]:
        return
    
    if state == 0:
        state = 1
        current.append(mypos)
    elif state == 1:
        state = 2
        turns += 1
        current.append(mypos)
    else:
        state = 1
        if (num[current[0]] != num[current[1]]):
            clicked[current[0]] = clicked[current[1]] = False
        current = [mypos]
    
    clicked[mypos] = True
    label.set_text("Turns = " + str(turns))

# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if clicked[i]:
            canvas.draw_text(str(num[i]), (i*50+18, 60), 30, 'White')
        else:
            canvas.draw_line([i*50+25, 0], [i*50+25, 100], 50, 'Green')
    for i in range(50, 800, 50):
        canvas.draw_line([i, 0], [i, 100], 2, 'Black')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric