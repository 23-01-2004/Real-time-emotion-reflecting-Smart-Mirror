import cv2

def open_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error ! Webcam not opened")

        return
    print("webcam is running. Press q to quit")
    
    while True : 
        ret, frame = cap.read()
        if not ret:
            print("failed to capture frame")
            break 

        cv2.imshow("Smart Mirror", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_webcam()