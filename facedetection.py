import cv2


# -----------------------------------------
# Load Haar Cascade Face Detector
# -----------------------------------------

face_cascade_path = (
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

face_cascade = cv2.CascadeClassifier(face_cascade_path)

# Check if Haar Cascade was loaded
if face_cascade.empty():
    print("Error: Could not load the face detection model.")
    exit()


# -----------------------------------------
# Start Webcam
# -----------------------------------------

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()


# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


print("Face Detection Started")
print("Press 'q' to quit.")


# -----------------------------------------
# Face Detection Loop
# -----------------------------------------

while True:

    # Capture a frame
    ret, frame = cap.read()

    # Check whether frame was captured
    if not ret:
        print("Error: Could not read frame from camera.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangle around every detected face
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

    # Display number of detected faces
    face_count = len(faces)

    cv2.putText(
        frame,
        f"Faces Detected: {face_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Display instructions
    cv2.putText(
        frame,
        "Press Q to Quit",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Show the video
    cv2.imshow(
        "Face Detection",
        frame
    )

    # Press Q to exit
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break


# -----------------------------------------
# Release Resources
# -----------------------------------------

cap.release()
cv2.destroyAllWindows()

print("Face detection stopped.")