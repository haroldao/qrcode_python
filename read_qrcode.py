import cv2
from main import file_name

detector = cv2.QRCodeDetector()
file_name+= ".png"
val, points, qrcode = detector.detectAndDecode(cv2.imread(file_name))

# Print Link from the qrcode
print(val)