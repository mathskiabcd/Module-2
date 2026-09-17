import cv2
import matplotlib.pyplot as plt

# Step 1: Load the Image
image_path = 'example.jpg'
image = cv2.imread(image_path)

# Check if image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
    print("Please check the image path or file name.")
    exit()

# Get image dimensions
height, width = image.shape[:2]

print("Image Width:", width, "pixels")
print("Image Height:", height, "pixels")

# Convert BGR to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ------------------------------------------------
# Step 2: Draw Rectangle 1 - Top Left
# ------------------------------------------------

rect1_width = 150
rect1_height = 150

top_left1 = (20, 20)
bottom_right1 = (
    top_left1[0] + rect1_width,
    top_left1[1] + rect1_height
)

cv2.rectangle(
    image_rgb,
    top_left1,
    bottom_right1,
    (255, 255, 0),
    3
)

# ------------------------------------------------
# Step 3: Draw Rectangle 2 - Bottom Right
# ------------------------------------------------

rect2_width = 200
rect2_height = 150

top_left2 = (
    max(0, width - rect2_width - 20),
    max(0, height - rect2_height - 20)
)

bottom_right2 = (
    min(width - 1, top_left2[0] + rect2_width),
    min(height - 1, top_left2[1] + rect2_height)
)

cv2.rectangle(
    image_rgb,
    top_left2,
    bottom_right2,
    (255, 0, 255),
    3
)

# ------------------------------------------------
# Step 4: Find Centers of Both Rectangles
# ------------------------------------------------

center1 = (
    (top_left1[0] + bottom_right1[0]) // 2,
    (top_left1[1] + bottom_right1[1]) // 2
)

center2 = (
    (top_left2[0] + bottom_right2[0]) // 2,
    (top_left2[1] + bottom_right2[1]) // 2
)

# Draw green circles at the centers
cv2.circle(image_rgb, center1, 15, (0, 255, 0), -1)
cv2.circle(image_rgb, center2, 15, (0, 255, 0), -1)

# ------------------------------------------------
# Step 5: Connect the Two Centers
# ------------------------------------------------

cv2.line(
    image_rgb,
    center1,
    center2,
    (0, 255, 0),
    3
)

# ------------------------------------------------
# Step 6: Add Text Labels
# ------------------------------------------------

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(
    image_rgb,
    'Region 1',
    (top_left1[0], max(20, top_left1[1] - 10)),
    font,
    0.7,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

cv2.putText(
    image_rgb,
    'Region 2',
    (top_left2[0], max(20, top_left2[1] - 10)),
    font,
    0.7,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

cv2.putText(
    image_rgb,
    'Center 1',
    (center1[0] - 40, center1[1] + 40),
    font,
    0.6,
    (0, 255, 0),
    2,
    cv2.LINE_AA
)

cv2.putText(
    image_rgb,
    'Center 2',
    (center2[0] - 40, center2[1] + 40),
    font,
    0.6,
    (0, 255, 0),
    2,
    cv2.LINE_AA
)

# ------------------------------------------------
# Step 7: Draw Bi-Directional Height Arrow
# ------------------------------------------------

arrow_x = width - 50

arrow_start = (arrow_x, 20)
arrow_end = (arrow_x, height - 20)

# Downward arrow
cv2.arrowedLine(
    image_rgb,
    arrow_start,
    arrow_end,
    (255, 255, 0),
    3,
    tipLength=0.05
)

# Upward arrow
cv2.arrowedLine(
    image_rgb,
    arrow_end,
    arrow_start,
    (255, 255, 0),
    3,
    tipLength=0.05
)

# ------------------------------------------------
# Step 8: Add Height Label
# ------------------------------------------------

height_label = f'Height: {height}px'

label_x = max(10, arrow_x - 170)
label_y = height // 2

cv2.putText(
    image_rgb,
    height_label,
    (label_x, label_y),
    font,
    0.8,
    (255, 255, 0),
    2,
    cv2.LINE_AA
)

# ------------------------------------------------
# Step 9: Display Final Image
# ------------------------------------------------

plt.figure(figsize=(12, 8))

plt.imshow(image_rgb)
plt.title('Annotated Image')
plt.axis('off')

plt.show()