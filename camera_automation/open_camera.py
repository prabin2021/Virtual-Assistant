import subprocess as sp
import cv2

def open_camera():
        sp.run('start microsoft.windows.camera:', shell=True)
def capture_photo():
        from main import speak

        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite('captured_photo.jpg', image)
        del(camera)
        speak("Photo captured successfully!")