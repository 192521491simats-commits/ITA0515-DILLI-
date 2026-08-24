import cv2
import time

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

print("Press 's' for Slow Motion")
print("Press 'f' for Fast Motion")
print("Press 'n' for Normal Speed")
print("Press 'q' to Quit")

speed = 1.0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break

    cv2.imshow("Web Camera", frame)

    key = cv2.waitKey(int(30 / speed)) & 0xFF

    if key == ord('s'):
        speed = 0.3          # Slow motion
        print("Slow Motion")

    elif key == ord('f'):
        speed = 3.0          # Fast motion
        print("Fast Motion")

    elif key == ord('n'):
        speed = 1.0          # Normal speed
        print("Normal Speed")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
