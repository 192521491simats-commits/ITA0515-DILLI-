import cv2

img = cv2.imread("I3.png")

if img is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original Image", img)
cv2.imshow("Outline using Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
