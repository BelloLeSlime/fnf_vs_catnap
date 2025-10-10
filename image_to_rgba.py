from PIL import Image
import numpy as np

def image_to_rgba_matrix(path, target_width=None, ratio=None, alpha_threshold=0):
    """
    Convertit une image en une matrice [[(r,g,b), ...], ...]
    avec -1 pour les pixels transparents.
    """
    # Ouvre et convertit en RGBA
    img = Image.open(path).convert("RGBA")

    # Redimensionnement
    if target_width is not None:
        ratio = target_width / img.width
    elif ratio is None:
        ratio = 1.0

    if ratio != 1.0:
        new_w = int(img.width * ratio)
        new_h = int(img.height * ratio)
        img = img.resize((new_w, new_h), Image.LANCZOS)

    # Conversion en matrice numpy
    arr = np.array(img)  # (h, w, 4)

    # Transformation : RGBA → (r,g,b) ou -1
    matrix = []
    for y in range(arr.shape[0]):
        row = []
        for x in range(arr.shape[1]):
            r, g, b, a = arr[y, x]
            if a <= alpha_threshold:
                row.append(-1)
            else:
                row.append([int(r), int(g), int(b)])
        matrix.append(row)

    return matrix

def save_matrix_to_txt(matrix, output_path="output.txt"):
    with open(output_path, "w", encoding="utf-8") as f:
        for row in matrix:
            f.write(str(row) + ",\n")
    print(f"Matrice sauvegardée dans {output_path}")

if __name__ == "__main__":
    image = input("Image avec extension : ")
    image_path = "images/" + image
    target_width = input("Target width : ")
    if target_width != "":
        target_width = int(target_width)
    else:
        target_width = None
    mat = image_to_rgba_matrix(image_path, target_width, 99)
    save_matrix_to_txt(mat, "output.txt")
