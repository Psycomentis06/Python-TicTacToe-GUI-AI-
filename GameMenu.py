import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QPushButton, QWidget, QMessageBox, QMainWindow, QApplication, QDesktopWidget, \
    QLabel, QVBoxLayout
import OptionWidget
import ModeSelect


class MenuInterface(QMainWindow):
    def __init__(self, mode, slider, botLevelValue):
        """Constructor"""
        super().__init__()
        self.darkMode = mode
        self.musicVolume = slider
        self.botLevel = botLevelValue
        print(mode)
        print(slider)
        print(botLevelValue)
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.setGeometry(600, 600, 600, 600)
        self.setWindowIcon(QIcon('assets/icons/favicon.png'))
        self.setWindowTitle('Welcome to Tic Tac Toe')
        self.setStyleSheet("background-color:rgb(22, 22, 22);"
                           "color: white")
        self.menuWidget = QWidget()
        self.setCentralWidget(self.menuWidget)
        self.menuWindow()
        self.createButtons('Start', 220, 100, 180, 80, self.start)  # Create the Start Button
        self.createButtons('Option', 220, 100, 180, 180, self.optionMenu)  # Create the Option  Button
        self.createButtons('About', 220, 100, 180, 280, self.about)  # Create the About Button
        self.createButtons('Exit', 220, 100, 180, 380, exit)  # Create the About Button
        self.center()
        self.show()

    def center(self):
        """align window center"""
        windowFrame = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(desktopWidget)
        self.move(windowFrame.topLeft())

    def menuWindow(self):
        menuLayout = QVBoxLayout(self.menuWidget)
        menuLabel = QLabel(self)
        menuLayout.addWidget(menuLabel)
        menuLabel.setStyleSheet("background-color:rgb(55,55,55)")

    def start(self):
        """Open the select mode"""
        print("Start")
        print('**************')
        self.ui = ModeSelect.ModeSelect(self.darkMode, self.musicVolume, self.botLevel)
        self.ui.show()
        self.close()

    def optionMenu(self):
        self.window = QWidget()
        self.ui = OptionWidget.OptionWidget()
        self.close()

    def about(self):
        QMessageBox.about(self, "About the game",
                          "<p>The <b>Tic Tac Toe</b> game is a simple game created using PYQT5 and Python3."
                          "This game is created for educational purpose for learning Python to get a certification. "
                          "The GUI and the main functions of the app are made by the PYQT5 library under non comercial "
                          "use.</p>"
                          "<h3><b>Developper:</b> Amor Ali</h3>"
                          "<h3><b>Version:</b> 1.00</h3>"
                          "<h3><b>Platform:</b> Cross Platform</h3>"
                          "<h3><center>Copyright: 2019-2020</center></h3>"
                          )

    def createButtons(self, title, resizeW, resizeH, moveX, moveY, functionName):
        button = QPushButton(title, self)
        button.clicked.connect(functionName)
        button.resize(resizeW, resizeH)
        button.move(moveX, moveY)
        button.setStyleSheet("background-color: none;"
                             "border-style: outset;"
                             "font: bold 14px;"
                             "cursor: pointer;"
                             "font-size:24pt;"
                             "color: rgb(0, 178, 62);"
                             "font-family: ubuntu mono")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MenuUi = MenuInterface()
    sys.exit(app.exec_())
