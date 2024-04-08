import cv2
import dlib
from scipy.spatial import distance as dist
from datetime import datetime


testTime = datetime.now()
timeMinute = testTime.minute
testConverted = str(timeMinute)
fileName = '.\\user_data\\' + testConverted + '-from-video.txt'

file = open(fileName, 'a', encoding="utf-8")

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

# Загрузка видеофайла
video_filename = '.\\videofiles\\5.mp4'
video_capture = cv2.VideoCapture(video_filename)

# Извлечение размеров кадра
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Определение кодека для создания .mp4 видео
codec = cv2.VideoWriter_fourcc(*'mp4v')

# Создание объекта VideoWriter для записи видео в .mp4 формате
# output_video = cv2.VideoWriter('output_video.mp4', codec, 30, (frame_width, frame_height))

# Номера индексов для левого и правого глаз
(lStart, lEnd) = (42, 48)
(rStart, rEnd) = (36, 42)

# Чтение видеофайла и анализ EAR
while True:
    ret, frame = video_capture.read()

    if not ret:
        break
    
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

        # Запись кадра в выходное видео
        # output_video.write(frame)

    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение видеопотока и объекта VideoWriter
video_capture.release()
output_video.release()
cv2.destroyAllWindows()