import cv2
import os

video_path = "V6.mp4"
output_path = r"C:\Users\Akash\Pictures\Screenshots\output_video.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Video not found!")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create output folder if it doesn't exist
os.makedirs(r"C:\Users\Akash\Pictures\Screenshots", exist_ok=True)

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    # Save frame
    out.write(frame)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved successfully at:")
print(output_path)
