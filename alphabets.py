import pickle
import cv2
import mediapipe as mp
import numpy as np

# Load the trained model from the saved pickle file
model_dict = pickle.load(open('./letters-detection/model.p', 'rb'))
model = model_dict['model']

# Open the webcam for capturing video
cap = cv2.VideoCapture(0)

# Initialize the MediaPipe Hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
# Configure the Hands module to detect only one hand
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.3)

# Dictionary mapping numeric labels to alphabetical characters
labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 
               10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 
               19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

# Main loop for capturing video frames and performing hand gesture recognition
while True:
    # Initialize lists to store hand landmarks data
    data_aux = []
    x_ = []
    y_ = []

    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Get the height and width of the frame
    H, W, _ = frame.shape

    # Convert the frame from BGR to RGB color space
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame using the MediaPipe Hands module
    results = hands.process(frame_rgb)

    # Check if hand landmarks are detected in the frame
    if results.multi_hand_landmarks:
        # Draw hand landmarks on the frame
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        # Extract hand landmarks data for gesture recognition
        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        # Calculate bounding box coordinates for the detected hand
        x1 = int(min(x_) * W) - 10
        y1 = int(min(y_) * H) - 10
        x2 = int(max(x_) * W) - 10
        y2 = int(max(y_) * H) - 10

        # Make a prediction using the trained model
        try:
            prediction = model.predict([np.asarray(data_aux)])
        except ValueError as e:
            # Skip this frame if there is an issue with the input data shape
            print(" ----------------- Shape of input data:", np.asarray(data_aux).shape)
            continue

        # Print the predicted gesture label
        print("Prediction =>", labels_dict[int(prediction[0])])

        # Get the predicted character based on the numeric label
        predicted_character = labels_dict[int(prediction[0])]

        # Draw bounding box and predicted character label on the frame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

    # Display the processed frame with hand landmarks and predicted character
    cv2.imshow('frame', frame)

    # Wait for user input to exit the loop (press 'q' key)
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
