import cv2


class pointer:
    direction_svg = ["h", "v", "h-", "v-"]
    direction_d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def __init__(self, pos, dir):
        self.dir = dir
        self.path = f"M{pos[0]},{pos[1]}"
        self.dis = 0

    def go(self):
        self.dis += 1

    def right(self):
        self.path += f"{self.direction_svg[self.dir]}{self.dis}"
        self.dir += 1
        self.dir %= 4
        self.dis = 0

    def left(self):
        self.path += f"{self.direction_svg[self.dir]}{self.dis}"
        self.dir += 3
        self.dir %= 4
        self.dis = 0

    def get(self):
        return self.path


def get_outline(map, height, width, start_h, start_w, r):
    direction_d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    direction_c = [[0, -1], [0, 0], [-1, 0], [-1, -1]]
    pos = [start_w, start_h]
    if r == 1:
        p = pointer([start_w, start_h], 0)
        first_check_dir = 0
        second_check_dir = 1
        turn = [p.left, p.right]
    elif r == -1:
        p = pointer([start_w, start_h], 1)
        first_check_dir = 1
        second_check_dir = 0
        turn = [p.right, p.left]
    first = True
    while first or pos != [start_w, start_h]:
        first = False
        y1 = pos[1] + direction_c[(p.dir + first_check_dir) % 4][1]
        x1 = pos[0] + direction_c[(p.dir + first_check_dir) % 4][0]
        y2 = pos[1] + direction_c[(p.dir + second_check_dir) % 4][1]
        x2 = pos[0] + direction_c[(p.dir + second_check_dir) % 4][0]
        if y1 != -1 and y1 != height and x1 != -1 and x1 != width and map[y1][x1] == 0:
            turn[0]()
        elif y2 == -1 or y2 == height or x2 == -1 or x2 == width or map[y2][x2] == 255:
            turn[1]()
        p.go()
        pos[0] += direction_d[p.dir][0]
        pos[1] += direction_d[p.dir][1]
    return p.get()


def closed_area(height, width, map):
    stack = []
    for [h, w] in [[0, 0], [0, width - 1], [height - 1, 0], [height - 1, width - 1]]:
        map[h][w] = 0
    for x in range(1, width - 1):
        if map[0][x] == 255 and map[1][x] == 255:
            stack.append([1, x])
            map[1][x] = 0
        if map[height - 1][x] == 255 and map[height - 2][x] == 255:
            stack.append([height - 2, x])
            map[height - 2][x] = 0
        map[0][x], map[height - 1][x] = 0, 0
    for y in range(1, height - 1):
        if map[y][0] == 255 and map[y][1] == 255:
            stack.append([y, 1])
            map[y][1] = 0
        if map[y][width - 1] == 255 and map[y][width - 2] == 255:
            stack.append([y, width - 2])
            map[y][width - 2] = 0
        map[y][0], map[y][width - 1] = 0, 0
    while stack != []:
        [y, x] = stack.pop()
        for [dy, dx] in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            if map[y + dy][x + dx] == 255:
                stack.append([y + dy, x + dx])
                map[y + dy][x + dx] = 0
    for h in range(height):
        for w in range(width):
            map[h][w] = 255 - map[h][w]
    return map


def main():
    inpath = input()
    outpath = input()
    data = cv2.imread(inpath, -1)
    gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
    value, img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    height = len(img)
    width = len(img[0])
    outline = ""

    print("height:", height, "width:", width)
    print("-" * width)
    for h in range(height):
        for w in range(width):
            print("#" if img[h][w] == 0 else " ", end="")
        print()
    print("-" * width)

    start_dir = 1

    for start_h in range(height):
        for start_w in range(width):
            if img[start_h][start_w] == 0:
                outline += get_outline(img, height, width, start_h, start_w, start_dir)
                img = closed_area(height, width, img)
                start_dir *= -1

    with open(outpath, mode="w") as f:
        f.write(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}"><path d="{outline}"/></svg>'
        )


if __name__ == "__main__":
    main()
