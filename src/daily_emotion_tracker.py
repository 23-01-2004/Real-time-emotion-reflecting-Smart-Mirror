import cv2
import numpy as np
import pandas as pd
from datetime import datetime, date

class DailyEmotionTracker:
    def __init__(self, log_file="emotion_log.csv"):
        self.log_file = log_file
        self.today_emotion = self.get_today_dominant_emotion()
        self.suggestions = self.generate_all_recommendations(self.today_emotion)
        self.display_lines = []

    def get_today_dominant_emotion(self):
        try:
            df = pd.read_csv(self.log_file)
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            today_logs = df[df["timestamp"].dt.date == date.today()]
            dominant = today_logs["dominant_emotion"].mode()[0] if not today_logs.empty else "neutral"
            return dominant
        except Exception as e:
            print("Error:", e)
            return "neutral"

    def generate_all_recommendations(self, emotion):
        return [
            f"[1] Mental Health Tip:\n→ {self.mental_health_tip(emotion)}",
            f"[2] Music Suggestion:\n→ {self.music_link(emotion)}",
            f"[3] Video Suggestion:\n→ {self.video_link(emotion)}",
            f"[4] Activity Tip:\n→ {self.activity_suggestion(emotion)}",
            f"[5] Quote + Fact:\n→ {self.quote_fact(emotion)}",
            f"[6] Color Mood Suggestion:\n→ {self.color_therapy(emotion)}",
            f"[7] Weekly Summary Hint:\n→ Track your mood every day to unlock weekly insights!",
            f"[8] Mindfulness Prompt:\n→ {self.mindfulness_tip(emotion)}",
            f"[9] Emotion-Based Goal:\n→ {self.goal_suggestion(emotion)}"
        ]

    def mental_health_tip(self, emotion):
        tips = {
            "sad": "Try writing your thoughts in a journal.",
            "angry": "Step away from the screen and breathe for 3 minutes.",
            "fear": "Name 5 things you can see right now.",
        }
        return tips.get(emotion, "Be kind to yourself today.")

    def music_link(self, emotion):
        return f"https://open.spotify.com/search/{emotion}%20playlist"

    def video_link(self, emotion):
        return f"https://www.youtube.com/results?search_query={emotion}+motivational+video"

    def activity_suggestion(self, emotion):
        return {
            "sad": "Take a walk in fresh air.",
            "angry": "Do 5 minutes of stretching.",
            "happy": "Call a friend and share the joy!"
        }.get(emotion, "Try a small physical activity.")

    def quote_fact(self, emotion):
        return {
            "happy": "Quote: 'Smile and the world smiles with you.' Fact: Smiling reduces stress.",
            "sad": "Quote: 'This too shall pass.' Fact: Crying releases stress hormones.",
        }.get(emotion, "Quote: Emotions are data, not directives. Fact: Every emotion has a role.")

    def color_therapy(self, emotion):
        return {
            "sad": "Use calming blues or greens.",
            "angry": "Warm pastels like peach can soothe you.",
            "happy": "Bright yellows lift the mood!"
        }.get(emotion, "Soft light pink promotes calm.")

    def mindfulness_tip(self, emotion):
        return "Take 3 deep breaths. Inhale... exhale..."

    def goal_suggestion(self, emotion):
        return {
            "neutral": "Focus and complete one pending task today.",
            "sad": "Text someone you trust and talk.",
            "happy": "Celebrate one small win!"
        }.get(emotion, "Keep a positive intention today.")

    def show_and_save(self):
        img_height = 900
        img_width = 1000
        padding = 20
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        font_color = (10, 10, 10)
        line_height = 25

        img = 255 * np.ones((img_height, img_width, 3), dtype=np.uint8)
        y_offset = 40

        full_text_output = []

        for i, suggestion in enumerate(self.suggestions):
            lines = suggestion.split('\n')
            full_text_output.append(suggestion + "\n")
            for line in lines:
                cv2.putText(img, line, (padding, y_offset), font, font_scale, font_color, 1, cv2.LINE_AA)
                y_offset += line_height
            y_offset += 15  # extra spacing between blocks

            cv2.imshow("Daily Emotion Tracker", img)
            cv2.waitKey(2000)  # wait 2 seconds before next suggestion

        # Save all 9 recommendations to a text file
        filename = f"report/daily_recommendations_{date.today()}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(full_text_output)

        print(f"✅ Saved all recommendations to: {filename}")
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    tracker = DailyEmotionTracker()
    tracker.show_and_save()
