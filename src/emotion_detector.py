from deepface import DeepFace
import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Use DeepFace to analyze emotions in the frame
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    
    # Get the dominant emotion
    dominant_emotion = result[0]['dominant_emotion']
    
    # Display the emotion on the frame
    cv2.putText(frame, dominant_emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the webcam feed
    cv2.imshow('Emotion Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
