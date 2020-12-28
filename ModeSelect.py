import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QRadioButton, \
    QDesktopWidget
import GameInterface
import CPUVSPlayer
import GameMenu


class ModeSelect(QWidget):
    def __init__(self, lightMode, volume, botLevel):
        super().__init__()
        self.lightMode = lightMode
        self.volume = volume
        self.botLevel = botLevel
        print('In Select Mode light value: ', self.lightMode)
        print('In Select Mode volume: ', self.volume)
        print('In Select Mode bot level: ', self.botLevel)
        self.setWindowTitle('Options')
        self.setWindowIcon(QIcon('assets/icons/favicon.png'))
        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)
        self.setGeometry(400, 400, 400, 400)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        QFontDatabase.addApplicationFont('assets/fonts/VerminVibesV-Zlg3.ttf')

        mainHLayout = QHBoxLayout()
        vLayout = QVBoxLayout()
        self.okButton = QPushButton("OK")
        self.okButton.setStyleSheet("background-color: #5F634F")
        self.okButton.clicked.connect(self.submit)

        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.setStyleSheet('background-color: #5F634F')
        self.cancelButton.clicked.connect(self.cancel)

        self.labelRadioTitle = QLabel("Choose Game mode to start")
        self.labelRadioTitle.setStyleSheet("color: #d63031;"
                                           "font-size: 10pt")

        vLayout.addWidget(self.labelRadioTitle)

        self.radio1 = QRadioButton("Player VS Player")
        self.radio1.setChecked(False)
        self.radioStyleSheet(self.radio1)
        self.radio1.toggled.connect(self.setData)

        self.radio2 = QRadioButton("Player VS Computer")
        self.radio2.setChecked(True)
        self.gameMode = "Player VS Bot"
        self.radioStyleSheet(self.radio2)
        self.radio2.toggled.connect(self.setData)

        self.radio3 = QRadioButton("Bot VS Bot(computer)")
        self.radio3.setChecked(False)
        self.radioStyleSheet(self.radio3)
        self.radio3.toggled.connect(self.setData)
        vLayout.addSpacing(50)
        vLayout.addWidget(self.radio1)
        vLayout.addSpacing(60)
        vLayout.addWidget(self.radio2)
        vLayout.addSpacing(60)
        vLayout.addWidget(self.radio3)
        vLayout.addSpacing(30)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.okButton)
        hLayout.addWidget(self.cancelButton)

        vLayout.addLayout(hLayout)
        mainHLayout.addLayout(vLayout)
        mainHLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(mainHLayout)
        self.backgroundChange()
        self.center()
        self.show()

    def backgroundChange(self):
        """Change the background color of the game"""
        if self.lightMode:
            self.setStyleSheet("background-color:rgb(22, 22, 22);"
                               "color: white;"
                               "font-family: Vermin Vibes V;")
            self.okButton.setStyleSheet("background-color: #5F634F")
            self.cancelButton.setStyleSheet('background-color: #5F634F')
        else:
            self.setStyleSheet("background-color:white;"
                               "color: black;"
                               "font-family: Vermin Vibes V;")
            self.okButton.setStyleSheet("background-color: black;"
                                        "color: white")
            self.cancelButton.setStyleSheet('background-color: black;'
                                            'color: white')

    def radioStyleSheet(self, radio):
        """set a custom style sheet to the radio object"""
        radio.setStyleSheet("""
QRadioButton::indicator {
    width:                  10px;
    height:                 10px;
    border-radius:          7px;
}

QRadioButton::indicator:checked {
    background-color:       red;
    border:                 2px solid white;
}

QRadioButton::indicator:unchecked {
    background-color:       black;
    border:                 2px solid white;
}
                            """)

    def center(self):
        """align window center"""
        windowFrame = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(desktopWidget)
        self.move(windowFrame.topLeft())

    def setData(self):
        """Set the value of QRadio"""
        if self.radio1.isChecked():
            print('Player VS Player')
            self.gameMode = "Player VS Player"
        elif self.radio2.isChecked():
            print('Player VS Bot(Computer)')
            self.gameMode = "Player VS Bot"
        elif self.radio3.isChecked():
            print('Bot VS Bot')
            self.gameMode = "Bot VS Bot"

    def submit(self):
        if self.gameMode == 'Player VS Player':
            self.GameInter = GameInterface.GameInterface(self.lightMode, self.volume, self.botLevel, self.gameMode)
            self.GameInter.show()
            self.close()
        elif self.gameMode == 'Player VS Bot' or self.gameMode == 'Bot VS Bot':
            self.CPU = CPUVSPlayer.CPUVSPlayer(self.lightMode, self.volume, self.botLevel, self.gameMode)
            self.CPU.show()
            self.close()

    def cancel(self):
        self.menu = GameMenu.MenuInterface(self.lightMode, self.volume, self.botLevel)
        self.menu.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    modeSelUi = ModeSelect()
    sys.exit(app.exec_())
