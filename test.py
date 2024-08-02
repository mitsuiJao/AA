import cv2
import numpy as np

img = np.zeros((100, 400, 3), dtype=np.uint8)
# x: 20, y: 50の位置に"ABCxyz"という文字列を描画
cv2.putText(img, "Hello Font", (20, 50), cv2.FONT_HERSHEY_DUPLEX, 2.0, (255,255,255),2)
# 座標が分かるよう線を引く
cv2.imshow("Test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
