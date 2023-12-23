import cv2
import face_recognition

# Load the image with faces
image_path = "path/to/your/image.jpg"
image = face_recognition.load_image_file(image_path)

# Find face locations in the image
face_locations = face_recognition.face_locations(image)

# Load the image using OpenCV for further processing
cv_image = cv2.imread(image_path)

# Loop through each face found in the image
for face_location in face_locations:
    # Get the coordinates of the face
    top, right, bottom, left = face_location

    # Draw a rectangle around the face
    cv2.rectangle(cv_image, (left, top), (right, bottom), (0, 255, 0), 2)

    # Extract the face region
    face_image = cv_image[top:bottom, left:right]

    # Use dlib to detect eyes in the face region
    predictor_path = "shape_predictor_68_face_landmarks.dat"  # Download from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    # Convert the face image to grayscale for dlib
    gray_face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray_face_image)

    # Loop through the detected faces
    for face in faces:
        # Get the landmarks (including eyes)
        landmarks = predictor(gray_face_image, face)

        # Extract the coordinates of the eyes
        left_eye = landmarks.part(36).x, landmarks.part(36).y
        right_eye = landmarks.part(45).x, landmarks.part(45).y

        # Draw circles around the eyes
        cv2.circle(face_image, left_eye, 5, (255, 0, 0), -1)
        cv2.circle(face_image, right_eye, 5, (255, 0, 0), -1)

# Display the image with face and eyes detected
cv2.imshow("Face and Eyes Detection", cv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
