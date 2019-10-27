import cv2
from matplotlib import pyplot as plt

# reading in the image
imgs = ['img\\beach.jpg','img\\bear.jpg','img\\dog.jpg', 'img\\lake.jpg', 'img\\moose.jpg',
        'img\\polar.jpg', 'img\\waves.jpg']

img = cv2.imread(imgs[0],0)

for s in imgs:
    img2 = cv2.imread(s, 0)
    # Calculate histogram
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

    # compare
    gap = cv2.compareHist(hist, hist2, cv2.HISTCMP_CORREL)

    print(s)
    print(gap)

# print
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.plot(hist)
plt.subplot(223), plt.plot(hist2)
plt.xlim([0,480])
plt.show()