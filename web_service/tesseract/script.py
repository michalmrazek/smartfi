import cv2
import pytesseract


img = cv2.imread("https://www.nvaccess.org/wp-content/uploads/2017/10/ocrimage.png")
text = pytesseract.image_to_string(img)
print(text)
