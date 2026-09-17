import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('example.jpg')

# Check if image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
    print("Please check the file name and path.")
    exit()

# Print original image dimensions
height, width = image.shape[:2]
print("Original Image Dimensions:", width, "x", height)

# -----------------------------
# Rotate the image by 45 degrees
# -----------------------------

# Find the center of the image
center = (width // 2, height // 2)

# Create rotation matrix
M = cv2.getRotationMatrix2D(center, 45, 1.0)

# Rotate the image
rotated = cv2.warpAffine(image, M, (width, height))

# Convert BGR to RGB for Matplotlib
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

# -----------------------------
# Increase Brightness
# -----------------------------

# Add 50 to pixel values
brightness_matrix = np.ones(image.shape, dtype=np.uint8) * 50

# Increase brightness safely
brighter = cv2.add(image, brightness_matrix)

# Convert BGR to RGB
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)

# -----------------------------
# Display Results
# -----------------------------

# Display original image
plt.figure(figsize=(7, 5))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")
plt.show()

# Display rotated image
plt.figure(figsize=(7, 5))
plt.imshow(rotated_rgb)
plt.title("Rotated Image - 45 Degrees")
plt.axis("off")
plt.show()

# Display brighter image
plt.figure(figsize=(7, 5))
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.axis("off")
plt.show()

# Print final information
print("Rotation: 45 degrees")
print("Brightness increased by: 50")