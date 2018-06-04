# -- encoding : utf-8 --
import cv2
import matplotlib as plt
import numpy as np
image = cv2.imread("009.png")
# cv2.imshow('original',image)
# cv2.waitKey()  #important

kernel =  np.array([[0.11, 0.11, 0.11],
                   [0.11, 0.11, 0.11],
                   [0.11, 0.11, 0.11]])
rect = cv2.filter2D(image,-1,kernel)
# cv2.imshow('rect.jpg',rect)
# cv2.waitKey()
kernelgao = np.array([[1, 4, 7, 4, 1],
                      [4, 16, 26, 16, 4],
                      [7, 26, 41, 26, 4],
                      [4, 16, 26, 14, 4],
                      [1, 4, 7, 4, 1]
]
)