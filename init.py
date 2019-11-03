from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLineEdit, QDialog
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Himnario Adventista"
        self.screen = App.primaryScreen().size()
        oImage = QImage("icons/background.jpg")
        sImage = oImage.scaled(QSize(self.screen.width(), self.screen.height()))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.UIComponents()
        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icons/icon.jpg"))
        self.setWindowTitle(self.title)
        self.showFullScreen()
        self.show()

    # UI Components Generation
    def UIComponents(self):
        # Layout
        layout = QHBoxLayout()
        
        # Song TextBox
        txtSong = QLineEdit(self)
        txtSong.setFont(QtGui.QFont("Sanserif", 15))
        # txtSong.move(self.screen.width() / 2, 250)

        # Play Button
        btnPlaySong = QPushButton("Ir..", self)
        # btnPlaySong.move(self.screen.width() / 2, 300)
        btnPlaySong.setIcon(QtGui.QIcon("icons/play.jpg"))
        btnPlaySong.clicked.connect(self.btnPlaySongClick)
        
        layout.addWidget(txtSong)
        layout.addWidget(btnPlaySong)
        self.setLayout(layout)
    
    # Events
    def btnPlaySongClick(self):
        # Action for play song
        self.openSongWindow()

    def openSongWindow(self):
        songWindow = QDialog()
        songWindow.setModal(True)
        songWindow.showFullScreen()
        songWindow.exec()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            sys.exit(App.exec())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())