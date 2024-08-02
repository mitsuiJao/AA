import cv2
import numpy as np
import sys
np.set_printoptions(linewidth=500)
np.set_printoptions(threshold=np.inf)
# aaset = ['`', '.', "'", '-', ':', ',', '"', '_', '^', '~', '<', ';', '>', '!', '*', '=', '/', '\\', '+', 'L', 'r', '|', '?', 'c', ')', '(', '7', 'v', 'T', '{', 'z', 'J', ']', 's', 'i', 'x', 'Y', '}', '1', 'f', 'F', 'l', 'n', 'C', 'u', 't', 'I', '3', 'o', '2', '5', '[', 'E', 'P', 'j', 'K', 'S', 'y', 'V', 'Z', 'h', 'e', 'a', 'k', 'X', 'U', 'w', '4', 'p', 'b', '9', 'A', 'H', '6', 'm', 'D', 'd', 'G', 'O', 'q', 'R', '#', 'B', 'W', '8', '$', 'N', '%', 'M', '0', 'Q', '&', 'g', '@']
# aaset = ['.', '-', ',', '_', '~', ';', '!', '=', '\\', 'L', '|', 'c', '(', 'v', '{', 'J', 's', 'x', '}', 'f', 'l', 'C', 't', '3', '2', '[', 'P', 'K', 'y', 'Z', 'e', 'k', 'U', '4', 'b', 'A', '6', 'D', 'G', 'q', '#', 'W', '$', '%', '0', '&', '@']
# aaset = ['.', ',', '~', '!', '\\', '|', '(', '{', 's', '}', 'l', 't', '2', 'P', 'y', 'e', 'U', 'b', '6', 'G', '#', '$', '0', '@']
aaset = ['.', '~', '\\', '(', 's', 'l', '2', 'y', 'U', '6', '#', '0']

ookisa = 100
DETAIL = len(aaset) -1

def drow(img):
    if img.shape[2] == 4:
        alpha_channel = img[:, :, 3]
        mask = (alpha_channel == 0)
        # そのピクセルのRGBチャネルを0に設定する
        img[mask] = [0, 0, 0, 0]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, None, fx=1, fy=0.5)
    xyratio = img.shape[1] / ookisa
    img = cv2.resize(img, (ookisa, int(img.shape[0]/xyratio)))
    monoratio = 255 / DETAIL
    img = img / monoratio
    aaarray = np.empty((img.shape[0], img.shape[1]), dtype=str)
    for i in range(aaarray.shape[0]):
        for j in range(aaarray.shape[1]):
            tmp = round(img[i][j])
            if img[i][j] == 0:
                aaarray[i][j] = " "
            else:
                aaarray[i][j] = aaset[tmp]

    result = ""
    for i in range(aaarray.shape[0]):
        for j in range(aaarray.shape[1]):
            result += aaarray[i][j]
        result += "\n"

    return result

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()