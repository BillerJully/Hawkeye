import cv2
import dlib
from scipy.spatial import distance as dist
from datetime import datetime
import time


testTime = datetime.now()
timeMinute = testTime.minute
testConverted = str(timeMinute)
fileName = '.\\user_data\\' + testConverted + '-file-time.txt'

file = open(fileName, 'a', encoding="utf-8")

# file.write("***********************************\n")
# file.write("*******NEW TEST***********\n")
# nowTime = datetime.now()
# convertedTime = str(nowTime)
# file.write(convertedTime + "\n")
# file.write("***********************************\n")

# Функция для вычисления EAR
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Инициализация детекторов лиц и ключевых точек
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(".\\face_dot_files\\shape_predictor_68_face_landmarks.dat")

# Номера индексов для левого и правого глаз
(lStart, lEnd) = (42, 48)
(rStart, rEnd) = (36, 42)

# Захват видеопотока с веб-камеры
video_capture = cv2.VideoCapture(0)
# время работы программы 20 сек
# start_time = time.time()
# run_time = 20

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц в кадре
    faces = detector(gray, 0)
    for face in faces:
        shape = predictor(gray, face)
        shape = [(shape.part(i).x, shape.part(i).y) for i in range(68)]
        
        # Извлечение координат глаз
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        # Вычисление EAR для каждого глаза
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        convertedEar = ear
        if (convertedEar < 0):
            convertedEar = convertedEar * (-1)
        convertedEar = round(convertedEar, 4)
        filesText = str(convertedEar)

        file.write(filesText + "\n")
        # Отображение значения EAR на кадре
        cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    # Время работы без ограничений
    if cv2.waitKey(1) & 0xFF == ord('q'):
    # if time.time() - start_time > run_time:
        break

video_capture.release()
cv2.destroyAllWindows()