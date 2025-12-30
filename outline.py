import cv2


def _p(height, width, vertical, horizontal):
    for h in range(height + 1):
        for w in range(width):
            print(
                "|" if h != 0 and vertical[h - 1][w] else " ",
                "_" if horizontal[h][w] else " ",
                sep="",
                end="",
            )
        print("|" if h != 0 and vertical[h - 1][width] else " ")
    print()


inpath = input()
outpath = input()
data = cv2.imread(inpath, -1)
gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
value, img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

height = len(img)
width = len(img[0])

vertical = []
horizontal = []
for h in range(height + 1):
    if h < height:
        vertical.append([])
    horizontal.append([])
    for w in range(width + 1):
        if h < height:
            vertical[h].append(False)
        if w < width:
            horizontal[h].append(False)

for h in range(height):
    for w in range(width):
        if img[h][w] == 0:
            vertical[h][w] = not vertical[h][w]
            vertical[h][w + 1] = True
            horizontal[h][w] = not horizontal[h][w]
            horizontal[h + 1][w] = True

for start_h in range(height):
    for start_w in range(width):
        if (horizontal[h][w]):
            print()

print(height)
print(width)
_p(height, width, vertical, horizontal)

with open(outpath, mode="w") as f:
    f.write("hoge")
