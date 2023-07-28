# SARecorder - Screen and Audio Recorder

SARecorder is a simple Python application that allows you to record your screen and audio. It provides a graphical user interface (GUI) to easily start recording your screen or audio for a specified duration.

## Requirements

Before running the SARecorder application, ensure you have the following dependencies installed:

1. Python 3.x
2. OpenCV (`cv2`)
3. PyAutoGUI
4. NumPy
5. PyAudio

You can install the required Python packages using `pip`:

```bash
pip install opencv-python pyautogui numpy pyaudio
```

## Installation

To use the SARecorder application, follow these steps:

1. Clone the SARecorder repository from GitHub:

   ```bash
   git clone https://github.com/yourusername/SARecorder.git
   ```

2. Change into the SARecorder directory:

   ```bash
   cd SARecorder
   ```

3. Run the application:

   ```bash
   python gui.py
   ```

## How to Use

1. When you run the `gui.py` file, a GUI window will open.
2. The window will display a welcome message and two buttons: "Screen Recorder" and "Audio Recorder."
3. To record your screen, click the "Screen Recorder" button. A dialog will prompt you to enter the recording duration in seconds. After entering the duration, the screen recording will begin immediately.
4. To record audio, click the "Audio Recorder" button. A dialog will prompt you to enter the recording duration in seconds. After entering the duration, the audio recording will begin immediately.

## Note

- The screen recordings will be saved in the file "test.mp4" in the same directory as the application.
- The audio recordings will be saved in the file "recorded_audio.wav" in the same directory as the application.

## Contact

For any questions or feedback, feel free to contact me at prajapatiarjun2801@gmail.com.

Happy recording!
