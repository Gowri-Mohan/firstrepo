import cv2
import numpy as np

#filepath=input('enter filepath of image file=')
#img=cv2.imread(filepath)
img = cv2.imread('/Users/gowrimohan/Desktop/chessboard.jpg')

black_pixels = np.where(
    (img[:, :, 0] == 0) & 
    (img[:, :, 1] == 0) & 
    (img[:, :, 2] == 0)
)

white_pixels = np.where(
    (img[:, :, 0] == 255) & 
    (img[:, :, 1] == 255) & 
    (img[:, :, 2] == 255)
)

img[black_pixels] = [255, 255, 255]
img[white_pixels] = [0, 0, 0]

cv2.imshow('Image',img)





