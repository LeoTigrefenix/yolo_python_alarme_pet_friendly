import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import pygame
pygame.mixer.init()
pygame.mixer.music.load("alarme.mp3")
pygame.mixer.music.play()

