import cv2
import numpy as np

MATCHING = 0.9


def template_matching():
    # reading in the image
    img_rgb = cv2.imread('img/bear.jpg')

    # converting to grayscale
    # reading the template to be matched.
    template = cv2.imread('img/bear_tete.jpg', 0)
    hist_template_img = cv2.calcHist([template], [0], None, [256], [0, 256])

    w, h = template.shape[::-1]
    w_i, h_i = img_rgb_grey.shape[::-1]
    mask = np.zeros(img_rgb.shape[:2], np.uint8)
    img_copy = img_rgb.copy()
    w=w+10
    h=h+10

    for i in range(30, w_i-w, 20):
        for j in range(0, h_i-h, 20):
            mask_step = mask.copy()
            mask_step[j:h + j, i:w + i] = 255
            masked_img = cv2.bitwise_and(img_rgb, img_rgb, mask=mask_step)
            cv2.imshow('Detected', masked_img)
            cv2.waitKey(1)

            hist_masked_img = cv2.calcHist([masked_img], [0], mask_step, [256], [0, 256])
            # cv2.normalize(hist_template_img, hist_masked_img)
            cmp = cv2.compareHist(hist_template_img, hist_masked_img, cv2.HISTCMP_CORREL)
            if cmp > MATCHING:
                cv2.rectangle(img_copy, (i, j), (i + w, j + h), (0, 255, 255), 2)

    cv2.imshow('Detected', img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    template_matching()


if __name__ == '__main__':
    main()
