import cv2


def open_camera():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read the current frame from the camera
        ret, frame = cap.read()

        # If reading was successful, display the frame
        if ret:
            cv2.imshow('Camera', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()


# Call the function to open the camera
open_camera()
