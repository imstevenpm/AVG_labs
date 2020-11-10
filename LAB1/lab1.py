import numpy as np
import cv2
import matplotlib
from matplotlib import pyplot as plt

filename = 'tilef.jpg'
img = cv2.imread(filename)

plt.imshow(img ,cmap = 'gray')

plt.show()
