import math
import numpy as np 

# def distance_between_points(point1, point2):
#     x1, y1, z1 = point1
#     x2, y2, z2 = point2
#     print(z1)
#     distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
#     return distance

# # Example usage:
# point1 = np.array([1, 2, 3])
# point2 = [4, 5, 6]
# print("Distance between points:", distance_between_points(point1, point2))



def CalculateDistance(point1, point2):

    print(type(point1),type(point2))
    print(point1,point2)


    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[1])**2)
    
    return distance

arr = np.array([[3,4],[1,2],[4,6]])
xr = np.array([1,2])

d = (arr - xr) ** 2

dist = d.sum(axis=1)



print(dist)
print(np.sqrt(dist))