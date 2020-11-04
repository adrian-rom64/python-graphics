from PIL import Image, ImageOps  # Python Imaging Library
import numpy as np
from PIL import ImageChops


#im = Image.open('jesien1.jpg')
im = Image.open('jesien2.jpg')
#im = Image.open('RGB.jpg')
h, w = im.size
im.show()

# Kanały pobrane jako obrazy
r, g, b = im.split()  # powstają obrazy
r.show()
g.show()
b.show()
# zapis kanałów do tablic
r_T = np.array(r)
g_T = np.array(g)
b_T = np.array(b)

input()
# tablica obrazu
T = np.array(im)
# tablica kanału r
t_r = T[:, :, 0]
im_r = Image.fromarray(t_r)
# tablica kanału g
t_g = T[:, :, 1]
im_g = Image.fromarray(t_g)
# tablica kanału b
t_b = T[:, :, 2]
im_b = Image.fromarray(t_b)

im_r.show()
im_g.show()
im_b.show()
input()

diff_r = ImageChops.difference(r, im_r)
diff_r.show()
input()

szum = Image.open('szum.jpg')
szum.show()
diff_szum = ImageChops.difference(im, szum)
diff_szum.show()
input()

im1 = Image.merge('RGB', (im_r, im_g, im_b))
im2 = Image.merge('RGB', (r, g, b))  # zamień r na im_r i sprawdź efekt
im1.show()
im2.show()
diff_im = ImageChops.difference(im1, im2)
input()

im3 = Image.merge('RGB', (r, b, g))
im3.show()

input()

# tworzenie obrazu w odcieniach szarości
w1 = 0.3
w2 = 0.8
w3 = 0.2
szary = w1 * r_T + w2 * g_T + w3 * b_T
szary_im = Image.fromarray(szary)
szary_im.show()
input()

# tworzenie własnej tablicy
t = (w, h)
A = np.zeros(t, dtype=np.uint8)
A_im = Image.fromarray(A)

im4 = Image.merge('RGB', (r, A_im, b))
im4.show()
input()

# tablica obrazu w odcieniach szarosci
B = np.ones(t, dtype=np.uint8)
for i in range(w):
    for j in range(h):
        B[i, j] = (i + j) % 256
# zapis tablicy do obrazu
B_im = Image.fromarray(B)
B_im.show()
im6 = Image.merge('RGB', (B_im, g, b))
im6.show()
