import sys
import cv2
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QTimer

class VideoRecorderApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(VideoRecorderApp, self).__init__()
        uic.loadUi('video_recorder.ui', self)
        self.start_button.clicked.connect(self.start_recording)
        self.stop_button.clicked.connect(self.stop_recording)
        self.save_button.clicked.connect(self.save_video)
        
        self.video = cv2.VideoCapture(0)
        self.is_recording = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.record_video)
        
    def start_recording(self):
        self.is_recording = True
        self.timer.start(20)
        
    def stop_recording(self):
        self.is_recording = False
        self.timer.stop()
        
    def record_video(self):
        ret, frame = self.video.read()
        if ret:
            cv2.imshow('Video', frame)
            if self.is_recording:
                self.out.write(frame)
    
    def save_video(self):
        save_path, _ = QFileDialog.getSaveFileName(self, 'Save Video', '', 'Video Files (*.avi)')
        if save_path:
            self.out = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'XVID'), 20, (640, 480))
            QMessageBox.information(self, 'Video Saved', 'Video saved successfully!')
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = VideoRecorderApp()
    window.show()
    sys.exit(app.exec_())