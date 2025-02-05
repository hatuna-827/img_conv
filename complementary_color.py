import cv2
inpath=input()
outpath=input()
data=cv2.imread(inpath)
for y in range(len(data)):
    for x in range(len(data[0])):
        sum=max(data[y][x])+min(data[y][x])
        for i in range(3):
            data[y][x][i]=sum-data[y][x][i]
cv2.imwrite(outpath,data)
