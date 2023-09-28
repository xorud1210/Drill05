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
    global frame, x_cha, y_cha, x_hand, y_hand
    x1, y1 = x_cha, y_cha       # 시작점
    x2, y2 = x_hand, y_hand     # 도착점

    # 캐릭터 이동하면서 그려주기
    for i in range(0, 100, 1):
        t = i / 100

        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2

        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(x_hand, y_hand)
        if(x_cha < x_hand):         # 오른쪽으로 갈때
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:                       # 왼쪽으로 갈때
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)

    # 이동 후에 캐릭터 좌표 변경
    x_cha, y_cha = x_hand, y_hand


running = True
x_cha, y_cha = TUK_WIDTH // 2, TUK_HEIGHT // 2
x_hand, y_hand = random.randint(0,TUK_WIDTH),random.randint(0,TUK_HEIGHT)

frame = 0
hide_cursor()

while running:
    teleport_hand()
    move_character()
    handle_events()

close_canvas()




