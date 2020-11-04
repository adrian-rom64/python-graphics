from PIL import Image, ImageChops
import numpy as np

path = 'results/lab-4'


def load_img(name):
    img = Image.open(f"{path}/{name}")
    return (img, np.array(img))


def save_img(img, name):
    if isinstance(img, np.ndarray):
        Image.fromarray(img).save(f"{path}/{name}")
    else:
        img.save(f"{path}/{name}")


# zd 1
img, arr = load_img('input.jpg')

# zd 2
t_r = arr[:, :, 0]
t_g = arr[:, :, 1]
t_b = arr[:, :, 2]

save_img(t_r, 'im_r.jpg')
save_img(t_g, 'im_g.jpg')
save_img(t_b, 'im_b.jpg')

# zd 3
i_r, i_g, i_b = img.split()

# zd4
img_4 = Image.merge('RGB', (Image.fromarray(t_r), i_g, i_b))
save_img(img_4, 'img_4.jpg')

# zd5
diff = ImageChops.difference(img, img_4)
save_img(diff, 'diff.jpg')

# zd6
wr, wg, wb = 0.3, 0.8, 0.4
r = np.array(i_r)
g = np.array(i_g)
b = np.array(i_b)
gray_values = wr * r + wg * g + wb * b
gray = Image.fromarray(gray_values)
save_img(gray.convert('RGB'), 'gray.jpg')

# zd7
img_7 = Image.merge('RGB', (gray.convert('L'), i_g, i_b))
save_img(img_7, 'img_7.jpg')

# zd8
wr, wg, wb = 0.1, 0.3, 0.4
r = np.array(i_r)
g = np.array(i_g)
b = np.array(i_b)
gray_values = wr * r + wg * g + wb * b
gray = Image.fromarray(gray_values)
save_img(gray.convert('RGB'), 'img_8.jpg')
