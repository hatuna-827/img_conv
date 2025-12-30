import cv2

inpath = input()
outpath = input()
data = cv2.imread(inpath, -1)
gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
value, img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite(outpath, img)
