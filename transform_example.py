import cv2
import numpy as np
from fourpointtransform import four_point_transform

# Define the four points
points = [(120, 460), (710, 220), (950, 500), (360, 820)]

# Convert the points to a NumPy array
pts = np.array(points, dtype="float32")

# Reshape the points to be a list of (x, y) pairs
pts = pts.reshape(-1, 2)

# Load the image
image = cv2.imread("image.jpg")

# Apply the four-point transform to obtain a "bird's-eye view" of the image
warped = four_point_transform(image, pts)

# Show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
