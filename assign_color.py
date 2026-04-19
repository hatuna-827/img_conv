import cv2
import numpy as np
import random


def hex_to_bgr(hex_color):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return np.array([b, g, r], dtype=np.uint8)


def assign_color(img, target, replace):
    target_bgr = np.array([hex_to_bgr(c) for c in target], dtype=np.uint8)
    replace_bgr = np.array([hex_to_bgr(c) for c in replace], dtype=np.uint8)
    img_bgr = img[:, :, :3]
    mask = np.zeros(img.shape[:2], dtype=bool)
    for t in target_bgr:
        mask |= np.all(img_bgr == t, axis=-1)
    rand_idx = np.random.randint(0, len(replace_bgr), size=img.shape[:2])
    for i, color in enumerate(replace_bgr):
        img[mask & (rand_idx == i), :3] = color
    return img


# definition
assign_list = [
    (
        ["#000000"],
        [
            "#1F8484",
            "#8E6B00",
            "#00819A",
            "#847200",
            "#8E00E0",
            "#4E42FE",
            "#1A8C58",
            "#BF2222",
            "#A3571E",
        ],
    ),
    (
        ["#FFFFFF"],
        [
            "#239696",
            "#A97236",
            "#C85028",
            "#997D2B",
            "#938200",
            "#00A328",
            "#7F8D00",
            "#249E64",
            "#6C6CE4",
            "#9D45E1",
        ],
    ),
]

# input
inpath = input()
outpath = input()

# assign color
img = cv2.imread(inpath, -1)
for [target, replace] in assign_list:
    img = assign_color(img, target, replace)

cv2.imwrite(outpath, img)
