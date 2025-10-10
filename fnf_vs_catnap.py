from kandinsky import *
from kandinsky import fill_rect
from fnf_images import *
from ion import *
from ion import keydown as kd
from time import *

def display_image(image_mat, x, y, target_w):
    h = len(image_mat)
    w = len(image_mat[0])

    # Facteurs d'échelle pour chaque "pixel"
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
   while True:
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
        fill_rect(0, 0, 330, 330, 'white')
        display_image(rapperroo_image, x, y, w)
        sleep(0.1)
