import csv
from datetime import datetime

class DailyEmotionTracker:
    def __init__(self, csv_file_path):
        """
        Initialize the tracker with the provided CSV file path.
        """
        self.csv_file_path = csv_file_path
        self.emotion_data = {
            "happy": 0,
            "surprise": 0,
            "angry": 0,
            "sad": 0,
            "fear": 0,
            "disgust": 0,
            "neutral": 0
        }

    def read_emotion_csv(self):
        """
        Read the emotion data from the CSV file and track dominant emotions.
        """
        try:
            with open(self.csv_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    timestamp = row['timestamp']
                    dominant_emotion = row['dominant_emotion']
                    
                    if dominant_emotion in self.emotion_data:
                        self.emotion_data[dominant_emotion] += 1
        except FileNotFoundError:
            print(f"Error: The file '{self.csv_file_path}' does not exist.")
        except Exception as e:
            print(f"Error reading CSV file: {e}")
    
    def generate_daily_report(self):
        """
        Generate a daily report of tracked emotions.
        """
        report_date = datetime.now().strftime("%Y-%m-%d")
        print(f"Emotion Report for {report_date}:")

        for emotion, count in self.emotion_data.items():
            print(f"{emotion.capitalize()}: {count} occurrences")
        
        # Optionally, save the report to a new file
        report_file = f"daily_emotion_report_{report_date}.txt"
        with open(report_file, 'w') as f:
            f.write(f"Emotion Report for {report_date}:\n\n")
            for emotion, count in self.emotion_data.items():
                f.write(f"{emotion.capitalize()}: {count} occurrences\n")

        print(f"Report saved to {report_file}")
    
    def reset_emotion_data(self):
        """
        Reset emotion data for the next day.
        """
        self.emotion_data = {key: 0 for key in self.emotion_data}


if __name__ == "__main__":
    # Define the path to your CSV file
    csv_file_path = "emotion_log.csv"  # Change this path if necessary
    
    # Create an instance of the DailyEmotionTracker
    tracker = DailyEmotionTracker(csv_file_path)
    
    # Track emotions from the CSV file
    tracker.read_emotion_csv()
    
    # Generate the daily report
    tracker.generate_daily_report()

    # Optionally, reset data for the next day
    tracker.reset_emotion_data()
