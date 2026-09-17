import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('example.jpg')

# Check if image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
    print("Please check the file name and path.")
    exit()

# Print original image dimensions
height, width, channels = image.shape
print("Original Image Dimensions:", width, "x", height)
print("Channels:", channels)

# Resize the actual image
resized_image = cv2.resize(image, (800, 500))

# Convert BGR to RGB
image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

# Display RGB image
plt.figure(figsize=(8, 5))
plt.imshow(image_rgb)
plt.title("Resized RGB Image")
plt.axis("off")
plt.show()

# Convert to Grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Display Grayscale image
plt.figure(figsize=(8, 5))
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

# Crop the image
# Rows: 100 to 300
# Columns: 200 to 400
cropped_image = resized_image[100:300, 200:400]

# Check if cropped region is valid
if cropped_image.size == 0:
    print("Error: Cropping region is invalid.")
    exit()

# Convert cropped image from BGR to RGB
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

# Display cropped image
plt.figure(figsize=(6, 4))
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.axis("off")
plt.show()

# Print cropped image dimensions
print("Cropped Image Dimensions:", cropped_image.shape)