# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PAD_VEL = 5
THR = HALF_PAD_HEIGHT + BALL_RADIUS - 8

direction = RIGHT
paddle1_pos = paddle2_pos = HEIGHT / 2
paddle1_vel = paddle2_vel = 0
# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

#Button handler
def button_handler():
    new_game()

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[1] = -random.randrange(1, 3)
    if (direction == RIGHT):
        ball_vel[0] = random.randrange(2, 4)
    else:
        ball_vel[0] = -random.randrange(2, 4)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = score2 = 0
    paddle1_pos = paddle2_pos = HEIGHT / 2
    paddle1_vel = paddle2_vel = 0
    spawn_ball(direction)
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, direction
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if (ball_pos[0] + ball_vel[0] > BALL_RADIUS + HALF_PAD_WIDTH and ball_pos[0] + ball_vel[0] < WIDTH - BALL_RADIUS - HALF_PAD_WIDTH):
        ball_pos[0] += ball_vel[0]
    else:
        if (direction == LEFT):
            direction = RIGHT
            if (ball_pos[1] > paddle1_pos - THR and ball_pos[1] < paddle1_pos + THR):
                ball_vel[0] = -ball_vel[0]
                ball_vel[0] *= 1.1
            else:
                score2 += 1
                spawn_ball(direction)
        elif (direction == RIGHT):
            direction = LEFT
            if (ball_pos[1] > paddle2_pos - THR and ball_pos[1] < paddle2_pos + THR):
                ball_vel[0] = -ball_vel[0]
                ball_vel[0] *= 1.1
            else:
                score1 += 1
                spawn_ball(direction)
    
    if (ball_pos[1] + ball_vel[1] < HEIGHT - BALL_RADIUS and ball_pos[1] + ball_vel[1] > BALL_RADIUS):
        ball_pos[1] += ball_vel[1]
    else:
        ball_vel[1] = -ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT ):
        paddle1_pos += paddle1_vel
    if (paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT ):
        paddle2_pos += paddle2_vel
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    # draw scores
    canvas.draw_text(str(score1), [250, 50], 20, 'White')
    canvas.draw_text(str(score2), [350, 50], 20, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP["up"]):
        paddle2_vel = -5
    elif (key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 5
    elif (key == simplegui.KEY_MAP["w"]):
        paddle1_vel = -5
    elif (key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 5

def keyup(key):
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0
    elif (key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', button_handler)


# start frame
new_game()
frame.start()
