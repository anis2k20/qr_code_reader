import cv2

img = cv2.imread("qr_code.jpg")

detector = cv2.QRCodeDetector()

data,bbox,straight_qrcode = detector.detectAndDecode(img)
print(data)

