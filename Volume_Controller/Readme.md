# Smart Volume Controller
In today's world of automation, it is crucial to develop smart systems that can control our </br>
basic devices like laptops, PCs, or televisions. This project is a Smart Volume Controller that adjusts</br>
the system volume using hand gestures, providing a touch-free way to control device audio.

## How It Works
This system uses a hand tracking module to detect specific gestures and then adjusts the device's volume based </br>
on the distance between the thumb and index finger. The system relies on OpenCV and MediaPipe for hand detection, </br>
and PyCaw to control the system's audio.


#Workflow:
- Hand Tracking:</br>
The system captures the hand gestures using the device's camera.</br>
It detects the landmarks on the hand (such as the thumb and index finger) using MediaPipe's Hand Tracking module.</br>

- Distance Calculation:</br>
The distance between the tip of the thumb and the tip of the index finger is calculated.</br>
This distance is then mapped to the volume range (e.g., from 0% to 100% volume).</br>

- Volume Adjustment:</br>
Using PyCaw, the system adjusts the volume based on the calculated distance.</br>
If the fingers are close together, the volume is set to low; as the fingers move apart, the volume increases.</br>

- Visual Feedback:</br>
A volume bar is displayed on the screen, providing visual feedback on the current volume level.</br>
A circle is drawn between the thumb and index finger to indicate gesture detection.</br>

## Features
- Gesture-Based Control: Adjust the system's volume with simple hand gestures.
- Real-Time Feedback: Displays the volume percentage and a visual bar indicating the current volume level.
- Dynamic FPS Display: Frame rate per second (FPS) is shown in real-time to ensure smooth performance.

## Tools and Libraries
- OpenCV: For capturing and processing real-time video.
- MediaPipe: For hand gesture tracking and detecting hand landmarks.
- PyCaw: For controlling the system's audio levels.
- NumPy: For mathematical operations.
- Math: For calculating the distance between hand landmarks.

## Requirements
- Python 3.x
- OpenCV
- MediaPipe
- PyCaw
- NumPy

## Setup Instructions
- Clone the repository:
git clone https://github.com/yourusername/smart-volume-controller.git
cd smart-volume-controller

- Install dependencies:
pip install opencv-python mediapipe numpy comtypes pycaw

- Run the program:
python smart_volume_controller.py

## Demo
Image of Gesture Control:
Below is an example showing the hand gesture controlling the volume level:



Video Demo:
Watch the video demonstrating how the smart volume controller works.
