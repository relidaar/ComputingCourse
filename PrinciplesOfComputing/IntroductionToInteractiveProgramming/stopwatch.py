# template for "Stopwatch: The Game"

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
WIDTH = 200
HEIGHT = 200
BUTTON_SIZE = 100
INTERVAL = 100

time = 0

stops = 0
sstops = 0

running = True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = t % 10
    t = t / 10

    A = 0
    BC = 0
    while (t > 59):
        A += 1
        t -= 60
    BC = int(t)

    return '%d:%02d.%d' % (A, BC, D,)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True


def stop():
    global stops, sstops, running

    if running:
        stops += 1
        if time % 10 == 0:
            sstops += 1

    timer.stop()
    running = False


def reset():
    global time, stops, sstops, running

    timer.stop()
    running = False

    time = 0
    stops = 0
    sstops = 0


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1


# define draw handler
def draw(canvas):
    size = 32
    canvas.draw_text('%d/%d' % (sstops, stops), (WIDTH - size * 2, size), size, 'white')
    canvas.draw_text(format(time), (WIDTH / 2 - size, HEIGHT / 2), size, 'white')


# create frame
frame = simplegui.create_frame('Stopwatch', WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button('Start', start, BUTTON_SIZE)
frame.add_button('Stop', stop, BUTTON_SIZE)
frame.add_button('Reset', reset, BUTTON_SIZE)

timer = simplegui.create_timer(INTERVAL, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
