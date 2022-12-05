import cv2

img = cv2.imread('00-puppy-Copy1.jpg')

while True:
    cv2.imshow("Puppy",img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break;

cv2.destroyAllWindows()