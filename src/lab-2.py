from PIL import Image
import numpy as np

# zd 1
image = Image.open('results/lab-2/input.png')

# zd 2
print("typ", image.mode)
print("format", image.format)
print("format z opisem", image.format_description)
print("rozmiar", image.size)

# zd 3
image.save('results/lab-2/result.jpg', 'JPEG')
jpg_image = Image.open('results/lab-2/result.jpg')

print("typ", jpg_image.mode)
print("format", jpg_image.format)
print("format z opisem", jpg_image.format_description)
print("rozmiar", jpg_image.size)

# zd 4
small = image.resize((50, 50))
small.save('results/lab-2/maly.png')

print("typ", small.mode)
print("format", small.format)
print("format z opisem", small.format_description)
print("rozmiar", small.size)

# zd5
big = image.resize((500, 500))
big.save('results/lab-2/duzy.png')

print("typ", big.mode)
print("format", big.format)
print("format z opisem", big.format_description)
print("rozmiar", big.size)

# zd 7
# Moj pomysl to gradient poziomo
w, h = 500, 500
arr = np.zeros((w, h), dtype=np.uint8)
img = Image.fromarray(arr, mode='L')
for x in range(w):
    for y in range(h):
        arr[x, y] = y / 2
img.save('results/lab-2/obraz.png')

# zd 8
Image.fromarray((np.array(big) + np.array(img))).save('results/lab-2/suma.png')
Image.fromarray((np.array(big) - np.array(img))
                ).save('results/lab-2/roznica.png')
Image.fromarray((np.array(big) * np.array(img))
                ).save('results/lab-2/iloczyn.png')

# zd 9
negatyw = np.array(big)
for x in range(w):
    for y in range(h):
        negatyw[x, y] = 255 - negatyw[x, y]
Image.fromarray(negatyw).save('results/lab-2/negatyw.png')

# zd 10
Image.fromarray((np.array(big) + np.array(negatyw))
                ).save('results/lab-2/suma2.png')
Image.fromarray((np.array(big) - np.array(negatyw))
                ).save('results/lab-2/roznica2.png')
Image.fromarray((np.array(big) * np.array(negatyw))
                ).save('results/lab-2/iloczyn2.png')
