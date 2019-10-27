import cv2

image = cv2.imread('img.png')

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0


g = image.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

br = image.copy()
# set green channels to 0
br[:, :, 1] = 0

bg = image.copy()
# set red channels to 0
bg[:, :, 2] = 0

rg = image.copy()
# set red channels to 0
rg[:, :, 0] = 0


# RGB - Blue
# cv2.imshow('B-RGB', b)

# RGB - Green
# cv2.imshow('G-RGB', g)

# RGB - Red
# cv2.imshow('R-RGB', r)

# RGB - Blue&Red
cv2.imshow('BR-RGB', br)

# RGB - Green&Blue
cv2.imshow('GB-RGB', bg)

# RGB - Red&Green
cv2.imshow('RG-RGB', rg)

cv2.waitKey(0)