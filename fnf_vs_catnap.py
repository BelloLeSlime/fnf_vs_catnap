from kandinsky import *
from fnf_data import *
from fnf_images import *
from ion import *
from ion import keydown as kd
from time import *
from random import randint

def display_image(image_mat, x, y, target_w, x_off=0, y_off=0, w_off=None, h_off=None):
    """
    Affiche l'image image_mat à (x, y) avec largeur cible target_w,
    mais ne dessine que la partie qui se trouve à l'intérieur de la zone visible
    du canvas définie par (x_off, y_off, w_off, h_off).
    """

    h = len(image_mat)
    w = len(image_mat[0])
    ratio = target_w / w
    scale_x = scale_y = ratio

    # Par défaut, la zone visible = tout l’écran
    if w_off is None:
        w_off = 320
    if h_off is None:
        h_off = 240

    # Limites visibles dans les coordonnées écran
    x_min = x_off
    y_min = y_off
    x_max = x_off + w_off
    y_max = y_off + h_off

    for j, row in enumerate(image_mat):
        # coordonnée Y réelle sur le canvas
        screen_y = int(y + j * scale_y)
        next_y = screen_y + int(scale_y)

        # Ignore si la ligne est hors de la zone visible
        if next_y < y_min or screen_y > y_max:
            continue

        current_color = None
        run_start = None
        run_length = 0

        for i, pixel in enumerate(row + [[-1, -1, -1]]):  # pixel sentinelle
            if pixel == -1:
                if current_color is not None:
                    r, g, b = current_color
                    screen_x = int(x + run_start * scale_x)
                    next_x = screen_x + int(run_length * scale_x)

                    # On clip sur les bornes visibles
                    clip_x1 = max(screen_x, x_min)
                    clip_x2 = min(next_x, x_max)

                    if clip_x2 > clip_x1 and next_y > y_min and screen_y < y_max:
                        fill_rect(
                            clip_x1,
                            max(screen_y, y_min),
                            clip_x2 - clip_x1,
                            min(next_y, y_max) - max(screen_y, y_min),
                            color(r, g, b)
                        )

                    current_color = None
                    run_length = 0
                continue

            if current_color is None:
                current_color = pixel
                run_start = i
                run_length = 1
            elif pixel == current_color:
                run_length += 1
            else:
                r, g, b = current_color
                screen_x = int(x + run_start * scale_x)
                next_x = screen_x + int(run_length * scale_x)

                clip_x1 = max(screen_x, x_min)
                clip_x2 = min(next_x, x_max)

                if clip_x2 > clip_x1 and next_y > y_min and screen_y < y_max:
                    fill_rect(
                        clip_x1,
                        max(screen_y, y_min),
                        clip_x2 - clip_x1,
                        min(next_y, y_max) - max(screen_y, y_min),
                        color(int(r), int(g), int(b))
                    )

                current_color = pixel
                run_start = i
                run_length = 1

keys = [KEY_LEFT, KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_OK, KEY_BACKSPACE]
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

last_noise_pixels = []

def apply_noise(intensity=200, strength=25):
    """
    Applique un effet de bruit temporaire :
    - bg et fg : fonctions lambda pour redessiner un pixel du background et du foreground
    - intensity : nombre de pixels affectés
    - strength : intensité de la variation
    """

    global last_noise_pixels

    for (x, y) in last_noise_pixels:
        # On redessine le pixel original du bg et du fg (superposition)
        display_image(bg_soporific,0,0,320,x,y,10,1)
        display_image(fg_soporific, 0, 0, 320, x, y, 10, 1)

    last_noise_pixels = []

    for _ in range(intensity):
        x = randint(0, 319)
        y = randint(0, 239)
        for x_offset in range(10):

            r, g, b = get_pixel(x, y)
            r = max(0, min(255, r + randint(-strength, strength)))
            g = max(0, min(255, g + randint(-strength, strength)))
            b = max(0, min(255, b + randint(-strength, strength)))

            set_pixel(x + x_offset, y,color(r, g, b))

        last_noise_pixels.append((x, y))

def game():
    delta = 0.0
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
    display_image(bg_soporific, 0, 0, 320)
    display_image(fg_soporific, 0, 0, 320)

    time_ms = 0.0

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

        display_image(bg_soporific, 0, 0, 320, 170, 0, 80, 50)


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

        display_image(bg_soporific, 0, 0, 320, 180, 130, 60, 80)
        display_image(rapperroo_image, x, y, w)
        display_image(fg_soporific, 0, 0, 320, 180, 130, 60, 80)

        display_image(bg_soporific, 0, 0, 320, 50, 130, 60, 80)
        display_image(catnap_pose,50,y,w)
        display_image(fg_soporific, 0, 0, 320, 50, 130, 60, 80)

        display_image(bg_soporific, 0, 0, 320, 40, 30, 80, 60)
        display_image(a_g_left, 40, 30, 20)
        display_image(a_g_down, 60, 30, 20)
        display_image(a_g_up, 80, 30, 20)
        display_image(a_g_right, 100, 30, 20)

        display_image(bg_soporific, 0, 0, 320, 70, 198, 180, 13)
        display_image(rapperroo_image, x, y, w)
        display_image(catnap_pose, 50, y, w)
        fill_rect(80,200,160,9,'black')

        win_x = int((win /100) * 156)
        lose_x = 156-win_x

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
            previous_y = note_y

            if delta <= 0.05:
                arrow_y1[index] -= speed
                note_y -= speed
            else:
                arrow_y1[index] -= speed * (delta / 0.05)
                note_y -= speed * (delta / 0.05)

            arrow_image = None
            note_x = None
            note_direction = None
            note_visible = True

            sustain_ms = soporific_player1[index][2]

            if note_y <= 240 and note_y >= -480:
                if soporific_player1[index][1] == 0 or soporific_player1[index][1] == 4:
                    arrow_image = a_c_left
                    note_x = 170
                    note_direction = "left"
                    note_color = color(187, 100, 134)
                elif soporific_player1[index][1] == 1 or soporific_player1[index][1] == 5:
                    arrow_image = a_c_down
                    note_x = 190
                    note_direction = "down"
                    note_color = color(104, 187, 195)
                elif soporific_player1[index][1] == 2 or soporific_player1[index][1] == 6:
                    arrow_image = a_c_up
                    note_x = 210
                    note_direction = "up"
                    note_color = color(149, 182, 103)
                elif soporific_player1[index][1] == 3 or soporific_player1[index][1] == 7:
                    arrow_image = a_c_right
                    note_x = 230
                    note_direction = "right"
                    note_color = color(214, 83, 83)

            if 0 <= note_y <= 60:
                if (note_direction == "left" and jp[0]) or (note_direction == "down" and jp[1]) or (note_direction == "up" and jp[2]) or (note_direction == "right" and jp[3]):
                    note_visible = False
                    arrow_y1[index] = -20
                    win += 3
                    display_image(bg_soporific, 0, 0, 320, note_x, int(previous_y), 20, 20)
                    display_image(bg_soporific, 0, 0, 320, note_x, int(note_y), 20, 20)
                    if sustain_ms > 0:
                        sustain_height = int((sustain_ms / 50) * speed)
                        display_image(bg_soporific, 0, 0, 320, note_x + 5, int(previous_y), 10, 240)
                        display_image(bg_soporific, 0, 0, 320, note_x + 5, int(note_y), 10, 240)
                        display_image(fg_soporific, 0, 0, 320, note_x + 5, int(previous_y), 10, sustain_height)
                        display_image(fg_soporific, 0, 0, 320, note_x + 5, int(note_y), 10, sustain_height)



            if note_y <= 0 and note_y >= 0 - int(speed / 2) * int(delta / 0.05):
                win -= 5
                note_visible = False
                display_image(bg_soporific, 0, 0, 320, note_x, int(previous_y), 20, 20)
                display_image(bg_soporific, 0, 0, 320, note_x, int(note_y), 20, 20)
                if sustain_ms > 0:
                    sustain_height = int((sustain_ms / 50) * speed)
                    display_image(bg_soporific, 0, 0, 320, note_x + 5, int(previous_y), 10, sustain_height)
                    display_image(bg_soporific, 0, 0, 320, note_x + 5, int(note_y), 10, sustain_height)
                    display_image(fg_soporific, 0, 0, 320, note_x + 5, int(previous_y), 10, sustain_height)
                    display_image(fg_soporific, 0, 0, 320, note_x + 5, int(note_y), 10, sustain_height)

            if win <= 0:
                return

            if win > 100:
                win = 100

            if (sustain_ms > 0) and (note_x is not None) and note_visible:
                sustain_height = int((sustain_ms / 50) * speed)
                display_image(bg_soporific, 0, 0, 320, note_x + 5, int(previous_y), 10, sustain_height)
                display_image(bg_soporific, 0, 0, 320, note_x + 5, int(note_y), 10, sustain_height)
                display_image(fg_soporific, 0, 0, 320, note_x + 5, int(previous_y), 10, sustain_height)
                display_image(fg_soporific, 0, 0, 320, note_x + 5, int(note_y), 10, sustain_height)
                fill_rect(note_x + 5, int(note_y), 10, sustain_height, note_color)
                display_image(bg_soporific, 0, 0, 320, 170, 0, 80, 30)

            if (not arrow_image == None) and note_visible:
                display_image(bg_soporific, 0, 0, 320, note_x, int(previous_y), 20, 20)
                display_image(fg_soporific, 0, 0, 320, note_x, int(previous_y), 20, 20)
                display_image(arrow_image,note_x,note_y,20)


        catnap_pose = c_idle
        pose = None

        #notes player 2
        for index, note_y in enumerate(arrow_y2):
            previous_y = note_y

            if delta <= 0.05:
                arrow_y2[index] -= speed
                note_y -= speed
            else:
                arrow_y2[index] -= speed * (delta / 0.05)
                note_y -= speed * (delta / 0.05)


            arrow_image = None
            note_x = None
            if note_y <= 240 and note_y >= -30:
                if soporific_player2[index][1] == 0 or soporific_player2[index][1] == 4:
                    arrow_image = a_c_left
                    note_x = 40
                    pose = c_left
                    note_color = color(187,100,134)
                elif soporific_player2[index][1] == 1 or soporific_player2[index][1] == 5:
                    arrow_image = a_c_down
                    note_x = 60
                    pose = c_down
                    note_color = color(104,187,195)
                elif soporific_player2[index][1] == 2 or soporific_player2[index][1] == 6:
                    arrow_image = a_c_up
                    note_x = 80
                    pose = c_up
                    note_color = color(149,182,103)
                elif soporific_player2[index][1] == 3 or soporific_player2[index][1] == 7:
                    arrow_image = a_c_right
                    note_x = 100
                    pose = c_right
                    note_color = color(214,83,83)


            if arrow_image is not None and note_y >= 30 and note_x is not None:
                display_image(bg_soporific, 0, 0, 320, note_x, int(previous_y), 20, 20)
                display_image(fg_soporific, 0, 0, 320, note_x, int(previous_y), 20, 20)
                display_image(arrow_image,note_x,note_y,20)

            if note_y <= 10 and previous_y >= 10 and note_x is not None:

                display_image(bg_soporific, 0, 0, 320, note_x, int(previous_y), 20, 20)

                if delta <= 0.05:
                    previous_y += speed
                else:
                    previous_y += speed * (delta / 0.05)

                display_image(bg_soporific, 0, 0, 320, note_x, int(previous_y), 20, 20)
                display_image(bg_soporific, 0, 0, 320, note_x, int(note_y), 20, 20)
                display_image(bg_soporific, 0, 0, 320, note_x + 5, 0, 10, 240)
                display_image(fg_soporific, 0, 0, 320, note_x + 5, 0, 10, 240)
                win -=2
                if win <= 1:
                    win = 1

            if note_y <= 30 and note_y >= -30:
                if catnap_cooldown ==0 or pose is not None:
                    catnap_pose = pose
                    last_catnap_pose = catnap_pose
                    catnap_cooldown = 10
                else:
                    catnap_pose = last_catnap_pose

            catnap_cooldown -= 1
            if catnap_cooldown <= 0:
                catnap_cooldown = 0

        #apply_noise(50,10)


        delta = monotonic()-s
        if not delta > 0.05:
            sleep(0.05-delta)
            fps = int(1/0.05)
            time_ms += 50
        else:
            fps = int(1/delta)
            time_ms += int(delta * 1000)

        draw_string("FPS : " + f"{fps:02}", 0, 0, 'white', 'black')

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
            display_image(bg_menu,-20,0 - (index_cursor * 5),360)
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
            display_image(bg_menu, -20, 0 - (index_cursor * 5), 360)
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
            if jp[5]:
                index_cursor = 0
                menu = "mode"

        delta = monotonic() - s
        if delta < 0.05:
            sleep(0.05-delta)








menu("main")
display_image(bg_soporific, 0, 0, 320, 5, 53, 10, 134)