import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    global x_cha, y_cha
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x_cha, y_cha = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def teleport_hand():
    print('손가락 이동')
    pass
    #global x_hand, y_hand

def move_character():
    print('캐릭터 이동')
    pass


running = True
x_cha, y_cha = TUK_WIDTH // 2, TUK_HEIGHT // 2
x_hand, y_hand = random.randint(0,TUK_WIDTH),random.randint(0,TUK_HEIGHT)

frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(x_hand,y_hand)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x_cha, y_cha)
    update_canvas()
    move_character()
    teleport_hand()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




