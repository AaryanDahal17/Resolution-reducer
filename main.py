import numpy as np
import cv2
import os
from matplotlib import pyplot as plt


imageName = 'rand.png'

imagePath = os.path.join('image',imageName)

image_array = cv2.imread(imagePath)

image_array_RGB = cv2.cvtColor(image_array,cv2.COLOR_BGR2RGB)

print("image pixel size :",image_array_RGB.shape)

image_backup = image_array_RGB

pixel_height , pixel_width , pixel_dimension = image_array_RGB.shape

yz = 0

# plt.imshow(image_array_RGB[0]) # image ko first pixel row ko strip 

# plt.show()

import math

def CalculateDistance(point1, point2):

    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[1])**2)
    
    return distance



# we are going to use 10 colors only of the image

numOfColors = 10

random_colors_array = []

for i in range(numOfColors):

    h = np.random.randint(0,pixel_height)
    w = np.random.randint(0,pixel_width)

    random_colors_array.append(image_array_RGB[h][w])


for h in range(pixel_height):
    
    for w in range(pixel_width):

        pixel = image_array_RGB[h][w]

        lowestDistance = CalculateDistance(pixel,random_colors_array[0])
        dist = 0
        index = 0

        for j in range(1,numOfColors):
            dist = CalculateDistance(pixel,random_colors_array[j])
            if lowestDistance > dist:
                lowestDistance = dist
                index = j

        image_array_RGB[h][w] = random_colors_array[index]


plt.imshow(image_array_RGB)
plt.show()


# Not implemented clustering yet