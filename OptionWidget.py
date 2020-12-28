import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QCursor, QFontDatabase
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QPushButton, QSlider, QVBoxLayout, QLabel, \
    QHBoxLayout, QRadioButton, QMainWindow
import GameMenu
from functools import partial
from GameConfig import GameConfig


class OptionWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Options')
        self.setWindowIcon(QIcon('assets/icons/favicon.png'))
        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)
        self.setGeometry(400, 400, 400, 400)

        config = GameConfig()
        self.mode = config.readData('game_config.ini', 'Game values', 'dark_mode', 'bool')  # True mean dark mode on
        print('readed from file ', self.mode)
        self.botLevelValue = config.readData('game_config.ini', 'Game values', 'bot_level', 'int')
        print('readed from file ', self.botLevelValue)
        self.soundVolume = config.readData('game_config.ini', 'Game values', 'sound_volume', 'int')
        print('readed from file ', self.soundVolume)

        QFontDatabase.addApplicationFont('assets/fonts/VerminVibesV-Zlg3.ttf')

        vLayout = QVBoxLayout()
        vLayout.addStretch(1)

        self.okButton = QPushButton("OK")
        self.okButton.setStyleSheet("background-color: #5F634F")
        self.okButton.clicked.connect(self.submit)

        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.setStyleSheet('background-color: #5F634F')
        self.cancelButton.clicked.connect(self.cancel)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.okButton)
        hLayout.addWidget(self.cancelButton)

        self.labelRadioTitle = QLabel("Choose bot difficulty level")
        self.labelRadioTitle.setAlignment(Qt.AlignCenter)

        vLayout.addWidget(self.labelRadioTitle)

        self.radio1 = QRadioButton("Unbeatable")
        if self.botLevelValue == 1:
            self.radio1.setChecked(True)
        self.radio1.toggled.connect(self.setData)
        self.radio2 = QRadioButton("Medium")
        if self.botLevelValue == 2:
            self.radio2.setChecked(True)
        self.radio2.toggled.connect(self.setData)
        self.radio3 = QRadioButton("Stupid")
        if self.botLevelValue == 3:
            self.radio3.setChecked(True)
        self.radio3.toggled.connect(self.setData)

        vLayout.addWidget(self.radio1)
        vLayout.addWidget(self.radio2)
        vLayout.addWidget(self.radio3)

        self.labelTitle = QLabel("Change in game music volume")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        vLayout.addWidget(self.labelTitle)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(25)
        self.slider.setValue(self.soundVolume)
        self.slider.valueChanged.connect(self.setData)
        self.slider.setStyleSheet("""QSlider::groove:horizontal {
    border: 1px solid red;
    height: 6px;
    margin: 2px 0;
border-radius: 3px;
}
QSlider::handle:horizontal {
    background: red;
    border: 1px solid red;
    width: 3px;
    margin: -8px 0;
    border-radius: 1px;
}
QSlider::add-page:horizontal {
    background: #636e72;
}
QSlider::sub-page:horizontal {
    background: #d63031;
}""")

        vLayout.addWidget(self.slider)
        vLayout.addLayout(hLayout)
        self.setLayout(vLayout)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.button = QPushButton('', self)
        self.button.setIconSize(QSize(150, 90))
        self.button.move(110, 40)
        self.button.resize(170, 90)
        self.backgroundChange()
        self.button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button.clicked.connect(self.backgroundChangeWithValue)
        #  set and get the value of the right radio and the QSlider value
        self.setData()

        self.center()
        self.show()

    def setDarkMode(self):
        """Change the current state of the mode variable"""
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def backgroundChange(self):
        """Change the background color of the game"""
        if self.mode:
            self.setStyleSheet("background-color:rgb(22, 22, 22);"
                               "color: white;"
                               "font-family: Vermin Vibes V;")
            self.button.setStyleSheet("background-color: none;"
                                      "border-style: outset;"
                                      "cursor: pointer;"
                                      "color: rgb(0, 178, 62);")
            self.button.setIcon(QIcon('assets/icons/light.png'))
            self.okButton.setStyleSheet("background-color: #5F634F")
            self.cancelButton.setStyleSheet('background-color: #5F634F')
        else:
            self.setStyleSheet("background-color:white;"
                               "color: black;"
                               "font-family: Vermin Vibes V;")
            self.button.setStyleSheet("background-color: none;"
                                      "border-style: outset;"
                                      "cursor: pointer;"
                                      "color: rgb(0, 178, 62);")
            self.button.setIcon(QIcon('assets/icons/dark.png'))
            self.okButton.setStyleSheet("background-color: black;"
                                        "color: white")
            self.cancelButton.setStyleSheet('background-color: black;'
                                            'color: white')
        return 0

    def backgroundChangeWithValue(self):
        """Change the background color of the game and the self.mode var """
        self.setDarkMode()
        self.backgroundChange()

    def center(self):
        """align window center"""
        windowFrame = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(desktopWidget)
        self.move(windowFrame.topLeft())

    def setData(self):
        """Set the value of QRadio and QSlider"""
        if self.radio1.isChecked():
            print('current bot level : 1')
            self.botLevelValue = 1
        elif self.radio2.isChecked():
            print('current bot level : 2')
            self.botLevelValue = 2
        elif self.radio3.isChecked():
            print('current bot level : 3')
            self.botLevelValue = 3

        print("cuerrent mode : ", self.mode)
        print("current volume : ", self.slider.value())

    def submit(self):
        """Submit method will open the menu interface with the new args"""
        config = GameConfig()
        # print('before sub', self.mode)
        config.setData('game_config.ini', 'Game values', 'dark_mode', str(self.mode))
        config.setData('game_config.ini', 'Game values', 'bot_level', str(self.botLevelValue))
        config.setData('game_config.ini', 'Game values', 'sound_volume', str(self.slider.value()))
        self.ui = GameMenu.MenuInterface(self.mode, self.slider.value(), self.botLevelValue)
        self.ui.show()
        self.close()

    def cancel(self):
        """Cancel changes"""
        config = GameConfig()
        mode = config.readData('game_config.ini', 'Game values', 'dark_mode', 'bool')
        botLevelValue = config.readData('game_config.ini', 'Game values', 'bot_level', 'int')
        soundVolume = config.readData('game_config.ini', 'Game values', 'sound_volume', 'int')
        self.ui = GameMenu.MenuInterface(mode, soundVolume, botLevelValue)
        self.ui.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    OptionWindow = OptionWidget()
    sys.exit(app.exec_())
