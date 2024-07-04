import cv2
import numpy as np
print("Hello World")

# Introduce an unused import
import random

# Create a blank image
image = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw a rectangle with inconsistent naming convention (use camelCase)
cv2.rectangle(image, (50, 50), (200, 150), (0, 255, 0), thickness=2)
cv2.rectangle(image, (250, 200), (400, 300), (255, 0, 0), thickness=2)  # Duplicate rectangle unnecessarily

# Draw a circle with inconsistent spacing
cv2.circle(image, (300, 100),30,(0, 0, 255), thickness=-1)

# Display the image
cv2.imshow('OpenCV Example', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Hello World")

# Create a blank image with different dimensions
image2 = np.zeros((600, 800, 3), dtype=np.uint8)

# Draw a rectangle with inconsistent parameter order
cv2.rectangle(image2, (50, 50), (150, 200), (0, 255, 0), thickness=2)

# Draw a circle with inconsistent indentation
  cv2.circle(image2, (300, 100), 50, (0, 0, 255), thickness=-1)  # Incorrect indentation

# Display the image
cv2.imshow('OpenCV Example 2', image2)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
