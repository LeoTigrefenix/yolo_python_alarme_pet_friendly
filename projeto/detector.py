import cv2
from ultralytics import YOLO
# from playsound import playsound  # ou use pygame se preferir
import pygame

import time

# Carrega o modelo YOLO
model = YOLO("yolov8n.pt")  # ou yolov5s.pt

# Abre a câmera
cap = cv2.VideoCapture(0)

# Controle de alarme (para não disparar sem parar)
last_alarm_time = 0
alarm_interval = 10  # segundos

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Faz a detecção
    results = model(frame)
    boxes = results[0].boxes
    classes_detectadas = [model.names[int(box.cls[0])] for box in boxes]

    # Exibe o vídeo com anotações
    annotated_frame = results[0].plot()
    cv2.imshow("Pet Friendly Alarm", annotated_frame)

    # Se houver uma pessoa e nenhum cachorro, dispare o alarme
    if "person" in classes_detectadas:
        # Ignorar se só tiver cachorro
        if "dog" in classes_detectadas and len(classes_detectadas) == 1:
            pass
        else:
            current_time = time.time()
            if current_time - last_alarm_time > alarm_interval:
                print("⚠️ Pessoa detectada! Disparando alarme...")
                pygame.mixer.init()
                pygame.mixer.music.load("alarme.mp3")
                pygame.mixer.music.play()

                last_alarm_time = current_time

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
