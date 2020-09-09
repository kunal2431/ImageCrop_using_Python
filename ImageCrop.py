import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("Image.jpg")
plt.imshow(img)

face = img[70:350 , 200:450, 0:3] #[range of y-axis(height), range of x-axis(width), RGB ]
plt.imshow(face)
plt.imsave("final.jpg",face) # It saves cropped Image
