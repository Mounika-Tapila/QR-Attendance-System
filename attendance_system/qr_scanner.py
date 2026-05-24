import cv2
from pyzbar.pyzbar import decode

cam = cv2.VideoCapture(0)

print("Show QR code to camera")

while True:
    ret, frame = cam.read()

    for barcode in decode(frame):
        qr_data = barcode.data.decode('utf-8')
        print("QR Code Detected:", qr_data)

        # Draw rectangle
        pts = barcode.polygon
        if len(pts) > 4:
            pts = pts[:4]

        for i in range(len(pts)):
            cv2.line(frame, pts[i], pts[(i+1) % len(pts)], (0,255,0), 2)

        cv2.putText(frame, qr_data, (barcode.rect.left, barcode.rect.top),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    cv2.imshow("QR Scanner", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()