import cv2 
import uuid
### livelong - on fornt of ur face and left side using the other hand.
### perfect - on fornt of ur face and left side using the other hand.
### stop - on fornt of ur face and left side using the other hand.
labels=['livelong','perfect','stop','yes','no','thumbsup']
label='livelong'
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()

        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename=f'saved_images_test\{label}.{str(uuid.uuid1())}.jpg', img=frame)
        if key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break