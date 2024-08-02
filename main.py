import cv2
import sys
import aa
import os

path = "img/pose.png"
ext = os.path.splitext(path)[1]
ext = ext[1:]
video = ["gif", "mp4", "avi", "mov", "wmv", "flv", "mkv", "webm", "m4v", "3gp", "3g2"]
image = ["jpg", "jpeg", "png", "bmp", "tiff"]

if ext in video:
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        sys.exit()

    row = 0
    f = True
    while True:
        try:
            ret, frame = cap.read()
            if ret:
                cv2.imshow('image', frame)
                AA = aa.drow(frame)
                if f:
                    row = AA.count("\n")+1
                    f = False

                print(AA+"\033["+str(row)+"A")
                if cv2.waitKey(50) & 0xFF == ord('q'):
                    raise KeyboardInterrupt
            else:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        except KeyboardInterrupt:
            # subprocess.run(["cls"], shell=True)
            print("\033["+str(row)+"B")
            print("quit")
            break
else:
    img = cv2.imread(path)

    if img is not None:
        AA = aa.drow(img)
        cv2.imshow('image', img)
        print(AA)
    else:
        sys.exit()

cv2.destroyAllWindows()