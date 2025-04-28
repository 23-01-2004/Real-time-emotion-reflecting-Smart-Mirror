# Real-Time Emotion-Reflecting Smart Mirror Project

## Project Overview
The **Real-Time Emotion-Reflecting Smart Mirror** project involves creating an intelligent mirror that detects the user's emotional state using facial recognition. Based on the dominant emotion detected from a live webcam feed, the mirror applies dynamic filters to the mirror display, shows motivational quotes or emojis, and keeps track of daily emotional trends. The project uses **OpenCV**, a pre-trained **emotion detection model**, and integrates a logging system to track emotional data over time.

This smart mirror provides both practical and interactive features, enhancing the user's experience with real-time feedback on their emotional state.

## Features
1. **Emotion Detection**: The system continuously captures frames from the webcam feed and detects the user’s emotions, including `happy`, `sad`, `angry`, `fear`, `surprise`, `disgust`, and `neutral`. These emotions are detected using a facial emotion recognition model.
   
2. **Emotion-Based Color Filters**: Upon detecting the dominant emotion, a corresponding color filter is applied to the webcam feed. For instance:
   - **Happy**: The feed gets a bright yellow filter.
   - **Sad**: The feed receives a blueish tone.
   - **Angry**: The feed gets a red filter.
   - **Fear**: The feed gets a cold blue filter, etc.

3. **Motivational Quotes and Emojis**: Based on the dominant emotion, a motivational quote or emoji is displayed on the screen. The quotes are pre-defined for each emotion to encourage the user based on their current mood.

4. **Real-Time Image Saving**: The system saves every 10th frame of the webcam feed into a folder named `filtered_images`. Each image is stored with a timestamp and the dominant emotion associated with that frame.

5. **Daily Emotion Tracker**: The system generates a daily report of the dominant emotions recorded throughout the day. This report is saved in a CSV file and provides insights into the user’s emotional trends, including a breakdown of the most frequent emotions.

6. **Webcam Feed Display**: The real-time webcam feed is displayed to the user with the appropriate emotion-based filters and quotes.

## Technologies Used
- **Python 3.x**: Main programming language used for the project.
- **OpenCV**: For real-time video capture, image processing, and filter application.
- **Emotion Recognition Model**: A pre-trained model (or custom-built) to recognize facial emotions from webcam feed.
- **CSV**: For logging the detected emotions and image file paths.
- **Datetime**: For timestamping the frames and emotion logs.
  
## Installation Instructions
### 1. Install Python 3.x:
Ensure that you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

### 2. Install Required Libraries:
To get started, install the necessary Python libraries:
```bash
pip install opencv-python opencv-python-headless pandas
