# from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
# import ctypes

# # Function to set the master volume level (range: 0.0 to 1.0)


# def set_master_volume(volume_level):
#     sessions = AudioUtilities.GetAllSessions()
#     for session in sessions:
#         volume = session._ctl.QueryInterface(ISimpleAudioVolume)
#         volume.SetMasterVolume(volume_level, None)

# # Function to increase the volume by a specified percentage


# def increase_volume(percentage):
#     sessions = AudioUtilities.GetAllSessions()
#     for session in sessions:
#         volume = session._ctl.QueryInterface(ISimpleAudioVolume)
#         current_volume = volume.GetMasterVolume()
#         new_volume = max(0.0, min(1.0, current_volume + percentage))
#         volume.SetMasterVolume(new_volume, None)

# # Function to decrease the volume by a specified percentage


# def decrease_volume(percentage):
#     increase_volume(-percentage)


# # Example Usage:
# # Set the master volume to 70% (0.7)
# set_master_volume(0.7)

# # Increase the volume by 10%
# increase_volume(0.1)

# # Decrease the volume by 10%
# decrease_volume(0.1)
# {::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::}
import cv2
import numpy as np
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# Function to control the volume based on the hand position


def control_volume(y, frame_height):
    # Map the y-coordinate of hand to volume level (0.0 to 1.0)
    volume_level = 1 - y / frame_height
    # Ensure volume is in the range [0, 1]
    volume_level = max(0, min(1, volume_level))

    # Set the master volume to the calculated level
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(volume_level, None)


# Open camera
capture = cv2.VideoCapture(0)

# Variables for background subtraction
background = None
accumulated_weight = 0.5

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    # Convert the frame to grayscale for processing
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (25, 25), 0)

    # Initialize background if it's None
    if background is None:
        background = gray_frame.copy().astype("float")
        continue

    # Accumulate the weighted average between the current frame and previous frames
    cv2.accumulateWeighted(gray_frame, background, accumulated_weight)

    # Compute the absolute difference between the current frame and background
    delta_frame = cv2.absdiff(gray_frame, cv2.convertScaleAbs(background))

    # Threshold the delta frame to obtain binary image
    _, thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(
        thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the contour with the largest area (hand)
        hand_contour = max(contours, key=cv2.contourArea)

        # Get bounding box of the hand contour
        x, y, w, h = cv2.boundingRect(hand_contour)

        # Draw the bounding box and centroid of the hand
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (x + w // 2, y + h // 2), 4, (0, 0, 255), -1)

        # Control volume based on hand position
        control_volume(y + h // 2, frame.shape[0])

    # Show the frame with bounding box and centroid
    cv2.imshow("Gesture Volume Control", frame)

    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
