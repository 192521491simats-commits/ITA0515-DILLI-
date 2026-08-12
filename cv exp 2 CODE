import cv2

img = cv2.imread("i2.png")

if img is None:
    print("Error: Image not found!")
    exit()

blur = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blurred Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
