import cv2

# Захватываем видеопоток с веб-камеры
cap = cv2.VideoCapture(0)

# Устанавливаем параметры видео (ширина, высота)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Создаем объект для записи видео
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('//videofiles//output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Отображаем кадр
    cv2.imshow('Video', frame)
    
    # Записываем кадр в файл
    out.write(frame)
    
    # Прерываем цикл при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
out.release()
cv2.destroyAllWindows()