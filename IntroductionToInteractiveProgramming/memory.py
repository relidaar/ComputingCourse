# implementation of card game - Memory
import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

CAN_SIZE = (800, 100)
CARD_SIZE = (50, 100)
CARD_PAD = 1
CARD_POS = (CARD_SIZE[0] // 2, CARD_SIZE[1] - CARD_PAD)

NUM_SIZE = 40
NUM_POS = (NUM_SIZE // 2.5, NUM_SIZE * 1.5)


# helper function to initialize globals
def new_game():
    global cards, exposed, state, first, second, counter
    cards = range(0, 8) + range(0, 8)
    random.shuffle(cards)
    exposed = [False] * 16

    state = 0
    first = -1
    second = -1
    counter = 0


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, first, second, counter
    i = pos[0] // 50
    if exposed[i]:
        return

    if state == 0:
        exposed[i] = True
        first = i
        state = 1
        counter += 1
    elif state == 1:
        exposed[i] = True
        second = i
        state = 2
    else:
        if cards[first] != cards[second]:
            exposed[first] = False
            exposed[second] = False
        counter += 1
        exposed[i] = True
        first = i
        state = 1


# cards are logically 50x100 pixels in size
def draw(canvas):
    offset = 0
    label.set_text('Turns = ' + str(counter))
    for c, e in zip(cards, exposed):
        if not e:
            canvas.draw_line(
                (offset + CARD_POS[0], CARD_PAD),
                (offset + CARD_POS[0], CARD_POS[1]),
                CARD_SIZE[0] - CARD_PAD, 'green'
            )
        else:
            canvas.draw_text(str(c), (offset + NUM_POS[0], NUM_POS[1]), NUM_SIZE, 'white')

        offset += CARD_SIZE[0]


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CAN_SIZE[0], CAN_SIZE[1])
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric