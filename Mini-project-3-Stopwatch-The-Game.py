import simplegui

tick = 0
attempt = 0
success = 0
is_stop = True

def format(n):
    s = '.' + str(n % 10)
    n /= 10
    t = n % 60
    s = str(t % 10) + s
    s = str(t / 10) + s
    n /= 60
    s = str(n) + ':' + s
    return s

def start():
    timer.start()
    global is_stop
    is_stop = False
    
def stop():
    timer.stop()
    global is_stop
    global attempt
    global success
    global tick
    
    if not is_stop:
        attempt += 1
        if tick % 10 == 0:
            success += 1
        
    is_stop = True
    
def reset():
    global timer
    global tick
    global is_stop
    global attempt
    global success
    tick = 0
    timer.stop()
    attempt = 0
    success = 0
    is_stop = True
    timer = simplegui.create_timer(100, timer_handler)

def timer_handler():
    global tick
    tick += 1
    
def draw(canvas):
    canvas.draw_text(format(tick), [100,100], 48, "Red")
    canvas.draw_text(str(success) + '/' + str(attempt), [250,30], 24, "Yellow")

f = simplegui.create_frame("Stopwatch", 300, 200)
f.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)

f.add_button('Start', start, 200)
f.add_button('Stop', stop, 200)
f.add_button('Reset', reset, 200)

f.start()
