import sys

from PyQt5.QtCore import QTimer, QSize
from PyQt5.QtGui import QCursor, QIcon, QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QApplication, QDialog, \
    QDesktopWidget, QWidget, QLabel, QMessageBox
from PyQt5 import QtCore
from PyQt5 import QtMultimedia
from functools import partial
import GameMenu
import SaveData


class GameInterface(QMainWindow):

    def __init__(self, lightMode, volume, botLevel, gameMode):
        super().__init__()
        self.lightMode = lightMode
        self.volume = volume
        self.inGameVolume = volume
        self.botLevel = botLevel
        self.gameMode = gameMode
        self.setWindowTitle('Tic Tac Toe')
        self.setWindowIcon(QIcon('assets/icons/favicon.png'))
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.setGeometry(600, 600, 600, 600)
        QFontDatabase.addApplicationFont('assets/fonts/HALO____.ttf')
        self.playerRoleText = self.createPlayerRoleText('Player1')
        self.volumeHomeBtns()
        self.board = [' ' for i in range(9)]  # Game main board
        self.player1Role = True  # Player 1 is role First
        self.player2Role = False  # Player 2 waiting player 1 to play
        self.musicPlayer()
        self.btn1 = self.createButtons(' ', 30, 70, 1)  # Create buttons of board
        self.btn2 = self.createButtons(' ', 225, 70, 2)  # Create buttons of board
        self.btn3 = self.createButtons(' ', 420, 70, 3)  # Create buttons of board
        self.btn4 = self.createButtons(' ', 30, 240, 4)  # Create buttons of board
        self.btn5 = self.createButtons(' ', 225, 240, 5)  # Create buttons of board
        self.btn6 = self.createButtons(' ', 420, 240, 6)  # Create buttons of board
        self.btn7 = self.createButtons(' ', 30, 410, 7)  # Create buttons of board
        self.btn8 = self.createButtons(' ', 225, 410, 8)  # Create buttons of board
        self.btn9 = self.createButtons(' ', 420, 410, 9)  # Create buttons of board
        self.backgroundChange()
        self.gameFinishDelay = QTimer()
        self.center()
        self.show()

    #  *************************************************GUI Methods**************************************************

    def center(self):
        """align window center"""
        windowFrame = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(desktopWidget)
        self.move(windowFrame.topLeft())

    def musicPlayer(self):
        """Function to run a music in background"""
        filename = 'assets/background music/playerVSplayer.mp3'
        self.fullpath = QtCore.QDir.current().absoluteFilePath(filename)
        self.media = QtCore.QUrl.fromLocalFile(self.fullpath)
        self.content = QtMultimedia.QMediaContent(self.media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)
        self.player.setVolume(self.inGameVolume)
        self.player.play()

    def backgroundChange(self):
        """Change the background color of the game"""
        if self.lightMode:
            self.setStyleSheet("background-color:rgb(22, 22, 22)")
        else:
            self.setStyleSheet("background-color:white;"
                               "color: black;")

    def createPlayerRoleText(self, text):
        button = QPushButton('', self)
        button.setText(text)
        if not self.lightMode:
            button.setStyleSheet("background-color: none;"
                                 "border-style: outset;"
                                 "font: bold 14px;"
                                 "cursor: pointer;"
                                 "font-size:24pt;"
                                 "color: #FF9933;"
                                 "font-family: halo")
        else:
            button.setStyleSheet("background-color: none;"
                                 "border-style: outset;"
                                 "font: bold 14px;"
                                 "cursor: pointer;"
                                 "font-size:24pt;"
                                 "color: #d63031;"
                                 "font-family: halo")
        button.move(0, 0)
        button.resize(600, 100)
        return button

    def setPlayerText(self, player):
        self.playerRoleText.setText(player)
        if player == 'Player1':
            if not self.lightMode:
                self.playerRoleText.setStyleSheet("background-color: none;"
                                                  "border-style: outset;"
                                                  "font: bold 14px;"
                                                  "cursor: pointer;"
                                                  "font-size:24pt;"
                                                  "color: #FF9933;"
                                                  "font-family: halo")
            else:
                self.playerRoleText.setStyleSheet("background-color: none;"
                                                  "border-style: outset;"
                                                  "font: bold 14px;"
                                                  "cursor: pointer;"
                                                  "font-size:24pt;"
                                                  "color: #d63031;"
                                                  "font-family: halo")
        elif player == 'Player2':
            if not self.lightMode:
                self.playerRoleText.setStyleSheet("background-color: none;"
                                                  "border-style: outset;"
                                                  "font: bold 14px;"
                                                  "cursor: pointer;"
                                                  "color: #333366;"
                                                  "font-size:24pt;"
                                                  "font-family: halo;")
            else:
                self.playerRoleText.setStyleSheet("background-color: none;"
                                                  "border-style: outset;"
                                                  "font: bold 14px;"
                                                  "cursor: pointer;"
                                                  "color: #d4ff1e;"
                                                  "font-size:24pt;"
                                                  "font-family: halo;")

    def volumeHomeBtns(self):
        self.homeBtn = QPushButton(' ', self)
        self.homeBtn.resize(50, 50)
        self.homeBtn.move(30, 0)
        self.homeBtn.setIconSize(QSize(40, 40))
        self.homeBtn.clicked.connect(self.setHomeBtn)
        self.homeBtn.setStyleSheet("border-style: outset;"
                                   "background-color: none;"
                                   "border: none")
        self.homeBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.volumeBtn = QPushButton(' ', self)
        self.volumeBtn.setIconSize(QSize(40, 40))
        self.volumeBtn.clicked.connect(self.setVolumeBtn)
        self.volumeBtn.resize(50, 50)
        self.volumeBtn.move(510, 0)
        self.volumeBtn.setStyleSheet("border-style: outset;"
                                     "background-color: none;"
                                     "border: none")
        self.volumeBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        if self.inGameVolume != 0 and self.lightMode:
            self.volumeBtn.setIcon(QIcon('assets/icons/volume_light.png'))
            self.homeBtn.setIcon(QIcon('assets/icons/homepage_light.png'))
        elif self.inGameVolume == 0 and self.lightMode:
            self.volumeBtn.setIcon(QIcon('assets/icons/mute_light.png'))
            self.homeBtn.setIcon(QIcon('assets/icons/homepage_light.png'))
        elif self.inGameVolume != 0 and not self.lightMode:
            self.volumeBtn.setIcon(QIcon('assets/icons/volume_dark.png'))
            self.homeBtn.setIcon(QIcon('assets/icons/homepage_dark.png'))
        elif self.inGameVolume == 0 and not self.lightMode:
            self.volumeBtn.setIcon(QIcon('assets/icons/mute_dark.png'))
            self.homeBtn.setIcon(QIcon('assets/icons/homepage_dark.png'))

    def setVolumeBtn(self):
        """Set the button icon and value"""
        print('Muted!')
        if self.inGameVolume == 0:
            self.inGameVolume = self.volume
            self.player.setVolume(self.inGameVolume)
            if self.lightMode:
                self.volumeBtn.setIcon(QIcon('assets/icons/volume_light.png'))
            else:
                self.volumeBtn.setIcon(QIcon('assets/icons/volume_dark.png'))

        elif self.inGameVolume > 0:
            self.inGameVolume = 0
            self.player.setVolume(self.inGameVolume)
            if self.lightMode:
                self.volumeBtn.setIcon(QIcon('assets/icons/mute_light.png'))
            else:
                self.volumeBtn.setIcon(QIcon('assets/icons/mute_dark.png'))

    def setHomeBtn(self):
        print('Home!')
        self.player.stop()
        self.MenuUi = GameMenu.MenuInterface(self.lightMode, self.volume, self.botLevel)
        self.MenuUi.show()
        self.close()

    #  **************************************************Game methods**************************************************
    def setBoard(self, lettre, index):
        """Insert the letter X or O in the Board list"""
        self.board[index] = lettre

    def getButton(self, value):
        """Get the button object by the value"""
        if value == 1:
            return self.btn1
        elif value == 2:
            return self.btn2
        elif value == 3:
            return self.btn3
        elif value == 4:
            return self.btn4
        elif value == 5:
            return self.btn5
        elif value == 6:
            return self.btn6
        elif value == 7:
            return self.btn7
        elif value == 8:
            return self.btn8
        elif value == 9:
            return self.btn9
        return False

    def player1MoveEvent(self, value, word):
        """Actions will be applied when the player1 play or choose a position"""
        player = self.getButton(value)
        self.changeButtonStateX(player)
        self.setBoard(word, value - 1)

    def player2MoveEvent(self, value, word):
        """Actions will be applied when the player2 play or choose a position"""
        player = self.getButton(value)
        self.changeButtonStateO(player)
        self.setBoard(word, value - 1)

    def createButtons(self, title, moveX, moveY, value):
        """Create the buttons of the board and return the button object"""
        button = QPushButton(title, self)
        button.clicked.connect(partial(self.play, value))
        button.resize(150, 150)
        button.move(moveX, moveY)
        button.setStyleSheet("background-color: rgb(0, 178, 62);"
                             "border-style: outset;"
                             "font: bold 14px;"
                             "cursor: pointer;"
                             "font-size:72pt;"
                             "color: white;"
                             "font-family: consolas")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        return button

    def changeButtonStateX(self, button):
        """Change the button color and text to 'X' """
        button.setText('X')
        if not self.lightMode:
            button.setStyleSheet("background-color: #FF9933;"
                                 "border-style: outset;"
                                 "font-size: 72pt")
        else:
            button.setStyleSheet("background-color: #ff2525;"
                                 "border-style: outset;"
                                 "font-size: 72pt")

    def changeButtonStateO(self, button):
        """Change the button color and text to 'O' """
        button.setText('O')
        if not self.lightMode:
            button.setStyleSheet("background-color: #333366;"
                                 "border-style: outset;"
                                 "font-size: 72pt")
        else:
            button.setStyleSheet("background-color: #d4ff1e;"
                                 "border-style: outset;"
                                 "font-size: 72pt")

    def placeTokenMessage(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Warning)
        message.setWindowTitle('Warning')
        message.setText("Place already token")
        message.setInformativeText(
            'As you see that the position or move you choose was already taken and it has a letter'
            ' \'X\' or \'O\' so choose another empty place <br> <h4>Thanks ¯\_(ツ)_/¯</h4>')
        message.exec_()

    def gameFinishedMessageOnClick(self):
        """Show warning message when the game is finished and there is a click event"""
        message = QMessageBox()
        message.setIcon(QMessageBox.Warning)
        message.setWindowTitle('Warning')
        message.setText("Game finished")
        message.setInformativeText(
            'Stop it! please you are hearting me. The game is already finished'
            ' Althought you can replay if you want <br> <h4>Thanks (*^▽^*)</h4>')
        message.exec_()

    def isBoardFull(self, board):
        """This method will return true if the board true """
        for i in range(9):
            if board[i] == ' ':
                return False
        return True

    def winnerVerification(self, board, letter):
        """This method will return True if one of the 8 conditions is true"""
        return ((board[7 - 1] == letter and board[8 - 1] == letter and board[9 - 1] == letter) or
                (board[4 - 1] == letter and board[5 - 1] == letter and board[6 - 1] == letter) or
                (board[1 - 1] == letter and board[2 - 1] == letter and board[3 - 1] == letter) or
                (board[7 - 1] == letter and board[4 - 1] == letter and board[1 - 1] == letter) or
                (board[8 - 1] == letter and board[5 - 1] == letter and board[2 - 1] == letter) or
                (board[9 - 1] == letter and board[6 - 1] == letter and board[3 - 1] == letter) or
                (board[7 - 1] == letter and board[5 - 1] == letter and board[3 - 1] == letter) or
                (board[9 - 1] == letter and board[5 - 1] == letter and board[1 - 1] == letter))

    def playerWon(self, player):
        self.gameFinishDelay.stop()
        if player == 'player1':
            print("player1  won")
            self.player.stop()
            self.finishUi = SaveData.SaveData(self.lightMode, self.volume, self.botLevel, self.gameMode, 'player1')
            self.close()
        elif player == 'player2':
            print("player2 won")
            self.player.stop()
            self.finishUi = SaveData.SaveData(self.lightMode, self.volume, self.botLevel, self.gameMode, 'player2')
            self.close()
        else:
            print("Tie game")
            self.player.stop()
            self.finishUi = SaveData.SaveData(self.lightMode, self.volume, self.botLevel, self.gameMode, 'tie')
            self.close()

    def play(self, value):
        """Main function of the game"""

        if self.winnerVerification(self.board, 'X') or self.winnerVerification(self.board, 'O'):
            self.gameFinishedMessageOnClick()
            return 0

        if self.player1Role and not self.player2Role:
            if self.board[value - 1] != ' ':
                self.placeTokenMessage()
                return 0
            self.player1MoveEvent(value, 'X')
            self.player1Role = False
            self.player2Role = True
            self.setPlayerText('Player2')
            print(self.board)
            if self.winnerVerification(self.board, 'X'):
                #self.playerWon('player1')
                self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'player1'))
                self.gameFinishDelay.start(2000)
                print('done')
            if self.isBoardFull(self.board):
                print('Board full')
                #self.playerWon('tie')
                self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'tie'))
                self.gameFinishDelay.start(2000)
            else:
                print('Board not full yet')
        else:
            if self.board[value - 1] != ' ':
                self.placeTokenMessage()
                return 0
            self.player2MoveEvent(value, 'O')
            self.player1Role = True
            self.player2Role = False
            self.setPlayerText('Player1')
            print(self.board)
            if self.winnerVerification(self.board, 'O'):
                #self.playerWon('player2')
                self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'player2'))
                self.gameFinishDelay.start(2000)
                print('done')
            if self.isBoardFull(self.board):
                print('Board full')
                #self.playerWon('tie')
                self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'tie'))
                self.gameFinishDelay.start(2000)
            else:
                print('Board not full yet')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameInterface()
    sys.exit(app.exec_())
