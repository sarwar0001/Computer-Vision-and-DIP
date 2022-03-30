import cv2

img1 = cv2.imread('D:/Image_processing/iron_man.jpg')
img1 = cv2.resize(img1,(1200,700))
cv2.imshow("original_one",img1)
"""
cv2.waitKey()
cv2.destroyAllWindows()
"""

key = cv2.waitKey()
if key == ord("s"):
    cv2.imwrite('D:/Image_processing/original_one.jpg',img1)
else:
    cv2.destroyAllWindows()
    