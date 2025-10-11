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
        for i, pixel in enumerate(row):
            if pixel == -1:
                continue
            r, g, b = pixel
            fill_rect(
                int(x + i * scale_x),
                int(y + j * scale_y),
                max(1, int(scale_x)),
                max(1, int(scale_y)),
                color(r, g, b)
            )

if __name__ == "__main__":

    arrow_y1 = []
    speed = 20
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

    catnap_pose = c_idle

    while True:
        s = monotonic()
        x = 180
        y = 100
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
            fill_rect(0, 0, 330, 330, 'white')

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
        display_image(catnap_pose,30,y,w)

        display_image(a_g_left, 40, 30, 20)
        display_image(a_g_down, 60, 30, 20)
        display_image(a_g_up, 80, 30, 20)
        display_image(a_g_right, 100, 30, 20)

        #notes player 1
        for index, note_y in enumerate(arrow_y1):
            arrow_y1[index] -= speed
            arrow_image = None
            note_x = None
            if note_y <= 240 and note_y >= 0:
                if soporific_player1[index][1] == 0 or soporific_player1[index][1] == 4:
                    arrow_image = a_c_left
                    note_x = 170
                elif soporific_player1[index][1] == 1 or soporific_player1[index][1] == 5:
                    arrow_image = a_c_down
                    note_x = 190
                elif soporific_player1[index][1] == 2 or soporific_player1[index][1] == 6:
                    arrow_image = a_c_up
                    note_x = 210
                elif soporific_player1[index][1] == 3 or soporific_player1[index][1] == 7:
                    arrow_image = a_c_right
                    note_x = 230


            if not arrow_image == None:
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
                display_image(arrow_image,note_x,note_y,20) #

            if note_y <= 30 and note_y >= -30 and pose is not None:
                catnap_pose = pose



        turn += 1
        if turn == 1:
            turn = 0
        delta = monotonic()-s
        if not delta > 0.05:
            sleep(0.05-delta)
