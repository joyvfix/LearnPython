# # import cv2
# # import time
# # import numpy as np
# # import HangTrackingModule as htm
# # import math
# # from ctypes import cast,POINTER
# # from comtypes import CLSCTX_ALL
# # from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# # wCam, hCam = 640,480

# # while true :
# #     succes, img = cap.read()
# #     img = detector.findHands(img)
# #     lmList = detector.findPosition(img, draw=False)
# #     if len(lmList)!=0:

# #         length = math.hypot(x2 - x1,y2 - y1)

# #         vol = np.interp(length,[50,300],[minVol,maxVol])
# #         volBar = np.interp(length,[50,300],[400,150])
# #         volPer = np.interp(length,[50,300],[0,100])
# #         print(int(length),vol)
# #         volume.SetMasterVolumeLevel(vol,None)

# #         if length < 50:
# #             cv2.circle(img,(cx, cy),15,(0,255,0),cv2.FILLED)
# # {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# # import cv2
# # import time
# # import numpy as np
# # import HandTrackingModule as htm
# # import math
# # from ctypes import cast, POINTER
# # from comtypes import CLSCTX_ALL
# # from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# # # Initialize webcam
# # cap = cv2.VideoCapture(0)
# # cap.set(3, 640)
# # cap.set(4, 480)

# # # Initialize hand tracking module
# # detector = htm.HandDetector()

# # # Set volume range
# # minVol = -65
# # maxVol = 0

# # # Initialize audio control
# # devices = AudioUtilities.GetSpeakers()
# # interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# # volume = cast(interface, POINTER(IAudioEndpointVolume))
# # volumeRange = volume.GetVolumeRange()
# # minVolume = volumeRange[0]
# # maxVolume = volumeRange[1]

# # while True:
# #     success, img = cap.read()
# #     img = detector.findHands(img)
# #     lmList = detector.findPosition(img, draw=False)

# #     if len(lmList) != 0:
# #         x1, y1 = lmList[4][1], lmList[4][2]  # Thumb tip coordinates
# #         x2, y2 = lmList[8][1], lmList[8][2]  # Index finger tip coordinates
# #         cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Center coordinates

# #         length = math.hypot(x2 - x1, y2 - y1)

# #         vol = np.interp(length, [50, 300], [minVol, maxVol])
# #         volBar = np.interp(length, [50, 300], [400, 150])
# #         volPer = np.interp(length, [50, 300], [0, 100])
# #         print(int(length), vol)

# #         volume.SetMasterVolumeLevel(vol, None)

# #         if length < 50:
# #             cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

# #     cv2.imshow("Hand Tracking", img)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# # cap.release()
# # cv2.destroyAllWindows()
# # {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# # import cv2
# # import numpy as np
# # import math
# # from ctypes import cast, POINTER
# # from comtypes import CLSCTX_ALL
# # from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# # import HandTrackingModule as htm

# # # Webcam dimensions
# # wCam, hCam = 640, 480

# # # Minimum and maximum volume levels
# # minVol = -65
# # maxVol = 0

# # # Initialize hand tracking module
# # detector = htm.HandDetector(detection_confidence=0.7)

# # # Get audio control interface
# # devices = AudioUtilities.GetSpeakers()
# # interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# # volume = cast(interface, POINTER(IAudioEndpointVolume))
# # volume_range = volume.GetVolumeRange()
# # min_volume = volume_range[0]
# # max_volume = volume_range[1]

# # # Initialize volume control variables
# # vol_bar = 400
# # vol_percentage = 0
# # volume_bar_pos = 150

# # # Initialize webcam
# # cap = cv2.VideoCapture(0)
# # cap.set(3, wCam)
# # cap.set(4, hCam)

# # # Main loop
# # while True:
# #     # Read frames from webcam
# #     success, img = cap.read()
# #     img = cv2.flip(img, 1)  # Flip horizontally for mirror effect

# #     # Find hand landmarks
# #     img = detector.find_hands(img)
# #     lm_list, bbox = detector.find_position(img, draw=True)

# #     # Check if landmarks are detected
# #     if len(lm_list) != 0:
# #         # Get coordinates of thumb and index finger
# #         x1, y1 = lm_list[4][1], lm_list[4][2]  # Thumb tip
# #         x2, y2 = lm_list[8][1], lm_list[8][2]  # Index finger tip
# #         cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Center coordinates

# #         # Draw a line between thumb and index finger
# #         cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
# #         cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

# #         # Calculate length and map it to the volume range
# #         length = math.hypot(x2 - x1, y2 - y1)
# #         volume_level = np.interp(length, [50, 300], [minVol, maxVol])
# #         volume_bar = np.interp(length, [50, 300], [400, 150])
# #         vol_percentage = np.interp(length, [50, 300], [0, 100])

# #         # Set volume level
# #         volume.SetMasterVolumeLevelScalar(volume_level, None)

# #         # Draw volume bar
# #         cv2.rectangle(img, (50, int(volume_bar)), (85, 400), (0, 255, 0), 3)
# #         cv2.rectangle(img, (50, int(vol_bar)),
# #                       (85, 400), (0, 255, 0), cv2.FILLED)
# #         cv2.putText(img, f'{int(vol_percentage)}%', (40, 450),
# #                     cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

# #     # Display the image
# #     cv2.imshow("Hand Volume Control", img)

# #     # Break the loop when 'q' is pressed
# #     if cv2.waitKey(1) == ord('q'):
# #         break

# # # Release the webcam and destroy windows
# # cap.release()
# # cv2.destroyAllWindows()
# # {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# import cv2

# # Define the callback function for mouse events


# def draw_control_volume(event, x, y, flags, param):
#     global top_left_pt, bottom_right_pt, drawing

#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         top_left_pt = (x, y)

#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         bottom_right_pt = (x, y)
#         cv2.rectangle(img, top_left_pt, bottom_right_pt, (0, 255, 0), 2)
#         cv2.imshow("Control Volume", img)


# # Create a blank image for drawing
# img = cv2.imread("path_to_your_image.jpg")  # Replace with your image path
# drawing = False
# top_left_pt, bottom_right_pt = (-1, -1), (-1, -1)

# # Create a window and bind the mouse callback function
# cv2.namedWindow("Control Volume")
# cv2.setMouseCallback("Control Volume", draw_control_volume)

# while True:
#     cv2.imshow("Control Volume", img)
#     key = cv2.waitKey(1) & 0xFF

#     # Press 'q' to exit the program
#     if key == ord("q"):
#         break

# cv2.destroyAllWindows()
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# import speech_recognition as sr
# import pyttsx3

# # Initialize text-to-speech engine
# engine = pyttsx3.init()

# # Function to speak the given text


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Function to convert speech to text


# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.pause_threshold = 1
#         audio = recognizer.listen(source)

#     try:
#         print("Recognizing...")
#         query = recognizer.recognize_google(audio, language="en")
#         print(f"You said: {query}")
#         return query
#     except sr.UnknownValueError:
#         print("Sorry, I didn't catch that.")
#         return ""
#     except sr.RequestError:
#         print("Sorry, I'm having trouble accessing the speech recognition service.")
#         return ""

# # Main function to run the AI assistant


# def run_ai_assistant():
#     while True:
#         query = listen()

#         if query:
#             if "hello" in query:
#                 speak("Hello! How can I assist you?")
#             elif "what is your name" in query:
#                 speak("My name is AI Assistant.")
#             elif "how are you" in query:
#                 speak("I'm fine, thank you!")
#             elif "quit" in query or "exit" in query:
#                 speak("Goodbye!")
#                 break
#             else:
#                 speak("I'm sorry, I can't help with that.")


# if __name__ == "__main__":
#     run_ai_assistant()
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


def set_system_volume(volume):
    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:
        volume_object = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume_object.SetMasterVolume(volume, None)


# Example usage: Set system volume to 50%
set_system_volume(0.5)
