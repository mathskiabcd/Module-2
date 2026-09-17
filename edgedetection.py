import cv2
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------
# Function to Display an Image
# -----------------------------------------

def display_image(title, image):
    """Display grayscale or color image using Matplotlib."""

    plt.figure(figsize=(8, 6))

    if len(image.shape) == 2:
        # Grayscale image
        plt.imshow(image, cmap='gray')
    else:
        # Color image
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image_rgb)

    plt.title(title)
    plt.axis('off')
    plt.show()


# -----------------------------------------
# Function to Get a Positive Odd Number
# -----------------------------------------

def get_odd_number(message):
    """Ask the user for a positive odd number."""

    while True:
        try:
            number = int(input(message))

            if number > 0 and number % 2 == 1:
                return number

            print("Please enter a positive odd number.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# -----------------------------------------
# Main Edge Detection Activity
# -----------------------------------------

def interactive_edge_detection(image_path):

    # Load the image
    image = cv2.imread(image_path)

    # Check if image was loaded
    if image is None:
        print("Error: Could not load the image.")
        print("Please check the file path and image name.")
        return

    print("\nImage loaded successfully!")

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display original image
    display_image("Original Image", image)

    # Display grayscale image
    display_image("Grayscale Image", gray_image)

    # -----------------------------------------
    # Menu
    # -----------------------------------------

    while True:

        print("\n========== IMAGE PROCESSING MENU ==========")
        print("1. Sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Gaussian Smoothing")
        print("5. Median Filtering")
        print("6. Exit")
        print("===========================================")

        choice = input("Enter your choice (1-6): ")

        # -----------------------------------------
        # 1. Sobel Edge Detection
        # -----------------------------------------

        if choice == "1":

            print("\nApplying Sobel Edge Detection...")

            sobel_x = cv2.Sobel(
                gray_image,
                cv2.CV_64F,
                1,
                0,
                ksize=3
            )

            sobel_y = cv2.Sobel(
                gray_image,
                cv2.CV_64F,
                0,
                1,
                ksize=3
            )

            # Convert negative values to positive
            sobel_x = cv2.convertScaleAbs(sobel_x)
            sobel_y = cv2.convertScaleAbs(sobel_y)

            # Combine horizontal and vertical edges
            combined_sobel = cv2.addWeighted(
                sobel_x,
                0.5,
                sobel_y,
                0.5,
                0
            )

            display_image(
                "Sobel Edge Detection",
                combined_sobel
            )

        # -----------------------------------------
        # 2. Canny Edge Detection
        # -----------------------------------------

        elif choice == "2":

            print("\nCanny Edge Detection")

            try:
                lower_thresh = int(
                    input("Enter Lower threshold (0-255): ")
                )

                upper_thresh = int(
                    input("Enter Upper threshold (0-255): ")
                )

                if not (0 <= lower_thresh < upper_thresh <= 255):
                    print(
                        "Invalid thresholds. "
                        "Make sure 0 <= lower < upper <= 255."
                    )
                    continue

                edges = cv2.Canny(
                    gray_image,
                    lower_thresh,
                    upper_thresh
                )

                display_image(
                    "Canny Edge Detection",
                    edges
                )

            except ValueError:
                print("Invalid input. Please enter numbers.")

        # -----------------------------------------
        # 3. Laplacian Edge Detection
        # -----------------------------------------

        elif choice == "3":

            print("\nApplying Laplacian Edge Detection...")

            laplacian = cv2.Laplacian(
                gray_image,
                cv2.CV_64F
            )

            laplacian = cv2.convertScaleAbs(laplacian)

            display_image(
                "Laplacian Edge Detection",
                laplacian
            )

        # -----------------------------------------
        # 4. Gaussian Smoothing
        # -----------------------------------------

        elif choice == "4":

            print("\nGaussian Smoothing")

            kernel_size = get_odd_number(
                "Enter kernel size (positive odd number): "
            )

            blurred = cv2.GaussianBlur(
                image,
                (kernel_size, kernel_size),
                0
            )

            display_image(
                "Gaussian Smoothed Image",
                blurred
            )

        # -----------------------------------------
        # 5. Median Filtering
        # -----------------------------------------

        elif choice == "5":

            print("\nMedian Filtering")

            kernel_size = get_odd_number(
                "Enter kernel size (positive odd number): "
            )

            median_filtered = cv2.medianBlur(
                image,
                kernel_size
            )

            display_image(
                "Median Filtered Image",
                median_filtered
            )

        # -----------------------------------------
        # 6. Exit
        # -----------------------------------------

        elif choice == "6":

            print("\nExiting program...")
            break

        # -----------------------------------------
        # Invalid Choice
        # -----------------------------------------

        else:

            print(
                "Invalid choice. "
                "Please select a number between 1 and 6."
            )


# -----------------------------------------
# Start the Program
# -----------------------------------------

image_path = "example.jpg"

interactive_edge_detection(image_path)