import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2
import string
np.set_printoptions(linewidth=10000)
np.set_printoptions(threshold=np.inf)

def pil2cv(imgCV):
    ''' PIL型 -> OpenCV型 '''
    new_image = np.array(imgCV, dtype=np.uint8)
    return new_image

def noudo(asset):
    img = Image.new("L", (30, 50), "black")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("consola.ttf", 50)
    draw.text((0, 0), asset, "white", font=font)
    cv2img = pil2cv(img)
    a, cv2img = cv2.threshold(cv2img, 100, 255, cv2.THRESH_BINARY)
    return np.count_nonzero(cv2img)

word = [i for i in string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation]
result = {}
for i in word:
    n = noudo(i)
    result[i] = n

sorted = sorted(result.items(), key=lambda x:x[1])
l = [i[0] for i in sorted]
print(l, len(l))