import sys
from functools import partial

from PyQt5 import QtCore
from PyQt5 import QtMultimedia
from PyQt5.QtCore import QTimer, QSize
from PyQt5.QtGui import QIcon, QCursor, QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QMessageBox, QPushButton
import random
import GameMenu
import SaveData


class CPUVSPlayer(QMainWindow):
    def __init__(self, lightMode, volume, botLevel, gameMode):
        super().__init__()
        self.lightMode = lightMode
        self.volume = volume
        self.inGameVolume = volume
        self.botLevel = botLevel
        self.gameMode = gameMode
        self.compMove = 0  # initial computer move
        self.setWindowTitle('Tic Tac Toe')
        self.setWindowIcon(QIcon('assets/icons/favicon.png'))
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.setGeometry(600, 600, 600, 600)
        self.musicPlayer()
        QFontDatabase.addApplicationFont('assets/fonts/HALO____.ttf')
        self.playerRoleText = self.createPlayerRoleText('Player1')
        self.volumeHomeBtns()
        self.board = [' ' for i in range(9)]  # Game main board
        self.compRound = False
        self.playerRound = True
        self.bot1Round = True
        self.bot2Round = False
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
        #  Bot Vs Bot
        self.bot2Timer = QTimer()  # bot1 delay
        self.bot1Timer = QTimer()  # bot 2 delay
        self.gameFinishDelay = QTimer()  # this will add 2 sec delay after the game finish
        if self.gameMode == 'Bot VS Bot':
            self.setPlayerText('Bot1', 1)
            self.BotVSBot()
        self.center()
        self.show()

    def center(self):
        """align window center"""
        windowFrame = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(desktopWidget)
        self.move(windowFrame.topLeft())

    def musicPlayer(self):
        """Function to run a music in background"""
        if self.gameMode == 'Bot VS Bot':
            filename = 'assets/background music/compVScomp.mp3'
        else:
            filename = 'assets/background music/playerVScomp.mp3'
        self.fullpath = QtCore.QDir.current().absoluteFilePath(filename)
        self.media = QtCore.QUrl.fromLocalFile(self.fullpath)
        self.content = QtMultimedia.QMediaContent(self.media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)
        self.player.setVolume(self.volume)
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

    def setPlayerText(self, player, number):
        self.playerRoleText.setText(player)
        if number == 1:
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
        elif number == 2:
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
        self.bot1Timer.stop()
        self.bot2Timer.stop()
        self.MenuUi = GameMenu.MenuInterface(self.lightMode, self.volume, self.botLevel)
        self.MenuUi.show()
        self.close()

    # **********************************************Game Methods*****************************************************
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

    def cpuMoveEvent(self, value, word):
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
        """Show warning or error message when a player try to choose a chosen place"""
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

    def botGameMessage(self):
        """Show warning message if the player choose a place while it's a Bot vs Bot game"""
        message = QMessageBox()
        message.setIcon(QMessageBox.Warning)
        message.setWindowTitle('Warning')
        message.setText("Can't choose")
        message.setInformativeText(
            'Stop it! this is a BOT VS BOT game you are not allowed to take places.'
            ' Maybe if you go for a game Vs the PC you will <br> <h4>Thanks (*^▽^*)</h4>')
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
        """Open the save data class to save the data of game"""
        self.gameFinishDelay.stop()
        if player == 'player':
            print("player  won")
            self.player.stop()
            self.finishUi = SaveData.SaveData(self.lightMode, self.volume, self.botLevel, self.gameMode, 'player')
            self.close()
        elif player == 'bot':
            print("bot won")
            self.player.stop()
            self.finishUi = SaveData.SaveData(self.lightMode, self.volume, self.botLevel, self.gameMode, 'bot')
            self.close()
        elif player == 'bot1':
            print("bot1 won")
            self.player.stop()
            self.finishUi = SaveData.SaveData(self.lightMode, self.volume, self.botLevel, self.gameMode, 'bot1')
            self.close()
        elif player == 'bot2':
            print("bot2 won")
            self.player.stop()
            self.finishUi = SaveData.SaveData(self.lightMode, self.volume, self.botLevel, self.gameMode, 'bot2')
            self.close()
        else:
            print("Tie game")
            self.player.stop()
            self.finishUi = SaveData.SaveData(self.lightMode, self.volume, self.botLevel, self.gameMode, 'tie')
            self.close()

    def possibleMoves(self):
        """Return a list containing the index of free places"""
        dispoPlaces = []
        for i in range(9):
            if self.board[i] == ' ':
                dispoPlaces.append(i)
        return dispoPlaces


    def computerMove(self):
        """The computer move AI based on the bot level"""
        if self.botLevel == 1:
            #  the super AI
            possibleMoves = self.possibleMoves()
            self.compMove = 0
            #  step 1 get the wining move or block player waining move
            for letter in ['O', 'X']:
                for i in possibleMoves:
                    copyBoard = self.board[:]  # create a copy from original board to let the computer test in it
                    copyBoard[i] = letter
                    if self.winnerVerification(copyBoard, letter):
                        self.compMove = i
                        return self.compMove
            #  step 2 get the middle place if its free
            if 4 in possibleMoves:
                return 4

            #  special step for some cases the pc will take an edge if the user took 2 corners
            takeFreeEdge = []  # list witch contain the free corners
            for i in possibleMoves:
                if i in [1, 3, 5, 7]:
                    takeFreeEdge.append(i)
            tokenCorners = 0  # present token corners by the player if < 2 then the pc will choose a free edge
            for i in [0, 2, 6, 8]:
                if self.board[i] == 'X':
                    tokenCorners += 1
                    print(tokenCorners)
            if tokenCorners >= 2:
                self.compMove = random.choice(takeFreeEdge)
                return self.compMove

            #  step 3 take one of the free corners

            cornersFree = []  # list witch contain the free corners
            for i in possibleMoves:
                if i in [0, 2, 6, 8]:
                    cornersFree.append(i)

            if len(cornersFree) > 0:
                self.compMove = random.choice(cornersFree)
                return self.compMove

            # step 4 take a random free edge if there is any place for win or block option and the middle is token
            # and corners token too
            edgesFree = []  # list witch contain the free corners
            for i in possibleMoves:
                if i in [1, 3, 5, 7]:
                    edgesFree.append(i)

            if len(edgesFree) > 0:
                self.compMove = random.choice(edgesFree)
                return self.compMove

        elif self.botLevel == 2:
            #  the medium AI
            possibleMoves = self.possibleMoves()
            self.compMove = 0
            #  step 1 get the wining move or block player waining move
            for letter in ['O', 'X']:
                for i in possibleMoves:
                    copyBoard = self.board[:]  # create a copy from original board to let the computer test in it
                    copyBoard[i] = letter
                    if self.winnerVerification(copyBoard, letter):
                        self.compMove = i
                        return self.compMove
            #  step 2 get a random value
            if len(possibleMoves) > 0:
                self.compMove = random.choice(possibleMoves)
                return self.compMove
        elif self.botLevel == 3:
            #  basically no brain just random
            possibleMoves = self.possibleMoves()
            if len(possibleMoves) > 0:
                self.compMove = random.choice(possibleMoves)
                return self.compMove
        return 0

    def comupterRole(self, letter):
        """This where the computer will insert the move in the board and change the button state, this function made
        mainly for the QTimer delay"""
        cpuMove = self.computerMove()
        if self.isBoardFull(self.board):
            print('Board full')
            # self.playerWon('tie')
            self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'tie'))
            self.gameFinishDelay.start(2000)
            return 0
        self.cpuMoveEvent(cpuMove + 1, letter)
        print(self.board)
        if self.winnerVerification(self.board, letter):
            # self.playerWon('bot')
            self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'bot'))
            self.gameFinishDelay.start(2000)
            print('Game Finished')

    def computerVsPlayerRole(self):
        self.comupterRole('O')
        self.setPlayerText('Player1', 1)
        self.compRound = False
        self.playerRound = True
        self.timer.stop()  # stop the QTimer loop

    def play(self, value):
        """Main function of the game"""
        if self.gameMode == 'Bot VS Bot':
            self.botGameMessage()
            return 0
        if self.winnerVerification(self.board, 'X') or self.winnerVerification(self.board, 'O'):
            self.gameFinishedMessageOnClick()
            return 0
        # This if to stop the player from pick other places when the pc in QTimer period
        if self.compRound and not self.playerRound:
            return 0
        if self.board[value - 1] != ' ':
            self.placeTokenMessage()
            return 0
        self.player1MoveEvent(value, 'X')
        self.compRound = True
        self.playerRound = False
        self.setPlayerText('BOT', 2)
        print(self.board)
        if self.winnerVerification(self.board, 'X'):
            # self.playerWon('player1')
            self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'player'))
            self.gameFinishDelay.start(2000)
            print('Game Finished')
            return 0
        if self.isBoardFull(self.board):
            print('Board full')
            # self.playerWon('tie')
            self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'tie'))
            self.gameFinishDelay.start(2000)
            return 0
        else:
            print('Board not full yet')
            # Computer role
            self.timer = QTimer()  # 1 sec delay between player and cpu move
            self.timer.timeout.connect(self.computerVsPlayerRole)
            self.timer.start(1000)

    def computer2Role(self):
        if self.bot1Round and not self.bot2Round:
            return 0
        cpu2Move = self.computerMove()
        self.cpuMoveEvent(cpu2Move + 1, 'O')
        self.setPlayerText('Bot1', 1)
        self.bot1Round = True
        self.bot2Round = False
        print(self.board)
        if self.winnerVerification(self.board, 'O'):
            # self.playerWon('bot2')
            print('Game Finished')
            self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'bot2'))
            self.gameFinishDelay.start(2000)
            self.bot1Timer.stop()
            self.bot2Timer.stop()
            return 0

    def secondBotDelay(self):
        self.computer2Role()
        self.bot1Timer.timeout.connect(self.BotVSBot)
        self.bot1Timer.start(2000)
        if self.isBoardFull(self.board):
            print('Board full')
            self.playerWon('tie')
            self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'tie'))
            self.gameFinishDelay.start(2000)
            self.bot1Timer.stop()
            self.bot2Timer.stop()

    def BotVSBot(self):
        """Cpu Vs Cpu"""
        if self.winnerVerification(self.board, 'O'):
            #  Stop the QTimer to continue if *Bot 2 win
            return 0
        if self.bot2Round and not self.bot1Round:
            return 0
        cpu1Move = self.computerMove()
        self.player1MoveEvent(cpu1Move + 1, 'X')
        self.setPlayerText('Bot2', 2)
        self.bot1Round = False
        self.bot2Round = True
        print(self.board)
        if self.winnerVerification(self.board, 'X'):
            # self.playerWon('bot1')
            print('Game Finished')
            self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'bot1'))
            self.gameFinishDelay.start(2000)
            self.bot1Timer.stop()
            self.bot2Timer.stop()
            return 0
        # CPU2 role
        self.bot2Timer.timeout.connect(self.secondBotDelay)
        self.bot2Timer.start(2000)
        if self.isBoardFull(self.board):
            print('Board full')
            # self.playerWon('tie')
            self.gameFinishDelay.timeout.connect(partial(self.playerWon, 'tie'))
            self.gameFinishDelay.start(2000)
            self.bot1Timer.stop()
            self.bot2Timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CPUVSPlayer()
    sys.exit(app.exec_())
