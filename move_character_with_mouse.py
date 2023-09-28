import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def teleport_hand():
    global x_hand, y_hand
    x_hand, y_hand = random.randint(0,TUK_WIDTH),random.randint(0,TUK_HEIGHT)

def move_character():
    pass


running = True
x_cha, y_cha = TUK_WIDTH // 2, TUK_HEIGHT // 2
x_hand, y_hand = random.randint(0,TUK_WIDTH),random.randint(0,TUK_HEIGHT)

frame = 0
hide_cursor()

while running:
    teleport_hand()
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(x_hand, y_hand)
    update_canvas()
    delay(0.1)
    #move_character()
    handle_events()

close_canvas()




