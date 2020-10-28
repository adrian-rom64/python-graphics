from PIL import Image
import numpy as np


def box_range(x, y, w, h):
    return [(j, i) for i in range(x, x + w + 1) for j in range(y, y + h + 1)]


def load_img(path):
    return np.array(Image.open(path).convert('1'))


def save_img(arr, filename):
    Image.fromarray(arr).save(f"results/lab-3/{filename}")


def draw_box(img, x, y, w, h, color):
    for (i, j) in box_range(x, y, w, h):
        img[i, j] = color


def surround_range(xp, xk, yp, yk):
    hor = [(i, j) for i in [xp - 1, xk + 1] for j in range(yp - 1, yk + 2)]
    ver = [(i, j) for j in [yp - 1, yk + 1] for i in range(xp, xk + 1)]
    return hor + ver


def draw_bounds(img, width, color):
    h = img.shape[0] - 1
    w = img.shape[1] - 1
    draw_box(img, 0, 0, w, width, color)
    draw_box(img, 0, h - width, w, width, color)
    draw_box(img, 0, 0, width, h, color)
    draw_box(img, w - width, 0, width, h, color)


def draw_squares(img, size, color):
    h = img.shape[0] - 1
    w = img.shape[1] - 1
    draw_box(img, 0, 0, size, size, color)
    draw_box(img, w - size, 0, size, size, 0)
    draw_box(img, 0, h - size, size, size, color)
    draw_box(img, w - size, h - size, size, size, color)


def negative(img):
    res = np.copy(img)
    h, w = img.shape
    for (i, j) in box_range(0, 0, w - 1, h - 1):
        res[i, j] = not res[i, j]
    return res


# zd1
pic1 = load_img('results/lab-3/pic1.bmp')
pic2 = load_img('results/lab-3/pic2.bmp')

res1 = np.copy(pic1)
res2 = np.copy(pic2)

# zd2
draw_bounds(res1, 20, 0)
draw_bounds(res2, 20, 0)

# zd3
draw_squares(res1, 50, 0)
draw_squares(res2, 50, 0)

save_img(res1, 'res1.bmp')
save_img(res2, 'res2.bmp')

# zd4
add = pic1 + pic2
mul = pic1 * pic2
neg = negative(pic1)

save_img(add, 'add.bmp')
save_img(mul, 'mul.bmp')
save_img(neg, 'neg.bmp')

# zd5
tarr = np.ones((30, 30))
h = tarr.shape[0] - 1
w = tarr.shape[1] - 1
draw_box(tarr, (int)(w / 2) - 8, (int)(h / 2) - 8, 16, 16, 255)
for k in range(5, 14):
    lt = (int)(w / 2) - k
    rt = (int)(w / 2) + k
    lb = (int)(h / 2) - k
    rb = (int)(h / 2) + k
    for (i, j) in surround_range(lt, rt, lb, rb):
        tarr[i, j] = 255 if k % 2 == 0 else 0

timg = Image.fromarray(tarr)
timg.resize((500, 500)).show()
