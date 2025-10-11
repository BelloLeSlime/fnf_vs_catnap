from kandinsky import *
from fnf_data import *
from fnf_images import *
from ion import *
from ion import keydown as kd
from time import *

def display_image(image_mat, x, y, target_w):
    h = len(image_mat)
    w = len(image_mat[0])

    ratio = target_w / w
    scale_x = scale_y = ratio

    for j, row in enumerate(image_mat):
        current_color = None
        run_start = None
        run_length = 0

        for i, pixel in enumerate(row + [[-1, -1, -1]]):  # pixel "sentinelle" à la fin
            if pixel == -1:
                # transparent : on flush si on a un run en cours
                if current_color is not None:
                    r, g, b = current_color
                    fill_rect(
                        int(x + run_start * scale_x),
                        int(y + j * scale_y),
                        max(1, int(run_length * scale_x)),
                        max(1, int(scale_y)),
                        color(r, g, b)
                    )
                    current_color = None
                    run_length = 0
                continue

            if current_color is None:
                # premier pixel de la série
                current_color = pixel
                run_start = i
                run_length = 1
            elif pixel == current_color:
                # même couleur → on allonge la série
                run_length += 1
            else:
                # couleur différente → on dessine la série précédente
                r, g, b = current_color
                fill_rect(
                    int(x + run_start * scale_x),
                    int(y + j * scale_y),
                    max(1, int(run_length * scale_x)),
                    max(1, int(scale_y)),
                    color(r, g, b)
                )
                current_color = pixel
                run_start = i
                run_length = 1

keys = [KEY_LEFT, KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_OK]
prev_keys = [False] * len(keys)

def get_key_just_pressed():
    global prev_keys
    just_pressed = [False] * len(keys)

    for i, key in enumerate(keys):
        pressed = keydown(key)
        # vient d'être pressée si elle est maintenant True mais pas avant
        if pressed and not prev_keys[i]:
            just_pressed[i] = True
        prev_keys[i] = pressed  # met à jour l’état précédent

    return just_pressed

def game():
    arrow_y1 = []
    speed = 15
    for note in soporific_player1:
        y_value = note[0]
        y_value = (y_value / 50) * speed
        arrow_y1.append(y_value)

    arrow_y2 = []
    for note in soporific_player2:
        y_value = note[0]
        y_value = (y_value / 50) * speed
        arrow_y2.append(y_value)

    turn = 0
    win = 50

    catnap_pose = c_idle
    catnap_cooldown = 0
    last_catnap_pose = c_idle

    while True:
        s = monotonic()
        x = 180
        y = 130
        w = 60
        if kd(KEY_DOWN):
           rapperroo_image = r_down
        elif kd(KEY_UP):
            rapperroo_image = r_up
        elif kd(KEY_LEFT):
            rapperroo_image = r_left
        elif kd(KEY_RIGHT):
            rapperroo_image = r_right
        else:
            rapperroo_image = r_idle
        if turn == 0:
            display_image(bg_soporific,0,0,320)

        if kd(KEY_LEFT):
            display_image(a_c_left, 170, 30, 20)
        else:
            display_image(a_g_left,170,30,20)
        if kd(KEY_DOWN):
            display_image(a_c_down, 190, 30, 20)
        else:
            display_image(a_g_down,190,30,20)
        if kd(KEY_UP):
            display_image(a_c_up, 210, 30, 20)
        else:
            display_image(a_g_up, 210, 30, 20)
        if kd(KEY_RIGHT):
            display_image(a_c_right, 230, 30, 20)
        else:
            display_image(a_g_right, 230, 30, 20)

        display_image(rapperroo_image, x, y, w)
        display_image(catnap_pose,50,y,w)

        display_image(a_g_left, 40, 30, 20)
        display_image(a_g_down, 60, 30, 20)
        display_image(a_g_up, 80, 30, 20)
        display_image(a_g_right, 100, 30, 20)

        fill_rect(80,200,160,9,'black')

        win_x = int((win /100) * 156)
        lose_x = int(((100 - win) / 100) * 156)

        fill_rect(82,202,lose_x,5,'purple')
        fill_rect(238-win_x,202,win_x,5,'cyan')

        if win >= 80:
            display_image(c_icon_alt,238-win_x-11,199,10)
        else:
            display_image(c_icon,238-win_x-11,199,10)
        if win <= 20:
            display_image(r_icon_alt,238-win_x+1,199,10)
        else:
            display_image(r_icon,238-win_x+1,199,10)

        jp = get_key_just_pressed()

        #notes player 1
        for index, note_y in enumerate(arrow_y1):
            arrow_y1[index] -= speed
            arrow_image = None
            note_x = None
            note_direction = None
            note_visible = True



            if note_y <= 240 and note_y >= -20:
                if soporific_player1[index][1] == 0 or soporific_player1[index][1] == 4:
                    arrow_image = a_c_left
                    note_x = 170
                    note_direction = "left"
                elif soporific_player1[index][1] == 1 or soporific_player1[index][1] == 5:
                    arrow_image = a_c_down
                    note_x = 190
                    note_direction = "down"
                elif soporific_player1[index][1] == 2 or soporific_player1[index][1] == 6:
                    arrow_image = a_c_up
                    note_x = 210
                    note_direction = "up"
                elif soporific_player1[index][1] == 3 or soporific_player1[index][1] == 7:
                    arrow_image = a_c_right
                    note_x = 230
                    note_direction = "right"

            if note_y <= 60 and note_y >= 0:
                if note_direction == "left" and jp[0]:
                    note_visible = False
                    arrow_y1[index] = -20
                    win += 3
                elif note_direction == "down" and jp[1]:
                    note_visible = False
                    arrow_y1[index] = -20
                    win += 3
                elif note_direction == "up" and jp[2]:
                    note_visible = False
                    arrow_y1[index] = -20
                    win += 3
                elif note_direction == "right" and jp[3]:
                    note_visible = False
                    arrow_y1[index] = -20
                    win += 3

            if note_y <= 0 and note_y >= 0 - int(speed / 2):
                win -= 5

            if win <= 0:
                return

            if win > 100:
                win = 100



            if (not arrow_image == None) and note_visible:
                display_image(arrow_image,note_x,note_y,20)

        catnap_pose = c_idle
        pose = None

        #notes player 2
        for index, note_y in enumerate(arrow_y2):
            arrow_y2[index] -= speed
            note_y -= speed
            arrow_image = None
            note_x = None
            if note_y <= 240 and note_y >= -30:
                if soporific_player2[index][1] == 0 or soporific_player2[index][1] == 4:
                    arrow_image = a_c_left
                    note_x = 40
                    pose = c_left
                elif soporific_player2[index][1] == 1 or soporific_player2[index][1] == 5:
                    arrow_image = a_c_down
                    note_x = 60
                    pose = c_down
                elif soporific_player2[index][1] == 2 or soporific_player2[index][1] == 6:
                    arrow_image = a_c_up
                    note_x = 80
                    pose = c_up
                elif soporific_player2[index][1] == 3 or soporific_player2[index][1] == 7:
                    arrow_image = a_c_right
                    note_x = 100
                    pose = c_right


            if arrow_image is not None and note_y >= 30:
                display_image(arrow_image,note_x,note_y,20)

            if note_y <= 30 and note_y >= 30 - int(speed/2):
                win -=2
                if win <= 1:
                    win = 1

            if note_y <= 30 and note_y >= -30:
                if catnap_cooldown ==0:
                    catnap_pose = pose
                    last_catnap_pose = catnap_pose
                    catnap_cooldown = 5
                else:
                    catnap_pose = last_catnap_pose

            catnap_cooldown -= 1
            if catnap_cooldown <= 0:
                catnap_cooldown = 0

        display_image(fg_soporific,0,0,320)

        turn += 1
        if turn == 1:
            turn = 0
        delta = monotonic()-s
        if not delta > 0.05:
            sleep(0.05-delta)

def menu(menu_name = "main"):
    menu = menu_name
    display_image(bg_m_menu,0,0,320)
    draw_string("Press OK to start",10,140,'white','black')
    index_cursor = 0
    menu_button = [
        [
            "Story mode",
            "Freeplay",
            "Credits",
            "Options"
        ],
        [
            "Soporific",
            "Sour Nightmares",
            "Insomniac",
            "Doggone happy",
            "Joy hour",
            "Bootleg",
            "Melatonin",
            "Reject",
            "Control"
        ]
    ]
    while True:
        s = monotonic()
        jp = get_key_just_pressed()
        if menu == "main":
            if jp[4]:
                menu = "mode"
        elif menu == "mode":
            display_image(bg_menu,0,0,320)
            if jp[1]:
                index_cursor += 1
            if jp[2]:
                index_cursor -= 1
            if index_cursor > 3:
                index_cursor = 3
            if index_cursor < 0:
                index_cursor = 0

            for i in range(-3,3):
                if i + index_cursor >= 0 and i + index_cursor <= 3:
                    if i == 0:
                        draw_string(menu_button[0][i + index_cursor],50,30 * i + 100,'yellow',color(72,37,134))
                    else:
                        draw_string(menu_button[0][i + index_cursor], 50, 30 * i + 100, 'white', color(72, 37, 134))

            if jp[4]:
                if index_cursor == 1:
                    index_cursor = 0
                    menu = "freeplay"

        elif menu == "freeplay":
            display_image(bg_menu, 0, 0, 320)
            if jp[1]:
                index_cursor += 1
            if jp[2]:
                index_cursor -= 1
            if index_cursor > 8:
                index_cursor = 8
            if index_cursor < 0:
                index_cursor = 0

            for i in range(-8, 8):
                if i + index_cursor >= 0 and i + index_cursor <= 8:
                    if i == 0:
                        draw_string(menu_button[1][i + index_cursor], 50, 30 * i + 100, 'yellow', color(72, 37, 134))
                    else:
                        draw_string(menu_button[1][i + index_cursor], 50, 30 * i + 100, 'white', color(72, 37, 134))

            if jp[4]:
                if index_cursor == 0:
                    game()

        delta = monotonic() - s
        if delta < 0.05:
            sleep(0.05-delta)







menu("main")