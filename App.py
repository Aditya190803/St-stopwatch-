import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")
        self.setGeometry(100, 100, 250, 150)

        # Initialize the stopwatch state
        self.running = False
        self.elapsed_time = 0
        self.start_time = 0

        # Set up UI components
        self.layout = QVBoxLayout()

        # Display the time
        self.time_label = QLabel("00:00:00", self)
        self.time_label.setStyleSheet("font-size: 40px;")
        self.layout.addWidget(self.time_label)

        # Start button
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start)
        self.layout.addWidget(self.start_button)

        # Stop button
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop)
        self.layout.addWidget(self.stop_button)

        # Reset button
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.clicked.connect(self.reset)
        self.layout.addWidget(self.reset_button)

        # Set the layout
        self.setLayout(self.layout)

        # Timer to update the stopwatch display
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.timer.start(100)  # Update every 100 ms
            self.start_button.setText("Pause")

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time
            self.timer.stop()
            self.start_button.setText("Resume")

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.timer.stop()
        self.time_label.setText("00:00:00")
        self.start_button.setText("Start")

    def update_time(self):
        current_time = time.time() - self.start_time
        minutes, seconds = divmod(current_time, 60)
        hours, minutes = divmod(minutes, 60)
        self.time_label.setText(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Stopwatch()
    window.show()
    sys.exit(app.exec_())
