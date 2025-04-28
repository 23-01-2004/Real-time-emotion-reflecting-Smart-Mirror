# emotion_filter_app.py

import os
import csv
import cv2
import random
from datetime import datetime
from emotion_recognition import RealTimeEmotionLogger

class EmotionFilterApp:
    """
    Class to apply real-time emotion-based filters, display quotes,
    and log dominant emotions with timestamps and saved frames.
    """

    emotion_quotes = {
        "happy": ["Keep smiling!", "Happiness is an inside job.", "Smile, it's free therapy! 😊"],
        "surprise": ["Life is full of surprises!", "Wow, that’s amazing! 🎉", "Keep expecting the unexpected! 😲"],
        "angry": ["Take a deep breath.", "Anger is a feeling; don't let it control you.", "Calm down and take control of your emotions. 😌"],
        "sad": ["It's okay to feel sad sometimes.", "This too shall pass.", "Keep going, the best is yet to come. 🌻"],
        "fear": ["Don't fear, you’re stronger than you think!", "Courage doesn’t mean you don’t fear, it means you don’t give up.", "Be brave. Fear is just a feeling. 💪"],
        "disgust": ["Take a break. Relax and breathe.", "It's okay to step away when things are unpleasant.", "Things will get better! 😊"],
        "neutral": ["Stay calm and focus.", "Every emotion is a part of you. Embrace it.", "Take a moment to reflect. 🌿"]
    }

    colormap = {
        "happy": cv2.COLORMAP_SUMMER,
        "sad": cv2.COLORMAP_BONE,
        "angry": cv2.COLORMAP_HOT,
        "surprise": cv2.COLORMAP_AUTUMN,
        "fear": cv2.COLORMAP_WINTER,
        "disgust": cv2.COLORMAP_OCEAN,
        "neutral": cv2.COLORMAP_PINK
    }

    def __init__(self, log_path="emotion_log.csv", save_dir="filtered_images"):
        """
        Initializes the EmotionFilterApp.

        Args:
            log_path (str): Path to the CSV log file.
            save_dir (str): Directory to save filtered images.
        """
        self.emotion_logger = RealTimeEmotionLogger()
        self.log_path = log_path
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)
        self.frame_count = 0
        self._initialize_log_file()

    def _initialize_log_file(self):
        """
        Initializes the emotion log CSV file if it does not exist.
        """
        if not os.path.exists(self.log_path):
            with open(self.log_path, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "dominant_emotion", "image_path"])

    def apply_filter(self, frame, emotion):
        """
        Applies a color filter to the frame based on the dominant emotion.

        Args:
            frame (np.ndarray): Input frame from webcam.
            emotion (str): Detected dominant emotion.

        Returns:
            np.ndarray: Filtered frame.
        """
        if emotion in self.colormap:
            filtered = cv2.applyColorMap(frame, self.colormap[emotion])
            return cv2.addWeighted(frame, 0.5, filtered, 0.5, 0)
        return frame

    def display_quote(self, frame, emotion):
        """
        Displays a random motivational quote based on the detected emotion.

        Args:
            frame (np.ndarray): Frame to draw the quote on.
            emotion (str): Detected dominant emotion.

        Returns:
            np.ndarray: Frame with overlaid quote text.
        """
        quote = random.choice(self.emotion_quotes.get(emotion, ["Keep going! You're doing great! 💪"]))
        cv2.putText(frame, quote, (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        return frame

    def save_frame_and_log(self, frame, dominant_emotion):
        """
        Saves the frame and logs the timestamp, emotion, and image path.

        Args:
            frame (np.ndarray): Frame to save.
            dominant_emotion (str): Detected dominant emotion.
        """
        timestamp = datetime.now()
        filename = f"{self.save_dir}/filtered_{timestamp.strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)

        with open(self.log_path, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp.isoformat(), dominant_emotion, filename])

    def run(self):
        """
        Runs the real-time emotion filter application.
        """
        print("Webcam is running with emotion filters. Press 'q' to quit.")
        while True:
            frame, emotions, dominant_emotion = self.emotion_logger.get_frame_and_emotion()
            if frame is None:
                print("Failed to capture frame.")
                break

            filtered_frame = self.apply_filter(frame, dominant_emotion)
            filtered_frame = self.display_quote(filtered_frame, dominant_emotion)

            if dominant_emotion:
                cv2.putText(filtered_frame, f"Dominant Emotion: {dominant_emotion}", (10, 25),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            if self.frame_count % 10 == 0:
                self.save_frame_and_log(filtered_frame, dominant_emotion)

            self.frame_count += 1
            cv2.imshow("Emotion-Filtered Webcam", filtered_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.emotion_logger.release()
        print("Session ended.")

if __name__ == "__main__":
    app = EmotionFilterApp()
    app.run()
