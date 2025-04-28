# emotion_logger.py

import os
import csv
import cv2
from datetime import datetime
from deepface import DeepFace

class RealTimeEmotionLogger:
    def __init__(self, save_dir="captured_images", csv_file="emotion_log.csv"):
        self.save_dir = save_dir
        self.csv_file = csv_file
        self.frame_count = 0
        os.makedirs(self.save_dir, exist_ok=True)
        self._init_csv()
        self.cap = cv2.VideoCapture(0)

    def _init_csv(self):
        if not os.path.isfile(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "image_filename", "angry", "disgust", "fear", "happy", "sad", "surprise", "neutral", "dominant_emotion"])

    def log_emotion(self, frame, emotions, dominant_emotion):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = os.path.join(self.save_dir, f"frame_{timestamp}.jpg")
        cv2.imwrite(image_filename, frame)

        with open(self.csv_file, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                timestamp,
                image_filename,
                emotions.get('angry', 0),
                emotions.get('disgust', 0),
                emotions.get('fear', 0),
                emotions.get('happy', 0),
                emotions.get('sad', 0),
                emotions.get('surprise', 0),
                emotions.get('neutral', 0),
                dominant_emotion
            ])

    def get_frame_and_emotion(self):
        ret, frame = self.cap.read()
        if not ret:
            return None, None, None

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotions = result[0]['emotion']
            dominant_emotion = result[0]['dominant_emotion']

            if self.frame_count % 10 == 0:
                self.log_emotion(frame, emotions, dominant_emotion)

            self.frame_count += 1
            return frame, emotions, dominant_emotion

        except Exception as e:
            print("Emotion detection failed:", e)
            return frame, {}, None

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
