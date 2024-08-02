import cv2
import sys
import aa

path = "img/Animhorse.gif"
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

cv2.destroyAllWindows()