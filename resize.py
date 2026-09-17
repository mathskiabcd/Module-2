import cv2

# Load the image
image = cv2.imread('example.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
    print("Please check the file name and path.")
    exit()

# Resize the actual image to 800 x 500
resized_image = cv2.resize(image, (800, 500))

# Create a window
cv2.namedWindow('Resized Image', cv2.WINDOW_NORMAL)

# Display the resized image
cv2.imshow('Resized Image', resized_image)

# Wait until any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

# Print image properties
print("Original Image Dimensions:", image.shape)
print("Resized Image Dimensions:", resized_image.shape)