import cv2


# -----------------------------------------
# Function to Apply Color Filter
# -----------------------------------------

def apply_color_filter(image, filter_type):
    """Apply the selected color filter."""

    # Create a copy so the original image remains unchanged
    filtered_image = image.copy()

    if filter_type == "original":
        # Return the original image
        return filtered_image

    elif filter_type == "red_tint":
        # Keep only the Red channel
        filtered_image[:, :, 0] = 0  # Remove Blue
        filtered_image[:, :, 1] = 0  # Remove Green

    elif filter_type == "blue_tint":
        # Keep only the Blue channel
        filtered_image[:, :, 1] = 0  # Remove Green
        filtered_image[:, :, 2] = 0  # Remove Red

    elif filter_type == "green_tint":
        # Keep only the Green channel
        filtered_image[:, :, 0] = 0  # Remove Blue
        filtered_image[:, :, 2] = 0  # Remove Red

    elif filter_type == "increase_red":
        # Increase Red intensity
        filtered_image[:, :, 2] = cv2.add(
            filtered_image[:, :, 2],
            50
        )

    elif filter_type == "decrease_blue":
        # Decrease Blue intensity
        filtered_image[:, :, 0] = cv2.subtract(
            filtered_image[:, :, 0],
            50
        )

    return filtered_image


# -----------------------------------------
# Load the Image
# -----------------------------------------

image_path = "example.jpg"

image = cv2.imread(image_path)

# Check whether image was loaded
if image is None:
    print("Error: Could not load the image.")
    print("Please check the file path and file name.")
    exit()


# -----------------------------------------
# Display Menu
# -----------------------------------------

print("\n========== COLOR FILTER MENU ==========")
print("r - Red Tint")
print("b - Blue Tint")
print("g - Green Tint")
print("i - Increase Red Intensity")
print("d - Decrease Blue Intensity")
print("o - Original Image")
print("q - Quit")
print("=======================================")


# Start with the original image
filter_type = "original"


# -----------------------------------------
# Main Program Loop
# -----------------------------------------

while True:

    # Apply selected filter
    filtered_image = apply_color_filter(
        image,
        filter_type
    )

    # Display image
    cv2.imshow(
        "Color Filter",
        filtered_image
    )

    # Wait for keyboard input
    key = cv2.waitKey(0) & 0xFF

    # -----------------------------------------
    # Select Filter
    # -----------------------------------------

    if key == ord('r'):

        filter_type = "red_tint"
        print("Red Tint Applied")

    elif key == ord('b'):

        filter_type = "blue_tint"
        print("Blue Tint Applied")

    elif key == ord('g'):

        filter_type = "green_tint"
        print("Green Tint Applied")

    elif key == ord('i'):

        filter_type = "increase_red"
        print("Red Intensity Increased")

    elif key == ord('d'):

        filter_type = "decrease_blue"
        print("Blue Intensity Decreased")

    elif key == ord('o'):

        filter_type = "original"
        print("Original Image Restored")

    elif key == ord('q'):

        print("Exiting program...")
        break

    else:

        print(
            "Invalid key! "
            "Use r, b, g, i, d, o, or q."
        )


# -----------------------------------------
# Close All Windows
# -----------------------------------------

cv2.destroyAllWindows()