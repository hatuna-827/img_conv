import cv2

inpath = input()
outpath = input()
data = cv2.imread(inpath, -1)
gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
cv2.imwrite(outpath, gray)
